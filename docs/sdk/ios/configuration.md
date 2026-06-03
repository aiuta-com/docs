# Configuration Guide

The Aiuta iOS SDK is highly configurable to meet your specific needs.

## Setting Up

```swift
Aiuta.setup(configuration: Aiuta.Configuration)
```

__`Aiuta.Configuration`__ is a `struct` representing the configuration options for the Aiuta SDK. It offers a ready-made `.default(…)` preset that you can adopt as-is or extend, plus a full initializer for complete customization — depending on how detailed you want to customize the appearance and behavior of the SDK.

=== "Default Configurations"

    This preset contains the default appearance, feature set, and behavior.

    ```swift
    .default(auth: Aiuta.Auth) // (1)!
    ```

    1.  A ready-to-use configuration with all recommended features and settings.

        It authenticates the SDK and uses the builtin icons and images. Whether the
        configuration is optimized for development or production is controlled by the
        `debugSettings` parameter (see below), which defaults to `.release`.

        - [:material-arrow-down-left: __auth__](/sdk/developer/configuration/auth.md) required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

    ```swift
    .default(auth: Aiuta.Auth, // (1)!
        debugSettings: DebugSettings = .release) // (2)!
    ```

    1.  - [:material-arrow-down-left: __auth__](/sdk/developer/configuration/auth.md) required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

    2.  [:material-arrow-down-left: __debugSettings__](/sdk/developer/configuration/debug-settings.md) controls logging and validation policies.

        - `.debug` is intended for development and testing. It enables logging and performs
          validation checks — for example on the `Info.plist` file — triggering a `fatalError()`
          if any required keys are missing, so that issues are caught early during development.
        - `.release` is the default and is intended for production. It disables logging and skips
          all validation checks to prioritize stability and performance. Use it when deploying the
          application to end users.

=== "Custom Configuration"

    ```swift
    Aiuta.Configuration(auth: Aiuta.Auth, // (1)!
        userInterface: UserInterface, // (2)!
        features: Features, // (3)!
        analytics: Aiuta.Analytics?, // (4)!
        debugSettings: DebugSettings) // (5)!
    ```

    1.  A fully customizable configuration for the SDK.
        
        This configuration allows developers to customize every aspect of the SDK,
        including authentication, user interface, features, analytics, and debug settings.
        Use this option to tailor the SDK to specific application requirements.
            
        - [:material-arrow-down-left: __auth__](/sdk/developer/configuration/auth.md) required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

    2. [:material-arrow-down-left: __userInterface__](/sdk/developer/configuration/ui/index.md) configuration of the presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

    3. Describes the set of [:material-arrow-down-left: __features__](/sdk/developer/configuration/features/index.md)  enabled in the SDK for the user and thier interaction with the app.

    4. Allows to receive [:material-arrow-down-left: __analytics__](/sdk/developer/configuration/analytics.md) events from the SDK and send them to your analytics provider.

    5. [:material-arrow-down-left: __debugSettings__](/sdk/developer/configuration/debug-settings.md) controls the logging settings and validation policies for various parameters.


    The Aiuta SDK for iOS employs a standardized configuration scheme consistent with our other SDKs. Just as `Aiuta.Configuration` and its initializer parameters adhere to the naming conventions, all other nested types are conformed similarly.

    !!! doc "Please refer to the [__configuration scheme__](/sdk/developer/configuration/index.md)"

        !!! example ""
            Example compliance with [User Interface Scheme](/sdk/developer/configuration/ui/index.md)

            ```swift
            struct Aiuta.Configuration.UserInterface {

                init(theme: Theme,
                     presentationStyle: PresentationStyle,
                     swipeToDismissPolicy: SwipeToDismissPolicy)
            }
            ```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [initialize and use](/sdk/ios/basic-usage.md) the SDK
- :octicons-arrow-right-24: [Try with test configuration](/sdk/ios/quick-test.md)

</div>
