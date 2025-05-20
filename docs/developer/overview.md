# General SDK documentation and schemes

This area covers the common approach across our SDKs for [Android](../android/overview.md), [iOS](../ios/overview.md), and [Flutter](../flutter/overview.md). 

## Implementation Overview

<div class="annotate" markdown>
1. Add dependency to your project&nbsp; (1)
2. Set up the SDK with a [configuration](scheme/configuration.md)
3. Start the virtual try-on by passing a [product](scheme/product.md) to the SDK
</div>

1.  <div class="grid cards" markdown>

    - :fontawesome-brands-android: &nbsp; Android
    - :fontawesome-brands-apple: &nbsp; iOS
    - :fontawesome-brands-flutter: &nbsp; [Flutter](../flutter/installation.md)

    </div>

## Naming convention

Implementation and naming details may vary depending on the specific platform, but the core concepts and overall structure remain consistent across all platforms.

!!! example "Same same but different"
    For example type names, described in the schemes, like: 

    - `Configuration`

        - in Swift it will be `Aiuta.Configuration`
        - in Kotlin and Dart - `AiutaConfiguration`

    - `UserInterface`

        - in Swift it will be `Aiuta.Configuration.UserInterface`
        - in Kotlin and Dart - `AiutaUserInterfaceConfiguration`

    - `Product`

        - in Swift it will be `Aiuta.Product`
        - in Kotlin and Dart - `AiutaProduct`

    and so on - the key part of the name is the same.
    
## Justification

A scheme-based approach in the documentation applies core concepts and structures uniformly, unifying the SDK's understanding and implementation. By following this strategy, we achieve consistency in our SDK's implementations and minimize redundancy in our documentation for each platform. We use this documentation ourselves for development.
