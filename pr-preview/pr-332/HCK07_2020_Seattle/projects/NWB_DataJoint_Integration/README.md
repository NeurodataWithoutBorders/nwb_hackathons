[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB-DataJoint Integration

## Key Investigators

Eric Denovellis (HHMI, UCSF, Loren Frank Laboratory)

## Project Description

Once data is in a common format, there are a common set of “preprocessing” operations that all laboratories perform. These include spike-sorting, filtering and downsampling of continuous signals to extract local field potentials (LFPs), and basic video processing.

Our goal here is to build a common pipeline for these operations using DataJoint operating on the NWB-raw file, and to save the results in a new NWB:N file (NWB-preprocessed). This approach ensures that the preprocessed data can be shared.

As part of this process the Frank laboratory has already begun to work with both the NWB:N developers and DataJoint to allow for loading and saving of NWB:N objects within DataJoint. Another goal is the ability to scale up to large cohorts of animals without requiring an overwhelming amount of repetitive analysis tasks from lab personnel. With large cohort studies, it is critical to automate such tasks. The goal is to automate, as much as possible, spike sorting, behavioral annotation from video, and other early processing of the raw data.

## Objectives

1. Write minimum viable code for pulling in basic metadata from our new NWB-raw files to DataJoint.
2. Write minimum viable code for pulling in the electrode table.
3. Write minimum viable code for accessing the electrical potentials for probe data.


## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->


## Sample *dj_local_conf.json*:
```json*
{
    "database.host": "host",
	"database.user": "user",
	"database.password": "pass",
    "database.port": 3306,
    "connection.init_function": null,
    "database.reconnect": false,
    "loglevel": "INFO",
    "safemode": true,
    "display.limit": 7,
    "display.width": 14,
    "display.show_tuple_count": true,
    "enable_python_native_blobs": true,
    "custom": {
        "database.prefix": "demo_",
        "intracellular_directory": "F:/Guo-Inagaki-2017/data/whole_cell_nwb2.0"
    },
    "stores": {
        "nwb_store": {
            "protocol": "file",
            "location": "C:/DataJoint/Integrated_NWB_adaptive_attributes/nwb_store",
            "stage": "C:/DataJoint/Integrated_NWB_adaptive_attributes/nwb_store"
        }
    }
}
```