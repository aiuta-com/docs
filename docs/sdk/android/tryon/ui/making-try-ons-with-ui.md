# Making Try-Ons with UI

Aiuta Try On provides pre-built UI components and screens for implementing virtual try-on functionality in your application. This guide will walk you through implementing try-on features using the UI integration approach, which offers a complete out-of-the-box experience.

The UI integration approach is ideal for developers who want to quickly implement try-on functionality with minimal custom code while maintaining a consistent look and feel with other Aiuta features.

## Dependencies

To use Aiuta Try On with UI components, you need to add the following dependencies to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-tryon-compose:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-tryon-compose:<version>"
    }
    ```

!!! tip "Dependencies tip"

    The `fashionsdk-tryon-compose` artifact already includes `fashionsdk-tryon-core` and `fashionsdk-configuration` dependencies, so you don't need to explicitly declare them in your dependencies.


## Configuration

Before using the UI components, you need to configure `AiutaConfiguration`. For detailed information about configuration options and setup, see [Getting Started with Aiuta Configuration](configuration/getting-started-configuration.md).

The configuration allows you to customize various aspects of the try-on experience through:

- **Features Configuration**: Control which features are enabled in your try-on experience
- **User Interface Configuration**: Customize the look and feel of the UI components

{% include-markdown "sdk/templates/android/default-configuration-tip.md" %}


## UI Entry Points

Aiuta Try On provides two main UI entry points for implementing virtual try-on functionality:

=== "AiutaTryOnFlow"
    `AiutaTryOnFlow` is the main entry point for creating new try-ons. It provides a complete flow for:
    
    - Selecting a product to try on
    - Taking or uploading a photo
    - Generating and viewing the try-on result
        
    ```kotlin
    AiutaTryOnFlow(
        modifier = ...,
        aiutaConfiguration = ...,
        productForGeneration = ...,
    )
    ```

=== "HistoryFlow"
    `HistoryFlow` allows users to view their try-on history and previous results. It provides:
    
    - Ability to view and share past results
    
    ```kotlin
    HistoryFlow(
        modifier = ...,
        aiutaConfiguration = ...,
    )
    ```

Both flows are composable functions that can be integrated into your existing Compose UI. They handle all the necessary UI states and user interactions internally, providing a seamless try-on experience.
