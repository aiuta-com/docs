The sequence diagram of adding newly uploaded and generated images to the user's history using custom data providers.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    APP->>SDK: Provide configuration with observable data providers
    activate SDK
    SDK-->>SDK: Subscribe to observable<br>history lists changes
    deactivate SDK

    Note over SDK,API: After successful try-on generation
    activate SDK
    SDK->>APP: Call addUploadedImages / addGeneratedImages
    APP->>BE: Link new images<br>to the user's history
    APP-->>SDK: Update observable data providers
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

!!! doc "See details about" 
    
    - <span class="md-sequence-number">2 – 5</span> History images structure in the [Common Models](/sdk/about/developer/common-models/#history-images)
    - [Try-on generation process here](/sdk/about/diagrams/interaction-sequence/#making-try-on)