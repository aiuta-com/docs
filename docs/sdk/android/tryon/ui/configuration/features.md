# Aiuta Features Configuration

To configure which features are enabled in your try-on experience, you need to create an instance of the `AiutaFeatures` class. This class controls which functionality is available to users in the UI components.

Here's how to set up the AiutaFeatures class:

```kotlin
import com.aiuta.fashionsdk.configuration.AiutaFeatures
import com.aiuta.fashionsdk.configuration.aiutaFeatures
import com.aiuta.fashionsdk.configuration.features.tryon
import com.aiuta.fashionsdk.configuration.features.welcome

val aiutaFeatures = aiutaFeatures {
    // Configure which features are enabled
    // See the general configuration scheme for all available options
    
    // Example of configurations:
    welcomeScreen {
        // Initialize configuraiton
    }
    
    tryOn {
        // Initialize configuraiton
    }
    ...
}
```

The `aiutaFeatures` builder function allows you to configure various features that will be available in your try-on experience. For a complete list of available features and their configuration options, please refer to the [general configuration scheme](/sdk/about/developer/features/).

{% include-markdown "sdk/templates/android/default-configuration-tip.md" %}

