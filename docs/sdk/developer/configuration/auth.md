---
hide:
  - toc
---
# Auth Schemes

Auth is used to authenticate requests from Aiuta SDK to [API](/api/try-on/workflow) with your credentials.

!!! info ""
    Using JSON Web Tokens (JWT) is the most flexible and secure way to access Aiuta services, while the ApiKey authentication method is best used for server-side integration. But it's up to you. :material-book-open-variant: Read more about [API Authentication](/api/getting-started/#authentication).

## [:material-arrow-up-left:](/sdk/developer/configuration/#configuration) Auth

=== "Jwt"
    ```typescript
    JwtAuth {
      subscriptionId: String // (1)!
      getJwt: Callback(Map<String: String>) => String // (2)!
    }
    ```

    1. Should be provided for the SDK to make unsecured requests related to your account.

        !!! doc "Please see [Obtaining credentials](/api/getting-started/#obtaining-credentials) for instructions on how to get your `subscriptionId`"

    2. The implementation of this method should securely generate the JWT [on the server side](/api/server-side-auth-component/) and subsequently return it to the SDK.

        !!! success "Returns"
            Non-empty string representing the generated JWT

        !!! failure "Throws"
            An error if the JWT cannot be generated. 
            
            If an error is thrown, the SDK will be unable to complete the tryOn request and will display an error message to the user

    ## Details

    !!! doc "Please see"

        - [Obtaining credentials](/api/getting-started/#obtaining-credentials)
        - [Implementing the backend component](/api/server-side-auth-component/)

    === "`getJwt`"

        This method is invoked by the SDK each time a tryOn request necessitates authentication
        through a JSON Web Token. 

        !!! info ""
            The SDK will provide a set of key-value pairs that represent the `parameters` of the request
            requiring a JWT. These parameters include identifiers like a `uploaded_image_id` and `product_id` and can be used 
            for associating the JWT with the specific image and product involved in the tryOn request. 
            This ensures that the generated token is tailored specifically to the request being processed, enhancing security and relevance.

        ### Sequence diagram

        {% include-markdown "sdk/templates/diagrams/auth-jwt.md" %}

    === "`subscriptionId`"
        The `subscriptionId` is used to authenticate requests that do not require secure transmission. It acts as a key to ensure that the requests are properly linked to your subscription and account.

        ### Sequence diagram

        {% include-markdown "sdk/templates/diagrams/auth-subscription-id.md" %}

=== "ApiKey"
    ```typescript
    ApiKeyAuth {
      apiKey: String
    }
    ```

    ## Details

    !!! doc "Please see [API documentation](/api/getting-started/#obtaining-credentials) Obtaining credentials section for instructions on how to get your `apiKey`"

    The `apiKey` is used to authenticate all outgoing requests from the Aiuta SDK to the Aiuta API. This key ensures that the requests are linked to your account, allowing the SDK to access the necessary resources and services provided by Aiuta. 

    ### Sequence diagram
    
    {% include-markdown "sdk/templates/diagrams/auth-api-key.md" %}
