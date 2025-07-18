# Getting started with Aiuta

To start using Aiuta SDK, you need to create an instance of the `Aiuta` class. This class serves as the main entry point to the SDK and requires configuration of essential components.

## Installation

Install it along with one of the options that suits you:

<div class="grid cards" markdown>

-   [:material-window-open: __Try-On with UI__](/sdk/android/tryon-ui/installation.md)

    ---

    Quickly implement try-on functionality with minimal custom code while maintaining a consistent look and feel with other Aiuta features.

-   [:material-code-tags: __Try-On__](/sdk/android/tryon/installation.md)

    ---

    Direct access to try-on generation capabilities without any pre-built UI components, allowing you to build custom experiences.

</div>

Next set up the Aiuta class:

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.aiuta

val aiuta: Aiuta = aiuta {
    // Configure authentication strategy
    authenticationStrategy = ... // (1)!
    
    // Configure platform context
    platformContext = ... // (2)!
    
    // Configure logger (optional)
    logger = ... // (3)!
}
```

1. __Required__:  Defines how the SDK authenticates with the Aiuta backend.  
See [Authentication section](#authentication) for details.
2. __Required__: Provides platform-specific information and context.  
See [Platform context section](#platform-context) for details.
3. Optional: Customizes logging behavior of the SDK.
See [Logger section](#logger) for details.


## Authentication

The authentication strategy is a required component that defines how the SDK authenticates with the Aiuta backend. 

To configure authentication, you need to provide an implementation of the authentication strategy. The SDK provides several built-in strategies:

=== "API Key"

    ```kotlin
    authenticationStrategy = ApiKeyAuthenticationStrategy(
        apiKey = "your-api-key",
    )
    ```

=== "JWT"

    ```kotlin
    authenticationStrategy = JWTAuthenticationStrategy(
        getJWT = { /* Provide new JWT token */ },
        subscriptionId = "your-subscription-id"
    )
    ```

!!! info "General configuration"

    You can find a more detailed description of API keys and JWT authentication in the SDK, as well as instructions on how to obtain them, in the [general configuration guide for developers](/sdk/developer/configuration/auth.md)


## Platform Context

The platform context is a required component that provides platform-specific information and context to the SDK. For Android, you need to provide the Android Context, while for other platforms, a general singleton default context is used.

=== "Android"

    ```kotlin
    import android.content.Context

    platformContext = applicationContext
    ```

=== "Other Platforms"

    ```kotlin
    platformContext = AiutaPlatformContext.INSTANCE
    ```

??? tip "Compose helpers"

    For better usage Aiuta with Jetpack Compose SDK contains `LocalAiutaPlatformContext` composition local. For Android, it will be alias for `LocalContext`, for all others platform - static composition local with platform context. 
    
    Pay attention, `LocalAiutaPlatformContext` is part of `fashionsdk-compose-core` artifact


## Logger

The logger is an optional component that allows you to customize the logging behavior of the SDK. By default, the SDK will not use any loggers, but you can provide your own implementation to integrate with your application's logging system.

!!! danger "Usage of default logger"

    Be careful with using default logger with production build - under the hood it's use simple log to console, therefore some sensetive inforamtion can be leak to console. Don't forget to turn it off on production build!

=== "Default Logger"

    ```kotlin
    logger = DefaultAiutaLogger() 
    ```

=== "Custom Logger"

    ```kotlin
    class CustomAiutaLogger : AiutaLogger {
        override fun log(
            priority: AiutaLogger.Level,
            tag: String?,
            throwable: Throwable?,
            message: String,
        ) {
            // Log message
        }
    }

    logger = CustomAiutaLogger()
    ```

The logger supports different log levels and can handle both messages and throwables. You can use it to:

- Control the verbosity of SDK logs
- Integrate SDK logs with your application's logging system
- Filter or transform log messages
- Add additional context to log messages

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Create [__Try-On with UI__ Configuration](/sdk/android/tryon-ui/configuration.md)
- :octicons-arrow-right-24: Using [__Try-Ons__](/sdk/android/tryon/usage.md)

</div>
