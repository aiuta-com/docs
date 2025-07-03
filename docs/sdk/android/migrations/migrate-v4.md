# Migration to v4

This guide outlines the key changes and migration steps required for upgrading to **Aiuta Android SDK v4**. Please review all sections carefully to ensure a smooth transition.


## Platform & Build Requirements

| Requirement                | Version                |
|---------------------------|------------------------|
| **minSdk**                 | 23                     |
| **targetSdk**              | 35                     |
| **Kotlin**                 | 2.2.0                  |
| **Java**                   | 11                     |

!!! warning "Java 11 Required"

    Java 11 is now required for building and running the SDK due to the adoption of Compose Multiplatform.


## Dependency Updates

SDK v4 introduces several new packages to provide better modularity and feature separation (since 1.2.23):

| Dependency Package                                              | Purpose                                                                                   |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| `com.aiuta:fashionsdk-analytics-events:<version>`              | Provides event models and definitions for analytics tracking                              |
| `com.aiuta:fashionsdk-analytics:<version>`                     | Main analytics library for collecting and sending analytics events                        |
| `com.aiuta:fashionsdk-compose-resources:<version>`             | Shared Compose resources for UI components                                                |
| `com.aiuta:fashionsdk-configuration-defaults-icons:<version>`  | Default icon assets and configuration for the SDK UI                                      |
| `com.aiuta:fashionsdk-configuration-defaults-images:<version>` | Default image assets and configuration for the SDK UI                                     |
| `com.aiuta:fashionsdk-configuration-defaults:<version>`        | Predefined configuration sets for common use cases                                        |
| `com.aiuta:fashionsdk-configuration:<version>`                 | Core configuration engine for customizing SDK features and UI                             |
| `com.aiuta:fashionsdk-io:<version>`                            | Input/output utilities for file and data handling within the SDK                          |
| `com.aiuta:fashionsdk-logger:<version>`                        | Logging utilities for debugging and monitoring SDK behavior                               |
| `com.aiuta:fashionsdk-tryon-compose-uikit:<version>`           | UI components and layouts for Try-On experiences using Jetpack Compose                    |

!!! danger "Analytics"
    
    Please note: the analytics package has been renamed. You should now use `com.aiuta:fashionsdk-analytics:<version>` as the dependency for analytics features.


## New SDK Configuration Approach

SDK v4.1.0 [introduces](https://github.com/aiuta-com/aiuta-android-sdk/releases/tag/4.1.0) a new, unified way to configure the SDK using the `AiutaConfiguration` class. This approach provides a more flexible and modular configuration scheme for features and UI customization. See the full guide [here](/sdk/android/tryon-ui/configuration/).

## Kotlin Multiplatform (KMP) Support

The Aiuta SDK v4 is built with Kotlin Multiplatform (KMP) technology, enabling shared business logic and UI components across Android and iOS. This allows for easier code reuse and faster feature delivery on both platforms.

| Platform | Support Status | Notes |
|----------|---------------|--------|
| Android  | ✅ Supported  | Full support |
| iOS      | ✅ Supported  | Full support |
| Desktop  | 🟡 Beta      | Limited functionality |
| Web      | ❌ Not Supported | Not available |



