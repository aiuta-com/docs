Detailed sequence of the user selecting the source image for the virtual try-on with custom configuration.

=== "Upload a photo"

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

        USR->>APP: Tap Try-on Button
        APP->>SDK: Start Try-on (Product)
        activate SDK
        SDK-->>USR: Present SDK UI

        USR->>SDK: Tap upload a photo
        SDK->>SDK: Check consent obtained
        opt consent required
            SDK-->>USR: Present consent page
            USR->>SDK: Accept consent terms
            SDK->>APP: Call obtainConsentIds (consent IDs)
            APP->>BE: Store consents obtained
        end
        
        SDK-->>USR: Show options for uploading
        USR->>SDK: Select/take a new photo
        SDK->>API: Upload a photo
        activate API
        API->>GS: Save input image
        Note over API,GS: Anonymous.<br>The photo is associated with the<br>app entry, not the user entry
        API->>API: Generate image ID, form URL
        API-->>SDK: Return image ID, URL
        deactivate API

        SDK->>SDK: Start Try-on (Image)
        deactivate SDK
    ```

    !!! doc "See [custom <span class="md-sequence-number">6 – 8</span> Consent configuration](/sdk/developer/configuration/features/consent.md)" 

=== "Predefined model / Uploads history"

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

        USR->>APP: Tap Try-on Button
        APP->>SDK: Start Try-on (Product)
        activate SDK
        SDK-->>USR: Present SDK UI
        
        USR->>SDK: Select model / previously used photo
        SDK->>APP: Add/Select image in the history
        APP->>BE: Update uploads history
        Note over APP,BE: Recent image first in the list
        APP-->>SDK: Update data provider observable list

        SDK->>SDK: Start Try-on (Image)
        deactivate SDK
    ```