---
hide:
  - toc
---
# Request Authentication

Authentication is mandatory for some calls, such as starting image generation, and optional for other trivial calls, such as checking the status of an operation. Based on [the configuration provided](/sdk/about/developer/configuration/#configuration), the SDK will select the request authentication scheme according to the following table

| Auth | Mandatory | Optional |
| ---- | --- | ------ |
| __JwtAuth__ | `JWT` | `subscriptionId` |
| __ApiKeyAuth__ | `apiKey` | `apiKey` |

!!! info "Preferred authentication type"
    Using JSON Web Tokens (JWT) is the most flexible and secure way to access the Aiuta services, while the ApiKey authentication method is best used only for server-side integration. But it's up to you. 
    
    :material-book-open-variant:{ .lg } Read more about [API Authentication](/api/getting-started/#authentication)


Here are all authentication sequence options for requests sent by the SDK to the Aiuta API.

=== "`JwtAuth` • `JWT`"
    {% include-markdown "sdk/templates/diagrams/auth-jwt.md" %}

    !!! doc "See also" 

        - [the JwtAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_2) in the SDK
        - [JWT server-side auth example](/api/server-side-auth-component/) for more details on securely generating JWTs

=== "`JwtAuth` • `subscriptionId`"
    {% include-markdown "sdk/templates/diagrams/auth-subscription-id.md" %}

    !!! doc "See also"
        - [the JwtAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_2) in the SDK 
        - [API documentation obtaining credentials](/api/getting-started/#obtaining-credentials) section for instructions on how to find your `subscriptionId`


=== "`ApiKeyAuth` • `apiKey`"
    {% include-markdown "sdk/templates/diagrams/auth-api-key.md" %}

    !!! doc "See also"
    
        - [the ApiKeyAuth configuration scheme](/sdk/about/developer/configuration/#__tabbed_1_1) in the SDK
        - [API documentation obtaining credentials](/api/getting-started/#obtaining-credentials) section for instructions on how to get your `apiKey`
