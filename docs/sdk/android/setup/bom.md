# Using Bill of Materials

The Aiuta SDK uses Bill of Materials (BOM) to manage dependencies and ensure version compatibility. This guide explains how to use BOM in your project.

## What is BOM?

Bill of Materials (BOM) is a special kind of POM file that controls the versions of dependencies. It helps you manage dependencies in a centralized way and ensures that all modules use compatible versions.

## Adding BOM to Your Project

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

=== "Kotlin"
    ```kotlin
    dependencies {
        // 1. Add BOM 
        implementation(platform("com.aiuta:fashionsdk-bom:<version>"))

        // 2. Add all required for you dependencies
        implementation("com.aiuta:fashionsdk")
        implementation("com.aiuta:fashionsdk-configuration") 
        ...
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        // 1. Add BOM
        implementation platform("com.aiuta:fashionsdk-bom:<version>")

        // 2. Add all required for you dependencies
        implementation "com.aiuta:fashionsdk"
        implementation "com.aiuta:fashionsdk-configuration"
        ...
    }
    ```
