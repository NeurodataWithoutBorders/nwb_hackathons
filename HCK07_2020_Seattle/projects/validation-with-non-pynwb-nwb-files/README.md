[:rewind: Back to the projects list](../PROJECTS.md)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Validation for non-pynwb NWB files

## Key Investigators

Thomas Braun (byte physics e.K.)

## Project Description

[MIES](https://github.com/AllenInstitute/MIES) is a FLOSS software package for
acquiring, viewing and evaluating intracellular ephys data. It already supports exporting into NWBv1.

Work is nearly done to allow exporting into NWBv2 files as well, see
https://github.com/AllenInstitute/MIES/pull/179 using a new version of [IPNWB](https://github.com/AllenInstitute/IPNWB).

In this project we want to focus on enhancing the pynwb validator for these files.
This is a special case as writing them *not* using h5py introduces subtle
differences.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Finalize MIES NWBv2 support
2. Introduce a standard method for validating non-pynwb NWB files and document that
3. Fix validation bugs

## Results

A first alpha version of the validator finding entities which should not be present
can be found at [1, 2]. During the development one validation issue was
encountered regarding links not being followed, see [3] for the fix. Related
issues were created at [4] and [5].

[1]: https://github.com/NeurodataWithoutBorders/pynwb/pull/1178
[2]: https://github.com/hdmf-dev/hdmf/pull/288
[3]: https://github.com/hdmf-dev/hdmf/pull/286
[4]: https://github.com/hdmf-dev/hdmf/issues/287
[5]: https://github.com/NeurodataWithoutBorders/pynwb/issues/1179
