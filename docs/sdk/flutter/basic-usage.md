# Basic Usage

This guide covers the fundamental usage of the Aiuta Flutter SDK in your application.

## Checking Availability

```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';

final isAvailable = await Aiuta.isAvailable;
 
```    

??? question "When might the SDK be unavailable?"
    Since iOS SDK requires iOS 13.0 or later to operate, but can be compiled for iOS 12.0,
    this will always completes with false if the iOS version is lower than 13.0.

    On Android this future will most likely completes with true
    as it can not be compiled with unsupported toolchains.

    Other platforms will return false.

    Additional checks for availability are performed in the native code,
    and may be extended in the future.


## Initialization

First, make sure you've configured the SDK as described in the [Configuration](configuration.md) guide.

```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';

final aiuta = Aiuta(
  configuration: AiutaConfiguration(...) // (1)!
);

```

1. Your configuration for Aiuta

    !!! note ""
        :material-book-open-variant: Please refer to the [configuration scheme](/sdk/developer/configuration/index.md)

## Virtual Try-On

To start the virtual try-on flow for a product:

```dart
class ProductScreen extends StatelessWidget {
  final Aiuta aiuta;

  Future<void> startTryOn() async {
    try {
      await aiuta.startTryonFlow(
        product: AiutaProduct(...) // (1)!
      );
    } catch (e) {
      // Handle errors
    }
  }

  // ... rest of your widget
}
```

1. Your product info for Aiuta

    !!! doc "Please refer to the [product scheme](/sdk/developer/product.md)"

??? question "When does startTryonFlow Future completes?"

    The `startTryonFlow` Future completes when:

    1. The plugin has successfully connected to the native layer
    2. All parameters have been passed to the native layer
    3. The native layer has been configured and accepted the parameters
    4. The SDK UI has been displayed to the user

    This means the Future completes once the SDK UI is visible, not when the user completes or dismisses the try-on flow. To handle user completion, you should implement appropriate analytics listeners.

    Similarly, the `startHistoryFlow` method follows the same completion pattern - it completes when the history UI is displayed, not when the user finishes interacting with it.

??? question "What errors may occur and require handling?"

    The SDK may throw errors that generally indicate something completely wrong:

    1. The Flutter plugin cannot connect to the native SDK due to technical issues.
    2. The native SDK cannot parse the configuration or parameters sent from the plugin.
    3. The method is called on an unsupported platform without checking `isAvailable` first.
    4. The native SDK cannot find a valid UI context to display itself.

    These errors typically represent SDK issues rather than runtime conditions:

    - They should never occur
    - They cannot be fixed at runtime
    - Retrying the operation is unlikely to succeed
    - The best approach is to log and report them as bugs

## Viewing Try-On History

To show the user's try-on history:

```dart
try {
  await aiuta.startHistoryFlow();
} catch (e) {
  // Handle errors
}
```

## Checking State

You can check at any time whether the SDK UI is currently displayed:

```dart
final isDisplayed = await Aiuta.isForeground;
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Try with test products](/sdk/flutter/quick-test.md)

</div>
