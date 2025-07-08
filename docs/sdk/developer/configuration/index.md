---
hide:
  - toc
---
# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

??? abstract "Type Definitions & Naming Convention"
    {% include-markdown "sdk/templates/developer/type-definitions.md" %}

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

1.  [:material-arrow-down-left:](/sdk/developer/configuration/auth/) Required to authenticate Aiuta SDK to use [API](https://developer.aiuta.com/products/digital-try-on/documentation){:target="_blank"} with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

2. [:material-arrow-down-left:](/sdk/developer/configuration/ui/) Configuration of the user interface presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

3. [:material-arrow-down-left:](/sdk/developer/configuration/features/) Describes the set of features enabled in the SDK for the user and thier interaction with the app.

4. [:material-arrow-down-left:](/sdk/developer/configuration/analytics/) Allows to receive analytics events from the SDK and send them to your analytics provider.

5. [:material-arrow-down-left:](/sdk/developer/configuration/debug-settings/) Controls the logging settings and validation policies for various parameters.

## Sequence Diagram

{% include-markdown "sdk/templates/diagrams/initialization.md" %}
