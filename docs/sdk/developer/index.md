---
hide:
  - toc
---
# Developer Section

The Developer Section provides an overview of the configuration and model schemes that are common to all SDK implementations. By understanding these core concepts, developers can ensure a uniform approach to implementing the SDK, which helps maintain consistency and reduces redundancy in documentation.

!!! tip "Annotations"
    Don't miss them - click :material-information-outline: for more details

## SDK integration

In general, all SDK implementations are integrated in three steps:

1. Add dependency
2. Initialize with [Configuration](/sdk/developer/configuration/)
3. Call SDK UI by passing the [Product](/sdk/developer/common/product)

## Quick Start

Check out the quick start guide to get started with the platform

<div class="grid cards" markdown>

-   :fontawesome-brands-android:{ .lg } __Android__

    ---
    {% include-markdown "sdk/templates/android/requirements-base.md" %}
    :material-book-open-variant: [Quick Start](/sdk/android/)

-   :fontawesome-brands-apple:{ .lg } __iOS__

    ---
    {% include-markdown "sdk/templates/ios/requirements.md" %}
    :material-book-open-variant: [Quick Start](/sdk/ios/)

-   :fontawesome-brands-flutter:{ .lg } __Flutter__ <span class="md-platfroms">:fontawesome-brands-android: Android :fontawesome-brands-apple: iOS</span>

    ---
    ```
    sdk: >=3.1.0 <4.0.0
    flutter: >= 3.19.6
    ```
    :material-book-open-variant: [Quick Start](/sdk/flutter/)

-   :fontawesome-brands-js:{ .lg } __Web__

    ---
    Coming soon

</div>
