# Getting started with Aiuta Analytic

In this guide, you will learn how to initialize `AiutaAnalytic` and observe `AnalyticEvent` from the SDK.


## Prerequisites

Before starting this tutorial:

- [Initialize Aiuta SDK in your project](/sdk/android/setup/installation/)


## Dependencies

To use Aiuta Analytic functionality, you need to add the following dependency to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-analytic:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-analytic:<version>"
    }
    ```

## Using Aiuta Analytic


!!! tip "General analytic scheme"

    For more information about available events and their parameters, see [Analytics Events](/sdk/about/analytics/analytics/).


To start using Aiuta Analytic in your application, follow these steps:

- Create an instance of `AiutaAnalytic` using the standard extension:

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.analytic.AiutaAnalytic
import com.aiuta.fashionsdk.analytic.analytic

val aiuta: Aiuta = ... // Your initialized Aiuta instance
val aiutaAnalytic: AiutaAnalytic = aiuta.analytic
```

- You can now observe `AnalyticEvent` from the SDK:

```kotlin
aiutaAnalytic.analyticFlow.collect { newEvent ->
    // Handle new events from SDK
}
```