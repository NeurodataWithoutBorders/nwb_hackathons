import os
from datetime import datetime
import re
import h5py as h5

# datetime format - should probably read this from a config file and not hard coded here
datetimeformat_ymdhms = '%Y-%m-%d %H:%M:%S'
datetimeformat_ymd = '%Y-%m-%d'


def parse_prefix(line):
    cover = len(datetime.now().strftime(datetimeformat_ymdhms))
    try:
        return datetime.strptime(line[:cover], datetimeformat_ymdhms)
    except Exception as e:
        msg = f'Error:  {str(e)} \n'
        cover = len(datetime.now().strftime(datetimeformat_ymd))
        try:
            return datetime.strptime(line[:cover], datetimeformat_ymd)
        except Exception as e:
            print(f'{msg}\t{str(e)}\n\tReturn None')
            return None


def find_session_matched_nwbfile(sess_data_dir, animal_id, date_of_experiment):
    ############## Dataset #################

    sess_data_files = os.listdir(sess_data_dir)
    which_data = re.search('extracellular|whole_cell', sess_data_dir).group()
    # Search the filenames to find a match for "this" session (based on key)
    sess_data_file = None
    for s in sess_data_files:
        try:
            temp_nwb = h5.File(os.path.join(sess_data_dir, s), 'r')
        except:
            print(f'!!! error load file: {s}')
            continue
        # read subject_id out of this file
        subject_id = temp_nwb['general']['subject']['subject_id'].value.decode('UTF-8').lower()

        # -- session_time - due to error in extracellular dataset (session_start_time error), need to hard code here...
        if which_data == 'whole_cell':  # case: whole cell
            session_start_time = temp_nwb['session_start_time'].value
            session_start_time = parse_prefix(session_start_time)
        elif which_data == 'extracellular':  # case: extracellular
            identifier = temp_nwb['identifier'].value
            session_start_time = re.split(';\s?', identifier)[-1].replace('T', ' ')
            session_start_time = parse_prefix(session_start_time)

        # compare key with extracted info from this file
        if (animal_id == subject_id) and (date_of_experiment == session_start_time):
            # if true, meaning the current "nwb" variable is a match with this session
            sess_data_file = s
            break
        temp_nwb.close()

    # If session not found from dataset, break
    if sess_data_file is None:
        print(f'Session not found! - Subject: {animal_id} - Date: {date_of_experiment}')
        return None
    else:
        print(f'Found datafile: {sess_data_file}')
        return sess_data_file


def get_brain_hemisphere(brain_region):
    # hemisphere: left-hemisphere is ipsi, so anything contra is right
    if re.search('Contra\s?', brain_region) is not None:
        hemi = 'right'
        brain_region = re.sub('Contra\s?', '', brain_region)
    else:
        hemi = 'left'
    return brain_region, hemi

