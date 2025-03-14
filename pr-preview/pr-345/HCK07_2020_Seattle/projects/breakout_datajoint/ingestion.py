import os
import re
import pathlib
import h5py as h5
import numpy as np
from decimal import Decimal
import datajoint as dj
import pynwb
from datetime import datetime
from dateutil.tz import tzlocal
import warnings

from pipeline import (subject, experiment, intracellular, utilities)

warnings.filterwarnings('ignore')


# ================== Dataset ==================
path = pathlib.Path(dj.config['custom'].get('intracellular_directory')).as_posix()
fnames = os.listdir(path)

for fname in fnames[:3]:
    try:
        nwb = h5.File(os.path.join(path, fname), 'r')
        print(f'File loaded: {fname}')
    except:
        print('=================================')
        print(f'!!! ERROR LOADING FILE: {fname}')
        print('=================================')
        continue

    # ========================== METADATA ==========================
    # ==================== subject ====================
    subject_info = {c: nwb['general']['subject'][c][()].decode('UTF-8')
                    for c in ('subject_id', 'description', 'sex', 'species', 'weight', 'age', 'genotype')}
    # force subject_id to be lower-case for consistency
    subject_info['subject_id'] = subject_info['subject_id'].lower()

    # dob and sex
    subject_info['sex'] = subject_info['sex'][0].upper()
    dob_str = re.search('(?<=Date of birth:\s)(.*)', subject_info['description'])
    if utilities.parse_prefix(dob_str.group()) is not None:
        subject_info['date_of_birth'] = utilities.parse_prefix(dob_str.group())

    # allele
    allele_str = re.search('(?<=Animal Strain:\s)(.*)',
                           subject_info['description']).group()  # extract the information related to animal allele
    allele_dict = {alias.lower(): allele for alias, allele in subject.AlleleAlias.fetch()}
    regex_str = '|'.join([re.escape(alias) for alias in allele_dict.keys()])
    alleles = [allele_dict[s.lower()] for s in re.findall(regex_str, allele_str, re.I)]
    # source
    source_str = re.search('(?<=Animal source:\s)(.*)',
                           subject_info['description']).group()  # extract the information related to animal allele
    source_dict = {alias.lower(): source for alias, source in subject.AnimalSourceAlias.fetch()}
    regex_str = '|'.join([re.escape(alias) for alias in source_dict.keys()])
    subject_info['animal_source'] = source_dict[re.search(regex_str, source_str, re.I).group().lower()] if re.search(
        regex_str, source_str, re.I) else 'N/A'

    with subject.Subject.connection.transaction:
        if subject_info not in subject.Subject.proj():
            subject.Subject.insert1(subject_info, ignore_extra_fields=True)
            subject.Subject.Allele.insert((dict(subject_info, allele=k)
                                           for k in alleles), ignore_extra_fields=True)

    # ==================== session ====================
    # -- session_time
    session_time = utilities.parse_prefix(nwb['session_start_time'].value)
    if session_time is not None:
        session_info = dict(
            experiment_description=nwb['general']['experiment_description'][()],
            institution=nwb['general']['institution'][()],
            related_publications=nwb['general']['related_publications'][()].decode('UTF-8'),
            session_id=nwb['general']['session_id'][()],
            surgery=nwb['general']['surgery'][()].decode('UTF-8'),
            identifier=nwb['identifier'][()],
            nwb_version=nwb['nwb_version'][()],
            session_note=nwb['session_description'][()],
            session_time=session_time)

        experimenters = nwb['general']['experimenter'][()]
        experiment_types = re.split('Experiment type: ', session_info['session_note'])[-1]
        experiment_types = re.split(',\s?', experiment_types)

        # experimenter and experiment type (possible multiple experimenters or types)
        experimenters = [experimenters] if np.array(
            experimenters).size <= 1 else experimenters  # in case there's only 1 experimenter

        experiment.Experimenter.insert(zip(experimenters), skip_duplicates=True)
        experiment.ExperimentType.insert(zip(experiment_types), skip_duplicates=True)

        if dict(subject_info, session_time=session_time) not in experiment.Session.proj():

            nwb_file = pynwb.file.NWBFile(identifier='_'.join(
                [str(subject_info['subject_id']),
                 session_info['session_time'].strftime('%y%m%d_%H%M%S')]),
                session_description=session_info['session_note'],
                session_start_time=session_info['session_time'],
                file_create_date=datetime.now(tzlocal()),
                experimenter=experimenters)
            # -- subject
            nwb_file.subject = pynwb.file.Subject(
                subject_id=subject_info['subject_id'],
                genotype=' x '.join(alleles),
                sex=subject_info['sex'],
                species=subject_info['species'],
                date_of_birth=subject_info['date_of_birth'] if subject_info['date_of_birth'] else None)

            experiment.Session.insert1({**subject_info, **session_info, 'nwb_file': nwb_file}, ignore_extra_fields=True)
            experiment.Session.Experimenter.insert(
                (dict({**subject_info, **session_info}, experimenter=k) for k in experimenters),
                ignore_extra_fields=True)
            experiment.Session.ExperimentType.insert(
                (dict({**subject_info, **session_info}, experiment_type=k) for k in experiment_types),
                ignore_extra_fields=True)
        print(f'Creating Session - Subject: {subject_info["subject_id"]} - Date: {session_info["session_time"]}')

    # ==================== Intracellular ====================
    # -- read data - devices
    devices = {d: nwb['general']['devices'][d][()].decode('UTF-8') for d in nwb['general']['devices']}

    # -- read data - intracellular_ephys
    ie_filtering = nwb['general']['intracellular_ephys']['whole_cell']['filtering'][()]

    ie_location = nwb['general']['intracellular_ephys']['whole_cell']['location'][()]
    brain_region = re.split(',\s?', ie_location)[-1]
    coord_ap_ml_dv = re.findall('\d+.\d+', ie_location)

    # -- Whole Cell Device
    ie_device = nwb['general']['intracellular_ephys']['whole_cell']['device'][()]
    nwb_device = pynwb.device.Device(name=ie_device)
    if {'device_name': ie_device} not in intracellular.WholeCellDevice.proj():
        intracellular.WholeCellDevice.insert1({'device_name': ie_device,
                                               'nwb_device': nwb_device})

    # -- BrainLocation
    # hemisphere: left-hemisphere is ipsi, so anything contra is right
    brain_region, hemisphere = utilities.get_brain_hemisphere(brain_region)
    brain_location = {'brain_region': brain_region,
                      'hemisphere': hemisphere}
    brain_location = dict(brain_location,
                          coordinate_ref='bregma',
                          coordinate_ap=round(Decimal(coord_ap_ml_dv[0]), 2),
                          coordinate_ml=round(Decimal(coord_ap_ml_dv[1]), 2),
                          coordinate_dv=round(Decimal(coord_ap_ml_dv[2]), 2))

    if brain_location not in intracellular.BrainLocation.proj():
        intracellular.BrainLocation.insert1(brain_location)

        # -- Intracellular Electrode
        ic_electrode = pynwb.icephys.IntracellularElectrode(
            name=brain_location['hemisphere'] + brain_location['brain_region'],
            device=nwb_device, description='N/A', filtering='low-pass: 10kHz',
            location='; '.join([f'{k}: {str(v)}' for k, v in brain_location.items()]))

        intracellular.IntracellularElectrode.insert1({'brain_region': brain_region,
                                                      'hemisphere': hemisphere,
                                                      'device_name': ie_device,
                                                      'ic_electrode': ic_electrode})

    # -- Cell
    cell_id = re.split('.nwb', session_info['session_id'])[0]
    cell_key = {**subject_info, **session_info, **brain_location, 'cell_id': cell_id}
    if cell_key not in intracellular.Cell.proj():
        intracellular.Cell.insert1(dict(cell_key, cell_type='N/A',
                                        brain_region=brain_region,
                                        hemisphere=hemisphere), ignore_extra_fields=True)

    nwb.close()
