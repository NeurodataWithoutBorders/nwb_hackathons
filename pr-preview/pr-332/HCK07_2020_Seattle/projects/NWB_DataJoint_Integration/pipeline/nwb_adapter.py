import datajoint as dj
import pathlib
import pynwb
from pynwb import NWBHDF5IO
import warnings

warnings.filterwarnings('ignore')

exported_nwb_dir = dj.config['stores']['nwb_store']['stage']

nwb_session_dir = pathlib.Path(exported_nwb_dir, 'session')
nwb_mp_dir = pathlib.Path(exported_nwb_dir, 'membrane_potential')

nwb_session_dir.mkdir(parents=True, exist_ok=True)
nwb_mp_dir.mkdir(parents=True, exist_ok=True)


class NWBFile(dj.AttributeAdapter):
    """ Adapter for: pynwb.file.NWBFile"""
    attribute_type = 'filepath@nwb_store'

    def put(self, nwb):
        save_file_name = ''.join([nwb.identifier, '.nwb'])
        save_fp = nwb_session_dir / save_file_name

        print(f'Write NWBFile: {save_file_name}')
        _write_nwb(save_fp, nwb)
        return save_fp.as_posix()

    def get(self, path):
        io = NWBHDF5IO(str(pathlib.Path(path)), mode='r')
        nwb = io.read()
        nwb.io = io
        return nwb


class Device(dj.AttributeAdapter):
    """ Adapter for: pynwb.device.Device"""
    attribute_type = 'longblob'

    def put(self, nwb_device):
        return {'name': nwb_device.name}

    def get(self, device_dict):
        return pynwb.device.Device(name=device_dict['name'])


class IntracellularElectrode(dj.AttributeAdapter):
    """ Adapter for: pynwb.icephys.IntracellularElectrode"""
    attribute_type = 'longblob'

    def put(self, electrode):
        return dict(name=electrode.name, device=Device().put(electrode.device),
                    description=electrode.description, filtering=electrode.filtering,
                    location=electrode.location)

    def get(self, ic_electrode_dict):
        return pynwb.icephys.IntracellularElectrode(
            name=ic_electrode_dict['name'],
            device=Device().get(ic_electrode_dict['device']),
            description=ic_electrode_dict['description'],
            filtering=ic_electrode_dict['filtering'],
            location=ic_electrode_dict['location'])


class PatchClampSeries(dj.AttributeAdapter):
    """ Adapter for: pynwb.icephys.PatchClampSeries"""
    attribute_type = 'filepath@nwb_store'

    def put(self, patch_clamp):
        nwb = patch_clamp.parent

        nwb.add_device(patch_clamp.electrode.device)
        nwb.add_ic_electrode(patch_clamp.electrode)
        nwb.add_acquisition(patch_clamp)

        save_file_name = ''.join([nwb.identifier + '_{}'.format(patch_clamp.name), '.nwb'])
        save_fp = nwb_mp_dir / save_file_name

        print(f'Write PatchClampSeries: {save_file_name}')
        _write_nwb(save_fp, nwb, manager=nwb.io.manager)
        return save_fp.as_posix()

    def get(self, path):
        io = NWBHDF5IO(str(pathlib.Path(path)), mode='r')
        nwb = io.read()
        patch_clamp = [obj for obj in nwb.objects.values()
                       if obj.neurodata_type == 'PatchClampSeries'][0]
        patch_clamp.io = io
        return patch_clamp


# ============= HELPER FUNCTIONS ===============

def _write_nwb(save_fp, nwb2write, manager=None):
    try:
        with NWBHDF5IO(save_fp.as_posix(), mode='w', manager=manager) as io:
            io.write(nwb2write)
    except Exception as e:
        if save_fp.exists():
            save_fp.unlink()
        raise e


# ==== instantiate dj.AttributeAdapter objects ====

nwb_file = NWBFile()
device = Device()
patch_clamp_series = PatchClampSeries()
ic_electrode = IntracellularElectrode()
