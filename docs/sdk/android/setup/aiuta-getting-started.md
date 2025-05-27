# Getting started with Aiuta

To start using Aiuta SDK, you need to create an instance of the `Aiuta` class. This class serves as the main entry point to the SDK and requires configuration of essential components.

Here's how to set up the Aiuta class:

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.aiuta

val aiuta: Aiuta = aiuta {
    // Configure authentication strategy
    authenticationStrategy = ...
    
    // Configure platform context
    platformContext = ...
    
    // Configure logger (optional)
    logger = ...
}
```

The `aiuta` builder function allows you to configure the following components:

- `authenticationStrategy`: **Required**. Defines how the SDK authenticates with the Aiuta backend.
- `platformContext`: **Required**. Provides platform-specific information and context.
- `logger`: Optional. Customizes logging behavior of the SDK.

Each of these components is described in detail in the sections below.


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

    You can find a more detailed description of API keys and JWT authentication in the SDK, as well as instructions on how to obtain them, in the [general configuration guide for developers](../../about/developer/configuration.md#auth)


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