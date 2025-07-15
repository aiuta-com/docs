Detailed sequence of the user selecting the source image for the virtual try-on.

=== "Upload a photo"

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

        USR->>APP: Tap Try-on Button
        APP->>SDK: Start Try-on (Product)
        activate SDK
        SDK-->>USR: Present SDK UI
        
        USR->>SDK: Select / take a new photo
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

=== "Predefined model / Uploads history"

    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

        USR->>APP: Tap Try-on Button
        APP->>SDK: Start Try-on (Product)
        activate SDK
        SDK-->>USR: Present SDK UI

        USR->>SDK: Select model / previously used photo
        SDK->>SDK: Add/Reorder image in the history
        Note right of SDK: Using the image ID

        SDK->>SDK: Start Try-on (Image)
        deactivate SDK
    ```
