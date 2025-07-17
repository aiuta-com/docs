# Using Aiuta Analytics

!!! tip "General analytics scheme"
    For more information about available events and their parameters, see [Analytics Events](/sdk/about/analytics/analytics.md).

To start using Aiuta Analytics in your application, follow these steps:

1. Create an instance of `AiutaAnalytics` using the standard extension:

    ```kotlin
    import com.aiuta.fashionsdk.Aiuta
    import com.aiuta.fashionsdk.analytics.AiutaAnalytics
    import com.aiuta.fashionsdk.analytics.analytics

    val aiuta: Aiuta = ... // Your initialized Aiuta instance
    val aiutaAnalytics: AiutaAnalytics = aiuta.analytics
    ```

2. You can now observe `AiutaAnalyticsEvent` from the SDK:

    ```kotlin
    aiutaAnalytics.analyticFlow.collect { newEvent ->
        // Handle new events from SDK
    }
    ```
