# Basic Usage

This guide covers the fundamental usage of the Aiuta iOS SDK in your application.

```swift
import AiutaSDK
```

## Setup

First, make sure you've configured the SDK as described in the [Configuration](configuration.md) guide.

```swift
await Aiuta.setup(configuration: Aiuta.Configuration) // (1)!
```

1. Your configuration for Aiuta

    !!! doc "Please refer to the [Configuration](configuration.md) guide."

## Virtual Try-On

To start the virtual try-on flow for a product:

```swift
await Aiuta.tryOn(product: Aiuta.Product) // (1)!
```

1. Your product info for Aiuta

    !!! doc "Please refer to the [product scheme](/sdk/developer/product.md)"


## Generation History

To show the user's try-on history:

```swift
await Aiuta.showHistory()
```

## Current State

You can check at any time whether the SDK UI is currently displayed:

```swift
let isDisplayed = await Aiuta.isForeground
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Try with test products](/sdk/ios/quick-test.md)

</div>
