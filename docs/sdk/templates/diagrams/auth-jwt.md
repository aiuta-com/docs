``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}
    
    USR->>SDK: Start some action
    activate SDK
    SDK->>APP: Request JWT (params)
    APP->>BE: Request new JWT (params)
    BE->>BE: Generate JWT
    Note over BE: Validating the request parameters
    BE-->>APP: Return generated JWT
    APP-->>SDK: Provide JWT
    SDK->>API: Make request
    Note over SDK,API: Authorization: Bearer <token>
    API->>API: Validate JWT

    break JWT is invalid
    rect
        API-->>SDK: Retun 401 Unauthorized
        SDK-->>USR: Show something went wrong
    end
    end

    API-->>SDK: Return response
    SDK-->>USR: Provide UI feedback / result
    deactivate SDK
```
