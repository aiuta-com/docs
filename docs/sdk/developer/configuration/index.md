---
hide:
  - toc
---
# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

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

1.  [:material-arrow-down-left:](/sdk/developer/configuration/auth.md) Required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

2. [:material-arrow-down-left:](/sdk/developer/configuration/ui/index.md) Configuration of the user interface presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

3. [:material-arrow-down-left:](/sdk/developer/configuration/features/index.md) Describes the set of features enabled in the SDK for the user and thier interaction with the app.

4. [:material-arrow-down-left:](/sdk/developer/configuration/analytics.md) Allows to receive analytics events from the SDK and send them to your analytics provider.

5. [:material-arrow-down-left:](/sdk/developer/configuration/debug-settings.md) Controls the logging settings and validation policies for various parameters.

!!! example "Default configuration"
    The configuration itself, as well as all themes and most features, have __built-in defaults__ on each platform. You decide how much detail you want to customize the behavior and appearance of the SDK. Starting with a few necessary parameters, ending with every aspect that is provided in the described schemes.

    The __minimum__ configuration for the fastest integration with the standard set of features and default UI requires only the following:
    
    - [Authentication](/sdk/developer/configuration/auth.md) credentials
    - Your Terms of Service URL
    - Add to [Cart](/sdk/developer/configuration/features/try-on.md#cart) handler

## Platform specifics

Check out the details and nuances of the configuration in the implementation of the platform you need:

<div class="grid cards small" markdown>

- [:fontawesome-brands-android:{ .lg } Android](/sdk/android/tryon-ui/configuration.md)
- [:fontawesome-brands-apple:{ .lg } iOS](/sdk/ios/configuration.md)
- [:fontawesome-brands-flutter:{ .lg } Flutter](/sdk/flutter/configuration.md)

</div>

## Sequence Diagram

{% include-markdown "sdk/templates/diagrams/initialization.md" %}
