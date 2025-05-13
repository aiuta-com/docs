# Configuration

The Aiuta SDK can be configured in several ways to suit your application's needs.

## Basic Configuration

The simplest way to configure the SDK is using the `setup` method:

```swift
import Aiuta

// Configure the SDK
Aiuta.setup(configuration: Configuration(
    // Your configuration parameters here
))
```

## Lazy Configuration

For cases where you want to configure the SDK just before its first use:

```swift
Aiuta.setup(lazy: {
    // Return your configuration here
    return Configuration(
        // Your configuration parameters
    )
})
```

## Factory Configuration

If you need to provide a fresh configuration before each SDK use:

```swift
Aiuta.setup(factory: {
    // Return a new configuration each time
    return Configuration(
        // Your configuration parameters
    )
})
```

## Configuration Parameters

The `Configuration` struct accepts various parameters to customize the SDK's behavior:

- API Keys
- Environment settings
- Feature flags
- Custom UI settings

For detailed information about available configuration options, see the [API Reference](api/configuration.md).

## Next Steps

- [Basic Usage](basic-usage.md)
- [Virtual Try-On](virtual-try-on.md)
- [Analytics](analytics.md) 