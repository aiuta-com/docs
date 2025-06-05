# Installation of Analytics

In this guide, you will learn how to initialize `AiutaAnalytics` and observe `AiutaAnalyticsEvent` from the SDK.


## Dependencies

To use Aiuta Analytics functionality, you need to add the following dependency to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-analytics:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-analytics:<version>"
    }
    ```

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

{% include-markdown "sdk/templates/android/using-bom.md" %}

## Using Aiuta Analytics


!!! tip "General analytics scheme"

    For more information about available events and their parameters, see [Analytics Events](/sdk/about/analytics/analytics/).


To start using Aiuta Analytics in your application, follow these steps:

- Create an instance of `AiutaAnalytics` using the standard extension:

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.analytics.AiutaAnalytics
import com.aiuta.fashionsdk.analytics.analytics

val aiuta: Aiuta = ... // Your initialized Aiuta instance
val aiutaAnalytics: AiutaAnalytics = aiuta.analytics
```

- You can now observe `AiutaAnalyticsEvent` from the SDK:

```kotlin
aiutaAnalytics.analyticFlow.collect { newEvent ->
    // Handle new events from SDK
}
```