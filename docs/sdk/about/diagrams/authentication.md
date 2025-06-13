---
hide:
  - toc
---
# Request Authentication

Authentication sequences for requests made by the SDK to the Aiuta API. Authentication is mandatory for some calls, such as starting image generation, and optional for other trivial calls, such as checking the status of an operation.

!!! info "Preferred authentication"
    Using JSON Web Tokens (JWT) is the most flexible and secure way to access the Aiuta services, while the ApiKey authentication method is best used only for server-side integration. But it's up to you. 
    
    :material-book-open-variant:{ .lg } Read more about [API Authentication](/api/getting-started/#authentication)

=== "`JwtAuth` • `getJwt`"
    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/about/common-sd-participants.md" %}
        
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

    !!! doc "See [the JwtAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_2) in the SDK"

=== "`JwtAuth` • `subscriptionId`"
    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/about/common-sd-participants.md" %}
        
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

    !!! doc "See [the JwtAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_2) in the SDK"

=== "`ApiKeyAuth`"
    ``` mermaid
    sequenceDiagram
        {% include-markdown "sdk/templates/about/common-sd-participants.md" %}
        
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

    !!! doc "See [the ApiKeyAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_1) in the SDK"
