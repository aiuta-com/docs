``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}
    
    USR->>SDK: Start some action
    activate SDK
    SDK->>SDK: Add Api Key<br>to the request Headers
    SDK->>API: Make request
    Note over SDK,API: x-api-key: <api_key>
    API->>API: Check Api Key
    API-->>SDK: Return response
    SDK-->>USR: Provide UI feedback / result
    deactivate SDK
```