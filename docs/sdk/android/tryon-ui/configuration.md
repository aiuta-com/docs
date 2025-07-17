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
See [Getting started with Aiuta](/sdk/android/base/aiuta-getting-started/) guide for details.
2. __Required__: Controls which features are enabled in your try-on experience.  
See [General configuration scheme](/sdk/about/developer/configuration/#features) to check list of available features and their configuration options.
3. __Required__: Customizes the look and feel of the UI components.  
See [General configuration scheme](/sdk/about/developer/configuration/#user-interface) to check complete list of available configuration options.
4. Optional: Configures debug-related settings for development and testing purposes.

{% include-markdown "sdk/templates/android/default-configuration-tip.md" %}

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [use Try-On with UI](/sdk/android/tryon-ui/basic-usage.md)
- :octicons-arrow-right-24: [Try with test products](/sdk/android/tryon-ui/quick-test.md)

</div>
