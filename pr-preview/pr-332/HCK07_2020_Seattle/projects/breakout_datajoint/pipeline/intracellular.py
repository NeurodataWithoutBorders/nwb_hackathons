import os
import pathlib
import numpy as np
import datajoint as dj
import h5py as h5
import pynwb

from . import experiment, utilities
from .nwb_adapter import *

schema = dj.schema(dj.config['custom'].get('database.prefix', '') + 'intracellular')

sess_data_dir = pathlib.Path(dj.config['custom'].get('intracellular_directory')).as_posix()


@schema
class WholeCellDevice(dj.Lookup):
    definition = """ # Description of the device used for electrical stimulation
    device_name: varchar(32)
    ---
    nwb_device: <device>
    """


@schema
class BrainLocation(dj.Manual):
    definition = """
    brain_region: varchar(32)
    hemisphere: enum('left', 'right')
    ---
    coordinate_ref: enum('bregma', 'lambda')
    coordinate_ap: decimal(4,2)    # in mm, anterior positive, posterior negative 
    coordinate_ml: decimal(4,2)    # in mm, always postive, number larger when more lateral
    coordinate_dv: decimal(4,2)    # in mm, always postive, number larger when more ventral (deeper)
    """


@schema
class IntracellularElectrode(dj.Manual):
    definition = """
    -> BrainLocation
    ---
    -> WholeCellDevice
    ic_electrode: <ic_electrode>
    """


@schema
class Cell(dj.Manual):
    definition = """ # A cell undergone intracellular recording in this session
    -> experiment.Session
    cell_id: varchar(36) # a string identifying the cell in which this intracellular recording is concerning
    ---
    cell_type: enum('excitatory','inhibitory','N/A')
    -> IntracellularElectrode
    """


@schema
class MembranePotential(dj.Imported):
    definition = """
    -> Cell
    ---
    nwb_patch_clamp: <patch_clamp_series>
    """

    def make(self, key):
        # ============ Dataset ============
        # Get the Session definition from the keys of this session
        animal_id = key['subject_id']
        date_of_experiment = key['session_time']
        # Search the files in filenames to find a match for "this" session (based on key)
        sess_data_file = utilities.find_session_matched_nwbfile(sess_data_dir, animal_id, date_of_experiment)
        if sess_data_file is None:
            raise FileNotFoundError(f'IntracellularAcquisition import failed for: {animal_id} - {date_of_experiment}')
        nwb = h5.File(os.path.join(sess_data_dir, sess_data_file), 'r')
        #  ============= Now read the data and start ingesting =============
        print('Insert intracellular data for: subject: {0} - date: {1} - cell: {2}'.format(key['subject_id'],
                                                                                           key['session_time'],
                                                                                           key['cell_id']))

        mp = nwb['acquisition']['timeseries']['membrane_potential']['data'][()]
        mp_time_stamps = nwb['acquisition']['timeseries']['membrane_potential']['timestamps'][()]
        mp_start_time = mp_time_stamps[0]
        mp_fs = 1 / np.mean(np.diff(mp_time_stamps))

        # -- pynwb.icephys.PatchClampSeries --
        patch_clamp = pynwb.icephys.PatchClampSeries(name='_'.join([key['cell_id'], 'membrane_potential']),
                                                     electrode=(IntracellularElectrode & key).fetch1('ic_electrode'),
                                                     unit='mV',
                                                     conversion=1e-3, gain=1.0,
                                                     data=mp, starting_time=mp_start_time, rate=mp_fs)

        sess_nwb = (experiment.Session & key).fetch1('nwb_file')
        patch_clamp.parent = sess_nwb.copy()
        patch_clamp.parent.io = sess_nwb.io

        # -- MembranePotential
        self.insert1(dict(key, nwb_patch_clamp=patch_clamp))
        nwb.close()
