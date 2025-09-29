# Try-On with UI Configuration

To start using Aiuta Try On with UI components, you need to create an instance of the `AiutaConfiguration` class. This class serves as the main configuration point for the UI components and requires configuration of essential components.

Here's how to set up the AiutaConfiguration class:

```kotlin
import com.aiuta.fashionsdk.tryon.compose.aiutaConfiguration
import com.aiuta.fashionsdk.configuration.features.features
import com.aiuta.fashionsdk.configuration.features.onboarding.onboarding
import com.aiuta.fashionsdk.configuration.features.tryon.tryOn
import com.aiuta.fashionsdk.configuration.ui.actions.AiutaUserInterfaceActions
import com.aiuta.fashionsdk.configuration.ui.theme.label.label
import com.aiuta.fashionsdk.configuration.ui.theme.theme
import com.aiuta.fashionsdk.configuration.ui.theme.selection.selectionSnackbar
import com.aiuta.fashionsdk.configuration.ui.userInterface

val aiutaConfiguration = aiutaConfiguration {
    aiuta = ... // (1)!
    
    features { // (2)!
        onboarding {
            // Initialize configuraiton
        }
        
        tryOn {
            // Initialize configuraiton
        }
        ...
    }
    
    userInterface { // (3)!
        actions = AiutaUserInterfaceActions(...)

        theme {
            label {
                // Initialize theme
            }
            
            selectionSnackbar {
                // Initialize theme
            }
            ...
        }
    }

    debugSettings = ...  // (4)!
}
```

1. __Required__: Your initialized Aiuta instance that provides core functionality.  
See [Getting started with Aiuta](/sdk/android/base/aiuta-getting-started.md) guide for details.
2. __Required__: Controls which features are enabled in your try-on experience.  
See [General configuration scheme](/sdk/developer/configuration/features/index.md) to check list of available features and their configuration options.
3. __Required__: Customizes the look and feel of the UI components.  
See [General configuration scheme](/sdk/developer/configuration/ui/index.md) to check complete list of available configuration options.
4. Optional: Configures debug-related settings for development and testing purposes.


!!! doc "Please refer to the [__configuration scheme__](/sdk/developer/configuration/index.md) for more details"

## Default Configurations

To use default configurations in your try-on experience, you can utilize the provided builder functions that come with pre-configured settings. These defaults are designed to provide a good starting point for your implementation.


### Dependencies

To use the default configurations, add the following dependency to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        // Only default icon resources
        implementation("com.aiuta:fashionsdk-configuration-defaults-icon:{{ latest(android) }}")

        // Only default image resources
        implementation("com.aiuta:fashionsdk-configuration-defaults-images:{{ latest(android) }}")

        // Both icon and images with builders
        implementation("com.aiuta:fashionsdk-configuration-defaults:{{ latest(android) }}")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        // Only default icon resources
        implementation "com.aiuta:fashionsdk-configuration-defaults-icon:{{ latest(android) }}"

        // Only default image resources
        implementation "com.aiuta:fashionsdk-configuration-defaults-images:{{ latest(android) }}"

        // Both icon and images with builders
        implementation "com.aiuta:fashionsdk-configuration-defaults:{{ latest(android) }}"
    }
    ```

### Using Default Configurations

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

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [use Try-On with UI](/sdk/android/tryon-ui/basic-usage.md)
- :octicons-arrow-right-24: [Try with test configuration](/sdk/android/tryon-ui/quick-test.md)

</div>
