# Configuration Guide

The Aiuta Flutter SDK is highly configurable to meet your specific needs. This guide will walk you through all available configuration options.

## Basic Configuration

The SDK is configured using the `AiutaConfiguration` class, which contains several key components:


```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';

// The main configuration class that initializes all SDK components
// All required parameters must be provided, while analytics is optional
final configuration = AiutaConfiguration(
  auth:// (1)!
  userInterface:// (2)!
  features:// (3)!
  analytics:// (4)!
  debugSettings:// (5)!
);

final aiuta = Aiuta(configuration: configuration);
```

1. __Required__: Handles API [authentication](#authentication) and token management
2. __Required__: Controls SDK presentation and visual appearance
3. __Required__: Manages SDK features and their interactions
4. __Optional__: Tracks SDK events and user interactions
5. __Required__: Controls logging and validation behavior

### Authentication

The SDK supports two authentication methods, each with specific use cases:

=== "API Key Authentication"

    ```dart
    // Use this for simpler integration where all requests use the same API key
    // Suitable for development and testing environments
    // Note: API key is used for all requests, including sensitive operations
    final auth = AiutaApiKeyAuth(
      apiKey: 'your-api-key-here' // Get this from the Aiuta Developer Portal
    );
    ```

=== "JWT Authentication"

    ```dart
    // Use this for production environments where sensitive operations need JWT
    // subscriptionId is used for non-sensitive requests
    // getJwt callback is called only for sensitive operations (e.g., starting try-on)
    final auth = AiutaJwtAuth(
      subscriptionId: 'your-subscription-id', // Used for non-sensitive requests
      getJwt: (Map<String, dynamic> params) async {
        // Called when a sensitive operation is requested
        // params may contain additional context for JWT generation
        // Must return a valid JWT string or throw an exception
        // If JWT is empty/invalid, the operation will fail with "Something went wrong"
        return await yourJwtService.generateToken(params);
      }
    );
    ```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: &nbsp; Learn how to [initialize and use](basic-usage.md) the SDK

</div>