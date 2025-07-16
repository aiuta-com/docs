---
hide:
  - toc
---
# Complete Interaction Sequences

The detailed sequence diagrams below cover all stages of interaction with the Aiuta SDK. The diagrams help visualize the flow of operations, such as initialization and the try-on process, highlighting the roles of the user, your app, backend services and Aiuta SDK. 

Authentication of requests from the SDK to the Aiuta API/Backend based on the configuration provided is described [here](/sdk/about/diagrams/authentication.md).

## Configuration

{% include-markdown "sdk/templates/diagrams/initialization.md" %}

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

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-custom.md" %}

#### Making Try-On

{% include-markdown "sdk/templates/diagrams/try-on.md" %}

!!! doc "See details about" 
    
    - [<span class="md-sequence-number">2</span> Authenticating secured requests](/sdk/about/diagrams/authentication.md)
    - [<span class="md-sequence-number">9</span> Adding Images to the History](/sdk/about/diagrams/interaction-sequence.md#addingviewing-images-in-the-history)

#### Viewing Results

=== "Default configuration"

    {% include-markdown "sdk/templates/diagrams/results-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/templates/diagrams/results-custom.md" %}
    
    !!! doc "See details about" 
        
        - [<span class="md-sequence-number">6-8</span> Wishlist integration](/sdk/developer/configuration/features/wishlist.md)
        - [<span class="md-sequence-number">11</span> Share functionality](/sdk/developer/configuration/features/share.md) 

### Managing History

The following sequence diagram illustrates the process of managing images history using the Aiuta SDK. It covers the workflow from adding and viewing the history to deleting existing ones. The diagrams are the same for the uploaded and generated history, as the processes are identical and only differ in the UI.

#### Adding/Viewing Images in the History

=== "Default configuration"

    {% include-markdown "sdk/templates/diagrams/history-add-default.md" %}

    !!! doc "See details about [Try-on generation process here](/sdk/about/diagrams/interaction-sequence.md#making-try-on)"

=== "Custom configuration" 

    {% include-markdown "sdk/templates/diagrams/history-add-custom.md" %}

    !!! doc "See details about" 
        
        - <span class="md-sequence-number">2 – 5</span> History images: [input](/sdk/developer/configuration/features/image-picker.md#input-image) and [generated](/sdk/developer/configuration/features/try-on.md#generated-image)
        - [Try-on generation process here](/sdk/about/diagrams/interaction-sequence.md#making-try-on)

#### Deleting Images from the History

=== "Default configuration"

    {% include-markdown "sdk/templates/diagrams/history-delete-default.md" %}

=== "Custom configuration" 

    {% include-markdown "sdk/templates/diagrams/history-delete-custom.md" %}
