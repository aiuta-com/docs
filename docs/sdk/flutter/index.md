# Flutter SDK

The Aiuta Flutter SDK provides a virtual try-on solution as a [plug-in package :octicons-link-external-24:](https://flutter.dev/developing-packages/){:target="_blank"} that includes platform-specific implementation code and depends of native SDKs for [Android](../android/quick-start.md) and [iOS](../ios/quick-start.md) that uses [Aiuta Digital Try On API](../../api/overview.md).

## Requirements

{% include-markdown "sdk/templates/flutter/requirements.md" %}

=== "Android"

    {% include-markdown "sdk/templates/android/requirements-flutter.md" %}

=== "iOS"

    {% include-markdown "sdk/templates/ios/requirements.md" %}

    !!! tip ""
        Can be compiled for iOS `12+`, but the SDK will not be available for use<br>
        [Check availability](basic-usage.md#checking-availability) at runtime if the target platform is iOS 12.

## Quick Start

1. [Installation](installation.md)
2. [Configuration](configuration.md)
3. [Basic Usage](basic-usage.md)

## Package and Sources

<div class="grid cards" markdown>

- :fontawesome-brands-flutter: [Pub.dev package :octicons-link-external-24:](https://pub.dev/packages/aiuta_flutter){:target="_blank"}
- :fontawesome-brands-github: [Plugin sources :octicons-link-external-24:](https://github.com/aiuta-com/flutter-sdk){:target="_blank"}
- :fontawesome-brands-github: [Android layer sources :octicons-link-external-24:](https://github.com/aiuta-com/android-sdk){:target="_blank"}
- :fontawesome-brands-github: [iOS layer sources :octicons-link-external-24:](https://github.com/aiuta-com/aiuta-ios-sdk){:target="_blank"}

</div>
