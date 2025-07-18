# Installation of Try-On

Aiuta Try On provides a powerful API for implementing virtual try-on functionality in your Android application. This guide will walk you through the core implementation of digital try-on features using the Aiuta SDK.

The core implementation gives you direct access to try-on generation capabilities without any pre-built UI components, allowing you to build custom experiences and integrate try-on functionality into your existing UI.


## Dependencies

To use Aiuta Try On, you need to add the following dependencies to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-tryon-core:{{ latest(android) }}")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-tryon-core:{{ latest(android) }}"
    }
    ```

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

{% include-markdown "sdk/templates/android/using-bom.md" %}

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Using [Try-Ons](/sdk/android/tryon/usage.md)

</div>
