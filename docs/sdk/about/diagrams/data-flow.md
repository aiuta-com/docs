---
hide:
  - toc
---
# Data flow

Overview sequence diagram covers the handling of user data. It shows a simplified process from obtaining user consent to uploading and displaying images, highlighting the roles of the user, your app, backend services, Aiuta SDK and API. You can view also [the complete interaction sequence](/sdk/about/diagrams/interaction-sequence/) diagrams.

!!! info "Anonymous photos" 
    We do not process any user data other than photos, do not request your user IDs, and all uploaded images remain anonymous to us

```mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    note over GS: Aiuta or Yours

    opt consent feature
        USR->>SDK: Accept Terms Of Use
        activate SDK
        note over SDK,APP: May contain any additional consents<br>provided by Your app to request from the user
        SDK->>APP: Provide user's consent
        APP->>BE: Store user's consent
    end

    USR->>SDK: Provide an image
    SDK->>API: Upload an image

    activate API
    API->>GS: Store input and<br>generated images
    API->>API: ⠀
    Note over API: Generate images ID, form URL that<br>may contains temporary access token
    API-->>SDK: Return the ID and<br>URL of images
    deactivate API

    SDK->>APP: Provide the ID and URL of images
    note over APP: May link this images to the user's identity for the<br>further use in accordance with the user's consent
    SDK-->>USR: Display generated images
    deactivate SDK
```

!!! info "Access tokens"
    Depending on the storage type and access levels set, the URL in the Aiuta API response <span class="md-sequence-number">8</span> may contain a temporary access token so that the SDK has time to download the results and <span class="md-sequence-number">10</span> show them to the user before access to that URL is expired. For further use <span class="md-sequence-number">9</span> under the control of your app and to provide historical data for display in the SDK when using data providers ([uploaded](/sdk/about/developer/configuration/#uploads-history) and [generated](/sdk/about/developer/configuration/#generations-history)), your application must ensure access by refreshing the tokens in the URL.
