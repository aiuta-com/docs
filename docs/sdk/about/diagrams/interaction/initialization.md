Initialization process from launching the app to displaying products, including SDK configuration.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    USR->>APP: Launch the App
    par
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
    and
        APP->>BE: Load products
        BE-->>APP: Products
        Note over APP,BE: Including a flag whether<br>a virtual try-on is available
        APP-->>USR: Show products
        Note over APP,USR: Including a try-on button for<br>products with try-on feature
    end
```

!!! doc "Find more about [<span class="md-sequence-number">2</span> Aiuta Configuration here](/sdk/about/developer/configuration/)"

    Please note in <span class="md-sequence-number">8 – 9</span> that you should obtain information about the availability of the virtual try-on feature for each of your products from __your__ backend, as the SDK does not receive information about product availability and will attempt to launch a virtual try-on with any product you provide, which may result in an error if that product has not been trained by Aiuta.
