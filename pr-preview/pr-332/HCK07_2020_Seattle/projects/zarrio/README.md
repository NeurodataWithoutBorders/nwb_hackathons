[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Integrate Zarr I/O with HDMF and PyNWB

## Key Investigators

* Oliver Ruebel (LBNL)
* Andrew Tritt (LBNL)

## Project Description

Integrate Zarr as alternative (python-only) backend for HDMF and PyNWB

## Objectives

* Finalize integration of Zarr I/O backend with HDMF and PyNWB

## Approach and Plan

* Update the Zarr-related PRs to the most recent versions of PyNWB and HDMF
* Implement helper functions for converting between different backends and remove code in the Zarr backend related to checking for read from other backends
* Implement support for Dimensions Scales in the Zarr backend

## Progress and Next Steps

* A fairly basic experiment/benchmark is [here](https://gist.github.com/arokem/bf2d5f335b4c4a390907b0c7907600ac)

## Materials

* https://github.com/hdmf-dev/hdmf/pull/98
* https://github.com/NeurodataWithoutBorders/pynwb/pull/1018

## Example

### Installing the current draft backend

```
conda create -n zarr4nwb python=3.6
conda activate zarr4nwb
pip install zarr
git clone https://github.com/NeurodataWithoutBorders/pynwb.git
cd pynwb/
git checkout add/zarrio
python setup.py develop
git clone https://github.com/kangdh/hdmf.git
cd hdmf/
git checkout 1.0.3-zarr
python setup.py develop
```

### Convert test Allen ICEphys file

```
from pynwb import NWBHDF5IO, NWBZarrIO
import os
infile = "H19.28.012.11.05-2.nwb"
outfile = "test_zarr_" + os.path.basename(infile)
h5r = NWBHDF5IO(infile , 'r', load_namespaces=False)
f = h5r.read()
zw = NWBZarrIO(outfile,
               mode='w',
               manager=h5r.manager,
               chunking=True)
zw.write(f, cache_spec=True)
zw.close()
h5r.close()
zr = NWBZarrIO(outfile, 'r')
zf = zr.read()
```

To create a test file: 1) copy the above code to a python file, 2) download the Allen pre-release file, and run the script, e.g.:

```
curl -O http://download.alleninstitute.org/informatics-archive/prerelease/H19.28.012.11.05-2.nwb
python convert_to_zarr.py
ls test_zarr_H19.28.012.11.05-2.nwb/
```

With chunking enabled this should result in:

```
find test_zarr_H19.28.012.11.05-2.nwb | wc -l
>>>    3168
du -hs test_zarr_H19.28.012.11.05-2.nwb/
>>>    166M
```


## Background and References

* ...

