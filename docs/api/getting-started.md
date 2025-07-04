# Getting Started

## Creating an Account
To create an account, start by selecting either the [`Sign Up` or `Login` :octicons-link-external-24:](https://developer.aiuta.com/products/digital-try-on/documentation){:target="_blank"} option from the top header . A pop-up window will appear with tabbed options, allowing you to either log in with an existing account or sign up for a new one. If you choose the "Sign Up" link, the pop-up will automatically display the corresponding tab.

To complete the sign-up process, simply follow the on-screen instructions, and your account will be ready in no time. 

!!! info "Verify your email address"
    After registering, you will receive an email prompting you to verify your email address.

## Obtaining credentials

=== "Just registered"

    To obtain credentials for accessing an API product, you must first subscribe to at least one of [its plans :octicons-link-external-24:](https://developer.aiuta.com/products/digital-try-on/plans){:target="_blank"}. Subscribing to a plan is straightforward: simply select the desired product and click "Subscribe," following the prompts on the page.

    After subscribing to the API product of your choice, you will be able to obtain your credentials from the subscription details. Upon completing the subscription process, you will be immediately redirected to a page displaying all the necessary details of the product, including the required credentials.

=== "Already subscribed"
    
    To retrieve the credentials for a product you have previously subscribed to, navigate to the [`My Subscriptions` :octicons-link-external-24:](https://developer.aiuta.com/subscriptions){:target="_blank"} section at the top of the page, and select the product for which you want to view the key.

## Authentication

Authentication is mandatory for some calls such as starting the image generation and is optional for the others trivial calls such as checking the status of the operation. 

!!! info "Optional authentication"
    You may use `x-user-id` header instead of authentication header with a secret value for the trivial calls. The value of `x-user-id` header should be your subscription ID (such as `66ec1726e728c1405e5ebca2`). You can find the subscription ID in the URL of a subscription you have.

=== "Using API key"
    
    The API key authentication method is used for server-side integrations with the Aiuta API. It involves a static key that must be included in each API request within the `X-API-Key` HTTP header.

=== "Using JWT"
    Using JSON Web Tokens (JWT) is the most flexible and secure way to access the Aiuta API. Once you have the secret, the tokens can be issued by your backend and then verified by Aiuta to ensure that the request originated from your application and to check the integrity of the request.
    
    Also you manage the expiration time of the tokens you generate by setting `exp` claim. Setting the expiration time will prevent misuse of compromised tokens.
    
    The flow is as follows:
    
    - The client requests a token from your backend service using your internal client-server communication. The client can provide an arbitrary set of arguments to be included in the payload to be signed.
    - Your application backend validates the parameters provided by the client (e.g., input image to generate, SKU ID, etc.) and issues a JWT using the private key configured during the [Obtaining credentials](#obtaining-credentials) step. All parameters significant to security and cost efficiency should be included in the JWT payload. You can also control the token’s expiration time.
    - The JWT can then be used by your application client to access the Aiuta API until it expires.

    !!! doc "Refer to the documentation for detailed instructions on [implementing the backend component](./server-side-auth-component.md)"
        As an example, see the sequence diagram showing how [Aiuta SDK uses the JWT flow](/sdk/about/diagrams/authentication/#__tabbed_1_1) to authenticate requests

    To make requests to the Aiuta API, use the Bearer Authentication HTTP scheme with the issued token:
    ```
    Authorization: Bearer <token>
    ```

## Making an API Request
<div class="grid cards" markdown>

- :material-book-open-variant:{ .lg } [Try out requests in the API reference](/api/try-on/reference/)

</div>
