---
hide:
  - toc
---
# Diagrams

This page provides sequence diagrams illustrating the interactions between your application and Aiuta. The diagrams help visualize the flow of operations, such as initialization and the try-on process, highlighting the roles of the user, your app, backend services, Aiuta SDK and API.

## Complete interaction sequences

##### Initialization

``` mermaid
sequenceDiagram
    autonumber
    actor User
    participant APP as Your App
    participant BE as Your BE
    participant SDK as Aiuta SDK
    participant API as Aiuta API

    User->>APP: Launch the App
    APP->>SDK: Initialize with Configuration

    activate SDK
    Note over APP,SDK: Includes auth, UI, features, analytics
    SDK->>API: Request internal configuration
    API-->>SDK: Internal configuration
    opt predefined models enabled
        SDK->>API: Request predefined models
        API-->>SDK: Predefined models
    end
    deactivate SDK

    APP->>BE: Load products
    BE-->>APP: Products
    Note over APP,BE: Including a flag whether<br>a virtual try-on is available

    APP-->>User: Show products
    Note over APP,User: Including a try-on button for<br>products with try-on feature
```

##### Try-On

=== "Default configuration"
    
    !!! note ""
        :octicons-dot-16: BuiltIn data providers :octicons-dot-16: Default features set :octicons-dot-16: Embedded legal info
    
    ``` mermaid
    sequenceDiagram
        autonumber
        actor User
        participant APP as Your App
        participant BE as Your BE
        participant SDK as Aiuta SDK
        participant API as Aiuta API

        User->>APP: Tap Try-on Button
        APP->>SDK: Call `startTryon`(Product)
        activate SDK
        SDK-->>User: Presents SDK UI

        %% User Photo
        User->>SDK: Select a photo
        SDK->>API: Upload a photo
        API->>API: Save a photo to<br>internal storage
        Note over API: Anonymous<br>the photo is associated with the<br>app entry, not the user entry
        
        deactivate SDK
    ```


!!! doc "Find more about"
    
    - Aiuta [Configuration](/sdk/about/developer/configuration/) 
    - [Common Models](/sdk/about/developer/common-models/)
