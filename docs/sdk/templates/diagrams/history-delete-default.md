The sequence diagram of removing images from the user's history.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    USR->>SDK: Select image(s) to delete
    activate SDK
    SDK-->>SDK: Delete records from the history
    Note right of SDK: Local storage
    SDK-->>USR: Show updated history
    deactivate SDK
```
