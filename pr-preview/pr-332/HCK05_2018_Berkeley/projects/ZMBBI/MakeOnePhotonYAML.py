import pynwb
import ruamel.yaml as yaml
import numpy as np
import json

from pynwb import load_namespaces, get_class
from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, NWBAttributeSpec

ns_path = "mylab.namespace.yaml"
ext_source = "mylab.extensions.yaml"

ns_builder = NWBNamespaceBuilder('Extension for use in my Lab', "mylab")
ext = NWBGroupSpec('A custom ElectricalSeries for my lab',
                   attributes=[NWBAttributeSpec('bins', 'int', 'the downsample bins')],
                   neurodata_type_inc='ImageSeries',
                   neurodata_type_def='OnePhotonSeries')

ns_builder.add_spec(ext_source, ext)
ns_builder.export(ns_path)

x = yaml.load(open(ext_source, 'r'), Loader=yaml.Loader)
print(json.dumps(x, indent=2))

load_namespaces(ns_path)

OnePhotonSeries = get_class('OnePhotonSeries', 'mylab')
visual_stimulus_images = OnePhotonSeries(
    name='stimulus',
    source='NA',
    data=np.random.rand(5,5,5),
    unit='NA',
    format='raw',
    bins=5,
    timestamps=[0.0])
