# Basic Usage

This guide covers the fundamental usage of the Aiuta SDK in your iOS application.

## Initialization

First, make sure you've configured the SDK as described in the [Configuration](configuration.md) guide.

## Virtual Try-On

To present the virtual try-on interface for a product:

```swift
import Aiuta

// In your view controller
func showVirtualTryOn(for product: Product) {
    Aiuta.tryOn(product: product, in: self)
}
```

## Viewing Try-On History

To show the user's try-on history:

```swift
import Aiuta

// In your view controller
func showTryOnHistory() {
    let success = Aiuta.showHistory(in: self)
    if !success {
        // Handle the case where history cannot be shown
    }
}
```

## Checking SDK State

You can check various aspects of the SDK's state:

```swift
import Aiuta

// Get the SDK version
let version = Aiuta.sdkVersion

// Check if the SDK is currently displayed
let isDisplayed = Aiuta.isForeground
```

## Best Practices

1. Always configure the SDK before using any of its features
2. Handle cases where features might not be available
3. Check the SDK state before presenting UI components
4. Implement proper error handling

## Next Steps

- [Virtual Try-On](virtual-try-on.md)
- [History Management](history.md)
- [Analytics](analytics.md)
- [Authentication](authentication.md) 