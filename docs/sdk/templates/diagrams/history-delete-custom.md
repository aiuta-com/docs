The sequence diagram of removing images from the user's history using custom data providers.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    USR->>SDK: Select image(s) to delete
    activate SDK
    
    SDK-->>USR: Show activity indicator
    SDK->>APP: Call deleteUploadedImages / deleteGeneratedImages
    activate APP
    APP->>BE: Delete images
    activate BE

    opt user owned images 
        alt Aiuta storage
            BE->>API: Delete images by ID
            activate API
            API-xGS: Delete files
            API-->>BE: Deletion response
            deactivate API
        else your storage
            BE-xGS: Delete files
        end
    end
    BE->>BE: Remove images from the user's records

    BE-->>APP: Acknowledge deletion
    deactivate BE

    APP-->>SDK: Acknowledge deletion
    SDK-->>USR: Hide activity indicator
    APP-->>SDK: Update observable history lists
    deactivate APP
    
    SDK->>SDK: Update history display
    SDK-->>USR: Show updated history
    deactivate SDK
```

!!! warning "Important: Owner Type Handling"
    
    When deleting images from the history, the behavior depends on the `ownerType`
    
    - **`user`** images can be deleted from storage and removed from history
    - **`aiuta`** images should only be unlinked from user history, not deleted from storage
    
    This ensures that shared model images remain available for other users while user-generated content can be properly cleaned up