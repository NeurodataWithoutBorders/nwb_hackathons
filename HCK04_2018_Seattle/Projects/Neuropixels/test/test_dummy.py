from datetime import datetime

import pytest
import numpy as np

from pynwb import NWBFile, ProcessingModule
from nwb_test_utilities import roundtrip_test

from high_density_ecephys.dummy import DummyClass


def test_dummy(tmpdir_factory):

    arr = np.linspace(0, 1, 300)
    dummy_instance = DummyClass(name='my_instance', source='imagination', afloat=5.0, anarray=arr)
    
    module = ProcessingModule(name='my_module', source='imagination', description='foo', containers=[dummy_instance])
    nwbfile = NWBFile('name', 'source', '?', datetime.now(), modules=[module])
    
    file_path = tmpdir_factory.mktemp('data').join('test.nwb')

    roundtrip_test(nwbfile, file_path)
    assert(np.array_equal( nwbfile.modules['my_module'].containers[0].anarray, arr  ))
    assert(np.array_equal( nwbfile.modules['my_module'].containers[0].afloat, 5.0  ))