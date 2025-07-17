# Installation of Try-On with UI

Aiuta Try-On provides pre-built UI components and screens for implementing virtual try-on functionality in your application. This guide will walk you through implementing try-on features using the UI integration approach, which offers a complete out-of-the-box experience.

The UI integration approach is ideal for developers who want to quickly implement try-on functionality with minimal custom code while maintaining a consistent look and feel with other Aiuta features.

## Dependencies

To use Aiuta Try On with UI components, you need to add the following dependencies to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-tryon-compose:{{ latest(android) }}")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-tryon-compose:{{ latest(android) }}"
    }
    ```

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

{% include-markdown "sdk/templates/android/using-bom.md" %}

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Quick Test](/sdk/android/tryon-ui/quick-test.md) SDK Propely Integrated
- :octicons-arrow-right-24: Create [Configuration](/sdk/android/tryon-ui/configuration.md)

</div>
