## Import

```swift
import AiutaSDK
```

## Setup

For quick test purposes you can use demo `apiKey`

```swift
await Aiuta.setup(configuration: .debug(auth: .apiKey("{{ aiuta.api.demo_key }}")))
```

## Start TryOn

You can use one of the following product examples that will work with the demo `apiKey`

{{ gen_test_products("sdk/templates/ios/test-tryon.swift") }}

## Show History

```swift
await Aiuta.showHistory()
```
