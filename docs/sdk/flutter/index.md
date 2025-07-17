# Flutter SDK

The Aiuta Flutter SDK provides a virtual try-on solution as a [plug-in package :octicons-link-external-24:](https://flutter.dev/developing-packages/){:target="_blank"} that includes platform-specific implementation code and depends of native SDKs for [Android](/sdk/android/index.md) and [iOS](/sdk/ios/index.md) that uses [Aiuta Virtual Try On API](/api/try-on/index.md).

{% include-markdown "sdk/templates/intro-links.md" %}

## Requirements

{% include-markdown "sdk/templates/flutter/requirements.md" %}

=== "Android"

    {% include-markdown "sdk/templates/android/requirements-flutter.md" %}

=== "iOS"

    {% include-markdown "sdk/templates/ios/requirements.md" %}

    !!! tip ""
        Can be compiled for iOS `12+`, but the SDK will not be available for use<br>
        [Check availability](/sdk/flutter/basic-usage.md#checking-availability) at runtime if the target platform is iOS 12.

## Quick Start

1. [Installation](/sdk/flutter/installation.md)
2. [Configuration](/sdk/flutter/configuration.md)
3. [Basic Usage](/sdk/flutter/basic-usage.md)

## Package and Sources

<div class="grid cards" markdown>

- :fontawesome-brands-flutter: [Pub.dev package :octicons-link-external-24:]({{ pub_package() }}){:target="_blank"}
- :fontawesome-brands-github: [Plugin sources :octicons-link-external-24:]({{ repo(flutter) }}){:target="_blank"}
- :fontawesome-brands-github: [Android layer sources :octicons-link-external-24:]({{ repo(android) }}){:target="_blank"}
- :fontawesome-brands-github: [iOS layer sources :octicons-link-external-24:]({{ repo(ios) }}){:target="_blank"}

</div>
