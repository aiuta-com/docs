# Flutter SDK

The Aiuta Flutter SDK provides a virtual try-on solution as a [plug-in package :octicons-link-external-24:](https://flutter.dev/developing-packages/){:target="_blank"} that includes platform-specific implementation code and depends of native SDKs for [Android](../android/quick-start.md) and [iOS](../ios/quick-start.md) that uses [Aiuta Digital Try On API](../../api/overview.md).

## Requirements

```
sdk: >=3.1.0 <4.0.0
flutter: >= 3.19.6
```

=== "Android"

    ```
    minSdkVersion: 23
    targetSdkVersion: 35
    com.android.application: 8.6.0
    ndkVersion: 26.1.10909125
    ```

=== "iOS"

    ```
    iOS: 13+
    swift: 5.10
    Xcode: 15.3+
    ```

    !!! tip ""
        Can be compiled for iOS `12+`, but the SDK will not be available for use<br>
        [Check availability](basic-usage.md#checking-availability) at runtime if the target platform is iOS 12.

## Quick Start

1. [Installation](installation.md)
2. [Configuration](configuration.md)
3. [Basic Usage](basic-usage.md)

## Package and Sources

<div class="grid cards" markdown>

- :fontawesome-brands-flutter: &nbsp; [Pub.dev package :octicons-link-external-24:](https://pub.dev/packages/aiuta_flutter){:target="_blank"}
- :fontawesome-brands-github: &nbsp; [Plugin sources :octicons-link-external-24:](https://github.com/aiuta-com/flutter-sdk){:target="_blank"}
- :fontawesome-brands-github: &nbsp; [Android layer sources :octicons-link-external-24:](https://github.com/aiuta-com/android-sdk){:target="_blank"}
- :fontawesome-brands-github: &nbsp; [iOS layer sources :octicons-link-external-24:](https://github.com/aiuta-com/aiuta-ios-sdk){:target="_blank"}

</div>
