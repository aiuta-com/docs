# General SDK documentation and API reference for developers

This area covers the common configuration schemes and public models used across our SDKs for [Android](android/overview.md), [iOS](ios/overview.md), and [Flutter](flutter/overview.md). While the implementation details and naming conventions may vary depending on the specific platform, the core concepts and overall structure remain consistent across all platforms.

!!! example ""
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
    
    This approach allows us to avoid repetition in documentation and keep functionality and implementation consistent across different platforms.

