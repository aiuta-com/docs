# Try-On with UI Basic Usage

Aiuta Try On provides two main UI entry points for implementing virtual try-on functionality. 
Both flows are composable functions that can be integrated into your existing Compose UI. They handle all the necessary UI states and user interactions internally, providing a seamless try-on experience.

## Try-On Flow

`AiutaTryOnFlow` is the main entry point for creating new try-ons. It provides a complete flow for:

- Selecting a product to try on
- Taking or uploading a photo
- Generating and viewing the try-on result
    
```kotlin
AiutaTryOnFlow(
    modifier = ...,
    aiutaConfiguration = ...,
    productForGeneration = ...,
)
```

## History Flow

`HistoryFlow` allows users to view their try-on history and previous results. It provides:

- Ability to view and share past results

```kotlin
HistoryFlow(
    modifier = ...,
    aiutaConfiguration = ...,
)
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Try with test products](/sdk/android/tryon-ui/quick-test.md)

</div>
