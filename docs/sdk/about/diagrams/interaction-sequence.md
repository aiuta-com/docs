---
hide:
  - toc
---
# Complete Interaction Sequences

The detailed sequence diagrams below cover all stages of interaction with the Aiuta SDK. The diagrams help visualize the flow of operations, such as initialization and the try-on process, highlighting the roles of the user, your app, backend services and Aiuta SDK. 

Authentication of requests from the SDK to the Aiuta API/Backend based on the configuration provided is described [here](/sdk/about/diagrams/authentication/).

## Configuration

{% include-markdown "sdk/about/diagrams/interaction/initialization.md" %}

## Usage

!!! tip "Configuration examples"
    You can switch the example configuration presets for the diagrams below to see the differences when using built-in or custom data providers, as well as some differences when using additional functionality.

    === "Default configuration"

        - BuiltIn data providers 
        - Default features set 
        - Embedded legal info

    === "Custom configuration"

        - Custom data providers 
        - All features including wishlist 
        - Standalone consent when upload a photo

### Try-On

The following sequence diagrams illustrate the process of a virtual try-on using the Aiuta SDK. They cover the entire workflow from the moment a user initiates a try-on request to the final rendering of the virtual try-on result, highlighting key actions such as image selection, authentication, and data processing.

#### Pick a Photo

=== "Default configuration"

    {% include-markdown "sdk/about/diagrams/interaction/pick-a-photo-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/about/diagrams/interaction/pick-a-photo-custom.md" %}

#### Making Try-On

{% include-markdown "sdk/about/diagrams/interaction/try-on.md" %}

#### Viewing Results

=== "Default configuration"

    {% include-markdown "sdk/about/diagrams/interaction/results-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/about/diagrams/interaction/results-custom.md" %}

### Managing History

The following sequence diagram illustrates the process of managing images history using the Aiuta SDK. It covers the workflow from adding and viewing the history to deleting existing ones. The diagrams are the same for the uploaded and generated history, as the processes are identical and only differ in the UI.

#### Adding/Viewing Images in the History

=== "Default configuration"

    {% include-markdown "sdk/about/diagrams/interaction/history-add-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/about/diagrams/interaction/history-add-custom.md" %}

#### Deleting Images from the History

=== "Default configuration"

    {% include-markdown "sdk/about/diagrams/interaction/history-delete-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/about/diagrams/interaction/history-delete-custom.md" %}
