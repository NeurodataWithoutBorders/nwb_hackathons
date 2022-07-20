[:rewind: Back to the projects list](../../README.md#ProjectsList)

# webnwb

## Key Investigators

- Garrett Flynn (Brains@Play)

## Project Description
Building on our progress at the [2022 NWB-DANDI Developer Hackathon](https://docs.google.com/document/d/1qGuBUHIRhal0d4DLK3urtj9YU6lTt8CddRkqCF-faQg/edit#heading=h.ngfb92naeue2), refine our JavaScript API for creating and interacting with NWB files directly on the browser.

## Objectives
1. Objective A. Support range requests through the browser's Fetch API rather than the (inaccessible on browser) ROS3 driver.
2. Objective B. Write thorough documentation on usage

## Approach and Plan
### Range Requests
1. Request a valid range from DANDI
2. Load as a Blob
3. Load blob directly into h5wasm. Will it just work?

### Documentation
1. Replicate tutorials from User Days

## Progress and Next Steps
Will update soon.

## Materials
- Source code: https://github.com/brainsatplay/webnwb
- Demos: https://nwb.brainsatplay.com/examples
- Rough Documentation: https://nwb.brainsatplay.com/examples

## Background and References
- Previous hackathon progress: https://docs.google.com/document/d/1qGuBUHIRhal0d4DLK3urtj9YU6lTt8CddRkqCF-faQg/edit#heading=h.ngfb92naeue2
- Relevant issue on supporting range requests: https://github.com/usnistgov/h5wasm/issues/12

