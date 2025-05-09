import os
from collections import Iterable

from pynwb import register_class, load_namespaces, NWBContainer, ProcessingModule
from pynwb.form.utils import docval, call_docval_func, popargs
import numpy as np


ns_path = os.path.join(os.path.dirname(__file__), 'data/dummy.namespace.yaml')
load_namespaces(ns_path)


@register_class('DummyClass', 'dummy')
class DummyClass(NWBContainer):
    """
    """

    __nwbfields__ = ('name', 'anarray', 'afloat')

    @docval({'name': 'name', 'type': str, 'doc': 'the name of this thing'},
            {'name': 'source', 'type': str, 'doc': 'required'},
            {'name': 'anarray', 'type': (Iterable), 'doc': 'an array'},
            {'name': 'afloat', 'type': float, 'doc': 'a float'})
    def __init__(self, **kwargs):
        call_docval_func(super(DummyClass, self).__init__, kwargs)
        self.anarray = popargs('anarray', kwargs)
        self.afloat = popargs('afloat', kwargs)
