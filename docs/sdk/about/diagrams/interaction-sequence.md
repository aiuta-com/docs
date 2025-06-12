---
hide:
  - toc
---
# Complete interaction sequences

The detailed sequence diagrams below cover all stages of interaction with the Aiuta SDK. The diagrams help visualize the flow of operations, such as initialization and the try-on process, highlighting the roles of the user, your app, backend services, Aiuta SDK and API. Authentication of requests from the SDK to the Aiuta API/Backend based on the configuration provided is described [here](/sdk/about/diagrams/authentication/).

## Initialization

The next diagram illustrates the initialization process from launching the app to displaying products, including configuration and model requests.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    USR->>APP: Launch the App
    APP->>SDK: Initialize with Configuration

    activate SDK
    Note over APP,SDK: Includes auth, UI, features, analytics
    SDK->>API: Request internal configuration
    API-->>SDK: Internal configuration
    opt predefined models feature
        SDK->>API: Request predefined models
        API-->>SDK: Predefined models collection
    end
    deactivate SDK

    APP->>BE: Load products
    BE-->>APP: Products
    Note over APP,BE: Including a flag whether<br>a virtual try-on is available

    APP-->>USR: Show products
    Note over APP,USR: Including a try-on button for<br>products with try-on feature
```

!!! doc "Find more about Aiuta [Configuration](/sdk/about/developer/configuration/) in <span class="md-sequence-number">2</span>"

    Please note in <span class="md-sequence-number">8 – 9</span> that you should obtain information about the availability of the virtual try-on feature for each of your products from __your__ backend, as the SDK does not receive information about product availability and will attempt to launch a virtual try-on with any product you provide, which may result in an error if that product has not been trained by Aiuta.

## Try-On

Sequence diagram of the virtual try-on.

=== "Default configuration"
        
    !!! note ""
        :octicons-dot-fill-16: BuiltIn data providers :octicons-dot-fill-16: Default features set :octicons-dot-fill-16: Embedded legal info

    ### Pick a photo

    Detailed sequence of the user selecting the source image for the virtual try-on.

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

        USR->>APP: Tap Try-on Button
        APP->>SDK: Start Try-on (Product)
        activate SDK
        SDK-->>USR: Present SDK UI
        
        alt New user photo
            USR->>SDK: Select/take a new photo
            SDK->>API: Upload a photo
            activate API
            API->>GS: Save input image
            Note over API,GS: Anonymous.<br>The photo is associated with the<br>app entry, not the user entry
            API->>API: Generate image ID, form URL
            API-->>SDK: Return image ID, URL
            deactivate API
            SDK->>SDK: Add image to the history
        else Predefined model / Uploads history
            USR->>SDK: Select model / previously used photo
            SDK->>SDK: Add/Reorder image in the history
            Note over SDK: Using the image ID
        end
    ```

    !!! doc "Details to store <span class="md-sequence-number">5-6, 8</span> History Images described in the [Common Models](/sdk/about/developer/common-models/#history-images)"

    ### Making Try-On

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

        USR->>SDK: Start Try-on (Image)
        Note over USR,SDK: Automatically after picking a new photo or by the<br>explicit button tap when last used photo is available

        activate SDK
        SDK->>API: Create operation<br>(image ID, product ID)
        activate API
        Note over SDK,API: Secure authenticated request
        API-->>SDK: Operation ID

        loop internal configuration delay
            SDK->>API: Request operaion status
            API-->>SDK: Operation details
            Note over API,SDK: status, error | generated images
            SDK-->>SDK: Check operation status
            Note over SDK: Repeat while IN_PROGRESS

        end
            critical Check operation status

            option SUCCESS
                API->>GS: Save generated image
                deactivate API
                Note over API,GS: Anonymous.<br>The photo is associated with the<br>app entry, not the user entry

                SDK->>SDK: Add generation<br>result to the history
                SDK->>GS: Get result image by the URL
                GS-->>SDK: Image data
                SDK-->>USR: Present results

            option FAILED
                SDK-->>USR: Show something whent wrong error

            option ABORTED
                SDK-->>USR: Report couldn't detect anyone
                deactivate SDK
                Note over SDK,USR: User may select other photo and start over
                
            end
    ```

    !!! doc "Details about <span class="md-sequence-number">2</span> Product and <span class="md-sequence-number">4, 12</span> Images described in the [Common Models](/sdk/about/developer/common-models/)"
        See diagrams of [<span class="md-sequence-number">4</span> piking a photo](#pick-a-photo) and [<span class="md-sequence-number">5</span> authenticating secured requests](#authenticate-request) below

=== "Custom configuration"
        
    !!! note ""
        :octicons-dot-fill-16: Custom data providers :octicons-dot-fill-16: All features including wishlist :octicons-dot-fill-16: Standalone consent when upload a photo


