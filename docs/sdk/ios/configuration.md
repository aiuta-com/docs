# Configuration Guide

The Aiuta iOS SDK is highly configurable to meet your specific needs.

## Setting Up

```swift
await Aiuta.setup(configuration: Aiuta.Configuration)
```

__`Aiuta.Configuration`__ is an `enum` representing the configuration options for the Aiuta SDK. It contains several configuration presets that you can select depending on how detailed you want to customize the appearance and behavior of the SDK.

=== "Default Configurations"

    These presets contain the default appearance, feature set, and behavior.

    ```swift
    .debug(auth: Aiuta.Auth) // (1)!
    ```

    1.  A default configuration for development and testing.

        This configuration is optimized for debug builds and includes all recommended
        features and settings for development purposes. It performs validation checks
        on the `Info.plist` file and triggers a `fatalError()` if any required keys
        are missing. This ensures that issues are caught early during development.
        
        - [:material-arrow-down-left: __auth__](/sdk/developer/configuration/auth.md) required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

    ```swift
    .release(auth: Aiuta.Auth) // (1)!
    ```

    1.  A default configuration for production use.

        This configuration is optimized for release builds and includes all recommended
        features and settings for production environments. It skips all validation checks
        to prioritize stability and performance. Use this configuration when deploying
        the application to end users.
        
        - [:material-arrow-down-left: __auth__](/sdk/developer/configuration/auth.md) required to authenticate Aiuta SDK to use [API](/api/try-on/index.md) with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`.

=== "Custom Configuration"

    ```swift
    .custom(auth: Aiuta.Auth, // (1)!
        userInterface: UserInterface = .default, // (2)!
        features: Features = .default, // (3)!
        analytics: Aiuta.Analytics = .none, // (4)!
        debugSettings: DebugSettings = .release) // (5)!
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


    The Aiuta SDK for iOS employs a standardized configuration scheme for `custom` case consistent with our other SDKs. Just as the `Aiuta.Configuration` and its custom associated values have been modified to adhere to the naming conventions, all other nested cases will be conformed similarly.

    !!! doc "Please refer to the [__configuration scheme__](/sdk/developer/configuration/index.md)"

        !!! example ""
            Example compliance with [User Interface Scheme](/sdk/developer/configuration/ui/index.md)

            ```swift
            enum Aiuta.Configuration.UserInterface {

                case `default`
                
                case custom(theme: Theme = .aiuta(scheme: .light),
                            presentationStyle: PresentationStyle = .pageSheet,
                            swipeToDismissPolicy: SwipeToDismissPolicy = .protectTheNecessaryPages)
            }
            ```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [initialize and use](/sdk/ios/basic-usage.md) the SDK
- :octicons-arrow-right-24: [Try with test configuration](/sdk/ios/quick-test.md)

</div>
