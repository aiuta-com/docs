# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

??? info "Naming Convention"
    Implementation and naming details may vary depending on the specific platform, but the core concepts and overall structure remain consistent across all platforms.
    For example type names, described in the schemes, like: 

    - `Configuration`

        - in Swift it will be `Aiuta.Configuration`
        - in Kotlin and Dart - `AiutaConfiguration`

    - `UserInterface`

        - in Swift it will be `Aiuta.Configuration.UserInterface`
        - in Kotlin and Dart - `AiutaUserInterfaceConfiguration`

    - `Product`

        - in Swift it will be `Aiuta.Product`
        - in Kotlin and Dart - `AiutaProduct`

    and so on - the key part of the name is the same.

    A scheme-based approach in the documentation applies core concepts and structures uniformly, unifying the SDK's understanding and implementation. By following this strategy, we achieve consistency in our SDK's implementations and minimize redundancy in our documentation for each platform. We use this documentation ourselves for development.

!!! tip "Annotations"
    Don't miss them - click :material-information-outline: for more details

!!! doc "Type Definitions"
    
    - [Platform-specific types](platform-types.md)
    - [Common Models schemes](common-models.md)

See also [the diagrams](/sdk/about/diagrams/interaction-sequence/) showing the sequence of configuration application and what it may affect.

## Configuration

```typescript
Configuration {
  auth: Auth // (1)!
  userInterface: UserInterface // (2)!
  features: Features // (3)!
  analytics: Analytics | null // (4)!
  debugSettings: DebugSettings // (5)!
}
```

1.  [:material-arrow-down-left:](#auth) Required to authenticate Aiuta SDK to use [API :octicons-link-external-24:](https://developer.aiuta.com/products/digital-try-on/documentation){:target="_blank"} with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`. 

    Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} Obtaining credentials section for instructions on how to get your credentials.

2. [:material-arrow-down-left:](#user-interface) Configuration of the user interface presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

3. [:material-arrow-down-left:](#features) Describes the set of features enabled in the SDK for the user and thier interaction with the app.

4. [:material-arrow-down-left:](#analytics) Allows to receive analytics events from the SDK and send them to your analytics provider.

5. [:material-arrow-down-left:](#debugsettings) Controls the logging settings and validation policies for various parameters.


### [:material-arrow-up-left:](#configuration) Auth

=== "ApiKey"
    ```typescript
    ApiKeyAuth {
      apiKey: String // (1)!
    }
    ```

    1.  The `apiKey` is used to authenticate all outgoing requests from the Aiuta SDK to the Aiuta API. This key ensures that the requests are linked to your account, allowing the SDK to access the necessary resources and services provided by Aiuta. 
    
        !!! doc "Please see [API documentation obtaining credentials](../../../api/getting-started.md#obtaining-credentials) section for instructions on how to get your `apiKey`"
    
  
=== "Jwt"
    ```typescript
    JwtAuth {
      subscriptionId: String // (1)!
      getJwt: Callback(Map<String: String>) => String // (2)!
    }
    ```

    1.  The `subscriptionId` is used to authenticate requests that do not require secure transmission. It acts as a key to ensure that the requests are properly linked to your subscription and account.

        !!! doc "Please see [API documentation obtaining credentials](../../../api/getting-started.md#obtaining-credentials) section for instructions on how to find your `subscriptionId`"
        
    2.  This method is invoked by the SDK each time a tryOn request necessitates authentication
        through a JSON Web Token. The implementation of this method should securely
        generate the JWT on the server side and subsequently return it to the SDK.

        The SDK will provide a set of key-value pairs that represent the `parameters` of the request
        requiring a JWT. These parameters include identifiers like a `uploaded_image_id` and `product_id` and can be used 
        for associating the JWT with the specific image and product involved in the tryOn request. 
        This ensures that the generated token is tailored specifically to the request being processed, enhancing security and relevance.

        !!! success "Returns"
            Non-empty string representing the generated JWT

        !!! failure "Throws"
            An error if the JWT cannot be generated. 
            
            If an error is thrown, the SDK will be unable to complete the tryOn request and will display an error message to the user

        !!! doc "See [JWT server-side auth example](../../../api/server-side-auth-component.md) for more details on securely generating JWTs."



<!-- User Interface -->
{% include-markdown "sdk/about/developer/user-interface.md" %}



<!-- Feature -->
{% include-markdown "sdk/about/developer/features.md" %}



### [:material-arrow-up-left:](#configuration) Analytics
```typescript
Analytics {
  handler: {
    onAnalyticsEvent: Callback(Event) // (1)!
  }
}
```

1.  Callback function that processes analytics events generated by the SDK, allowing integration with external analytics services or custom event handling.

    !!! note ""
        [:octicons-arrow-right-24: All events are listed in the analytics section](../../about/analytics/analytics.md)



### [:material-arrow-up-left:](#configuration) DebugSettings
```typescript
DebugSettings {
  isLoggingEnabled: Bool // (1)!
  emptyStringsPolicy: ValidationPolicy // (2)!
  unavailableResourcesPolicy: ValidationPolicy // (3)!
  infoPlistDescriptionsPolicy: ValidationPolicy // (4)!
  listSizePolicy: ValidationPolicy // (5)!
}

enum ValidationPolicy {
  ignore // (6)!
  warning // (7)!
  fatal // (8)!
}
```

1.  Controls whether the SDK should log debug information, providing detailed logs to help developers understand its behavior.
2.  Validation policy for checking whether required strings in the SDK configuration are not empty, preventing runtime issues.
3.  Validation policy for checking whether required resources are available and properly configured.
4.  Validation policy for checking whether the `info.plist` file contains all required descriptions for enabled features.
5.  Validation policy for checking whether lists required by the SDK are of the correct size.
6.  Ignores all validation errors, allowing the SDK to proceed without taking any action.
7.  Logs validation errors to the console for debugging purposes without interrupting execution.
8.  Stops the application's execution with a fatal error when validation errors occur.
