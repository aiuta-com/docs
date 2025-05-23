# Configuration Guide

The Aiuta Flutter SDK is highly configurable to meet your specific needs.

## Basic Configuration

The SDK is configured using the `AiutaConfiguration` class, which contains several key components:


```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';

final configuration = AiutaConfiguration( // (1)!
  auth: AiutaAuth(...), // (2)!
  userInterface: AiutaUserInterfaceConfiguration(...), // (3)!
  features: AiutaFeatures(...), // (4)!
  analytics: AiutaAnalytics(...) | null, // (5)!
  debugSettings: AiutaDebugSettings(...) // (6)!
);

final aiuta = Aiuta(configuration: configuration);
```

1. The main configuration class that initializes all SDK components. All required parameters must be provided, while analytics is optional
2. __Required__: Handles API authentication and token management
3. __Required__: Controls SDK presentation and visual appearance
4. __Required__: Manages SDK features and their interactions
5. __Optional__: Tracks SDK events and user interactions
6. __Required__: Controls logging and validation behavior

### Configuration Scheme

The Aiuta SDK for Flutter employs a standardized configuration scheme consistent with our other SDKs. Just as the primary `AiutaConfiguration` and its associated property class names have been modified to adhere to the naming conventions, all other internal classes will be updated similarly.

<div class="grid cards" markdown>

- :material-book-open-variant:{ .lg } Please refer to the [configuration scheme](../about/developer/configuration.md)

</div>

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: &nbsp; Learn how to [initialize and use](basic-usage.md) the SDK

</div>
