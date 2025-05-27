# Aiuta User Interface Configuration

To customize the appearance and behavior of the try-on UI components, you need to create an instance of the `AiutaUserInterfaceConfiguration` class. This class allows you to configure various visual and interactive aspects of the user interface.

Here's how to set up the user interface configuration:

```kotlin
import com.aiuta.fashionsdk.configuration.ui.AiutaUserInterfaceConfiguration
import com.aiuta.fashionsdk.configuration.ui.aiutaUserInterface

val aiutaUserInterface = aiutaUserInterface {
    // Configure UI appearance and behavior
    // See the general configuration scheme for all available options
    

    // Example of configurations:
    actions = // Add AiutaUserInterfaceActions instance

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
```

The `aiutaUserInterface` builder function allows you to customize various aspects of the user interface. For a complete list of available configuration options, please refer to the [general configuration scheme](../../../../about/developer/user-interface.md).

{% include-markdown "sdk/templates/android/default-configuration-tip.md" %}

