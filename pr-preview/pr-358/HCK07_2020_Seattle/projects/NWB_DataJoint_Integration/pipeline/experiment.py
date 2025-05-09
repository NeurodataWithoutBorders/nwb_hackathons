import datajoint as dj

from . import subject
from .nwb_adapter import *

schema = dj.schema(dj.config['custom'].get('database.prefix', '') + 'experiment')


@schema
class ExperimentType(dj.Lookup):
    definition = """
    experiment_type: varchar(64)
    """
    contents = [['behavior'], ['extracelluar'], ['photostim']]


@schema
class Experimenter(dj.Lookup):
    definition = """
    experimenter: varchar(64)
    """


@schema
class Session(dj.Manual):
    definition = """
    -> subject.Subject
    session_time: datetime    # session time
    ---
    session_note = "" : varchar(256) 
    nwb_file: <nwb_file>
    """

    class Experimenter(dj.Part):
        definition = """
        -> master
        -> Experimenter
        """

    class ExperimentType(dj.Part):
        definition = """
        -> master
        -> ExperimentType
        """

