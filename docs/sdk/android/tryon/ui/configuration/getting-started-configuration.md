# Getting Started with Aiuta Configuration

To start using Aiuta Try On with UI components, you need to create an instance of the `AiutaConfiguration` class. This class serves as the main configuration point for the UI components and requires configuration of essential components.

Here's how to set up the AiutaConfiguration class:

```kotlin
import com.aiuta.fashionsdk.configuration.AiutaConfiguration
import com.aiuta.fashionsdk.configuration.aiutaConfiguration

val aiutaConfiguration = aiutaConfiguration {
    aiuta = ... // Your initialized Aiuta instance
    
    // Configure features
    features = ... // Add AiutaFeatures instance
    
    // Configure user interface
    userInterface = ... // Add AiutaUserInterfaceConfiguration instance

    // Configure debug settings (optional)
    debugSettings = ... // Add AiutaDebugSettings instance
}
```

The `aiutaConfiguration` builder function allows you to configure the following components:

- `aiuta` **Required**. Your initialized Aiuta instance that provides core functionality.  
  See [Getting started with Aiuta](/sdk/android/setup/aiuta-getting-started/) guide for details.

- `features` **Required**. Controls which features are enabled in your try-on experience.  
  See [Features Configuration](/sdk/android/tryon/ui/configuration/features/) for details.

- `userInterface` **Required**. Customizes the look and feel of the UI components.  
  See [User Interface Configuration](/sdk/android/tryon/ui/configuration/user-interface/) for details.

- `debugSettings` Optional. Configures debug-related settings for development and testing purposes.  
  See [Debug Settings](/sdk/android/tryon/ui/configuration/default-configurations/) for details.

{% include-markdown "sdk/templates/android/default-configuration-tip.md" %}

