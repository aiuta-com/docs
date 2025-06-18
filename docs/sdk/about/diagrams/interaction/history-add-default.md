The sequence diagram of adding newly uploaded and generated images to the user's history.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation
    activate SDK
    SDK->>SDK: Add new images<br>to the user's history
    Note right of SDK: Local storage
    SDK->>SDK: Update local history display
    deactivate SDK

    USR->>SDK: Tap History Button / Change photo
    activate SDK
    SDK-->>USR: Display History Data
    Note over SDK,USR: Shows list of generated / uploaded<br>images with most recent first

    opt cache not exitst/expired
        SDK->>GS: Get images by the URL
        GS-->>SDK: Images data
        SDK->>SDK: Cache images
        deactivate SDK
    end
```

!!! doc "See details about [Try-on generation process here](/sdk/about/diagrams/interaction-sequence/#making-try-on)"