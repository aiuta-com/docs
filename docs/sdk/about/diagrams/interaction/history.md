The following sequence diagram illustrates the process of managing generated try-on images history using the Aiuta SDK. It covers the workflow from viewing the history to adding new generated images and deleting existing ones, highlighting the interaction between the user, SDK, and your app's data management system.

!!! note ""
    :octicons-dot-fill-16: BuiltIn data providers :octicons-dot-fill-16: Default features set :octicons-dot-fill-16: Embedded legal info

## Viewing Generation History

Detailed sequence of accessing and displaying the user's previously generated try-on images.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    USR->>SDK: Tap History Button
    activate SDK
    SDK->>APP: Request generatedImages (Observable)
    activate APP
    APP-->>SDK: Return List<GeneratedImage>
    Note over APP,SDK: Each GeneratedImage contains:<br>id, url, ownerType, productIds
    deactivate APP
    SDK-->>USR: Display Generation History Page
    Note over SDK,USR: Shows list of generated images<br>with most recent first
    deactivate SDK
```

!!! doc "Details about <span class="md-sequence-number">3-4</span> GeneratedImage structure described in the [Common Models](/sdk/about/developer/common-models/#generated-image)"

## Adding Generated Images to History

The sequence diagram of adding newly generated try-on results to the user's history.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation
    SDK->>SDK: Receive generated images from API
    Note over SDK: Generated images with SUCCESS status
    SDK->>APP: Call addGeneratedImages (List<GeneratedImage>)
    activate APP
    Note over APP: Store generated images in local storage<br>or sync with backend
    APP-->>SDK: Acknowledge addition
    deactivate APP
    SDK->>SDK: Update local history display
    Note over SDK: Add new images to the top of history
```

!!! doc "See details about" 
    
    - <span class="md-sequence-number">2</span> Generated images structure in the [Common Models](/sdk/about/developer/common-models/#generated-image)
    - [<span class="md-sequence-number">1</span> Try-on generation process here](#making-try-on)

## Deleting Generated Images from History

The sequence diagram of removing generated try-on images from the user's history.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    USR->>SDK: Select image to delete
    SDK->>SDK: Show delete confirmation
    USR->>SDK: Confirm deletion
    activate SDK
    
    SDK->>APP: Call deleteGeneratedImages (List<GeneratedImage>)
    activate APP
    
    alt user owned images
        APP->>API: Delete generated image (image ID)
        activate API
        API-->>APP: Success response
        deactivate API
        Note over APP,API: Only user-owned images can be deleted<br>from storage
    else aiuta owned images
        Note over APP: Only unlink from user history<br>Do not delete from storage
    end
    
    APP->>APP: Remove from local storage/history
    APP-->>SDK: Acknowledge deletion
    deactivate APP
    
    SDK->>SDK: Update history display
    Note over SDK: Remove deleted images from list
    SDK-->>USR: Show updated history
    deactivate SDK
```

!!! doc "See details about" 
    
    - <span class="md-sequence-number">6-7</span> Owner type handling in the [Common Models](/sdk/about/developer/common-models/#owner-type)
    - [<span class="md-sequence-number">8</span> API deletion endpoint here](/api/try-on/reference/#/default/delete_generated_image_generated_images__image_id__delete)

!!! warning "Important: Owner Type Handling"
    
    When deleting images from generation history, the behavior depends on the `ownerType`:
    
    - **`user`** images: Can be deleted from storage and removed from history
    - **`aiuta`** images: Should only be unlinked from user history, not deleted from storage
    
    This ensures that shared model images remain available for other users while user-generated content can be properly cleaned up. 