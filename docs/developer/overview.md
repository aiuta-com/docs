# General SDK documentation and schemes

This area covers the common public models used across our SDKs for [Android](../android/overview.md), [iOS](../ios/overview.md), and [Flutter](../flutter/overview.md). While the implementation and naming details may vary depending on the specific platform, the core concepts and overall structure remain consistent across all platforms.

!!! example "Naming"
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
