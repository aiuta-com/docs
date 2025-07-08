``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}
    
    USR->>SDK: Start some action
    activate SDK
    SDK->>SDK: Add Subscription ID<br>to the request Headers
    SDK->>API: Make request
    Note over SDK,API: x-user-id: <subscription_id>
    API->>API: Match Subscription ID
    API-->>SDK: Return response
    SDK-->>USR: Provide UI feedback / result
    deactivate SDK
```