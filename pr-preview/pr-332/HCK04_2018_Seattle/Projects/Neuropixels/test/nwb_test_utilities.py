import collections

import pytest
import numpy as np
from pynwb import NWBFile, get_manager, NWBHDF5IO, NWBContainer, NWBData

def assert_container_equal(astack, bstack):

    astack = list(astack)
    bstack = list(bstack)

    while astack or bstack:
        a, astack, key_order = stack_step(astack)
        b, bstack, _ = stack_step(bstack, key_order)

        if isinstance(a, NWBContainer) or isinstance(a, dict):
            assert( type(a) == type(b) )
            assert_container_equal(astack, bstack)
        elif isinstance(a, NWBData):
            assert_data_equal(a, b)
        elif isinstance(a, (list, tuple)):
            assert(len(a) == len(b))
        elif isinstance(a, (str, int, float, bool, type(None))):
            assert( a == b )
        else:
            assert(np.allclose( np.array(a), np.array(b) ))


def stack_step(stack, key_order=None):
    new = stack.pop()

    if hasattr(new, '__nwbfields__'):
        stack.extend([ getattr(new, f) for f in new.__nwbfields__ ])

    if isinstance(new, dict):
        if key_order is None:
            key_order = list(new.keys())
        stack.extend([ new[f] for f in key_order ])
    elif isinstance(new, (list, tuple)):
        stack.extend(list(new))

    return new, stack, key_order


def assert_data_equal(a, b):
    assert(type(a) == type(b))
    assert(len(a) == len(b))


def roundtrip_test(nwbfile, file_path):

    io = NWBHDF5IO(str(file_path))
    io.write(nwbfile)
    obt = io.read(str(file_path))

    assert_container_equal( [nwbfile], [obt] )