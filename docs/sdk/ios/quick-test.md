# Quick Test

This guide describes how to test the Aiuta SDK in your iOS application after installation.
It includes steps for setting up the configuration with a demo API key and using example products to start the TryOn.

```swift
import AiutaSdk
```

## Setup

For quick test purposes you can use demo `apiKey` auth

```swift
await Aiuta.setup(configuration: .debug(auth: .apiKey("{{ aiuta.api_key }}")))
```

!!! note ""
    A good place to initialize third-party libraries is usually your application delegate's `application(_:didFinishLaunchingWithOptions:)` - you can setup Aiuta there or right before calling the try-on.

## Start TryOn

You can use one of the following product examples that will work with the demo `apiKey`

{{ gen_test_products("sdk/templates/ios/test-tryon.swift") }}

## Show History

```swift
await Aiuta.showHistory()
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Create your custom [Configuration](/sdk/ios/configuration.md)

</div>
