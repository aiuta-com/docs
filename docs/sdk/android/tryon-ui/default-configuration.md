# Aiuta Default Configurations

To use default configurations in your try-on experience, you can utilize the provided builder functions that come with pre-configured settings. These defaults are designed to provide a good starting point for your implementation.


## Dependencies

The default configurations are provided through several dependencies:

- `fashionsdk-configuration-defaults-icons`: Contains default icons used in the UI components
- `fashionsdk-configuration-defaults-images`: Contains default images used in the UI components
- `fashionsdk-configuration-defaults`: A comprehensive package that includes both icons and images, plus provides builder functions for features and user interface configurations

To use the default configurations, add the following dependency to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        // Only default icon resources
        implementation("com.aiuta.fashionsdk:configuration-defaults-icon:<version>")

        // Only default image resources
        implementation("com.aiuta.fashionsdk:configuration-defaults-images:<version>")

        // Both icon and images with builders
        implementation("com.aiuta.fashionsdk:configuration-defaults:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        // Only default icon resources
        implementation "com.aiuta.fashionsdk:configuration-defaults-icon:<version>"

        // Only default image resources
        implementation "com.aiuta.fashionsdk:configuration-defaults-images:<version>"

        // Both icon and images with builders
        implementation "com.aiuta.fashionsdk:configuration-defaults:<version>"
    }
    ```

## Using Default Configurations

To use default configurations, you can use the provided builder functions `defaultAiutaFeatures` and `defaultAiutaUserInterfaceConfiguration`. These functions come with sensible defaults that you can customize by passing initialization parameters.

Here's how to use them:


```kotlin
import com.aiuta.fashionsdk.tryon.compose.aiutaConfiguration
import com.aiuta.fashionsdk.configuration.defaults.features.defaultAiutaFeatures
import com.aiuta.fashionsdk.configuration.defaults.theme.defaultAiutaUserInterfaceConfiguration

val aiutaConfiguration = aiutaConfiguration {
    aiuta = ... // Your initialized Aiuta instance
    
    // Configure default features
    defaultAiutaFeatures(
        // Initialization params
    )
    
    // Configure default user interface
    defaultAiutaUserInterfaceConfiguration(
        // Initialization params
    )
}
```
