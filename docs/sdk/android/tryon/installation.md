# Installation of Try-On

Aiuta Try On provides a powerful API for implementing virtual try-on functionality in your Android application. This guide will walk you through the core implementation of digital try-on features using the Aiuta SDK.

The core implementation gives you direct access to try-on generation capabilities without any pre-built UI components, allowing you to build custom experiences and integrate try-on functionality into your existing UI.


## Dependencies

To use Aiuta Try On, you need to add the following dependencies to your project:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-tryon-core:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-tryon-core:<version>"
    }
    ```

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

{% include-markdown "sdk/templates/android/using-bom.md" %}

## Using Aiuta Try-Ons


### Initialization

Create an instance of `AiutaTryOn` using the extension function:

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.tryon.core.AiutaTryOn
import com.aiuta.fashionsdk.tryon.core.tryon

val aiuta: Aiuta = ... // Your initialized Aiuta instance
val aiutaTryOn: AiutaTryOn = aiuta.tryon
```

Once you have created the `AiutaTryOn` instance, you're ready to implement digital try-on functionality in your application.



### Start Generation

To start generation, you need the following:

* `productId` - which will be used to fit on the uploaded photo
* `productCatalogName` (optional) - category name of the generated product
* Source of image - can be URI of file or URL of already uploaded image

That is why the interface `ProductGenerationContainer` has 2 implementations - `ProductGenerationUriContainer` and `ProductGenerationUrlContainer`.

After receiving all the necessary information, you can call the `startproductGeneration()` method, passing all the data through a special wrapper `ProductGenerationContainer` and collect the returned flow:

```kotlin
val receivingFlow = aiutaTryOn.startProductGeneration(
    container = // ProductGenerationUriContainer or ProductGenerationUrlContainer
)
```


### Observing Result

After the generation starts, you need to wait for some time until the entire result is ready. You can track the current status and get the result by collecting the returned flow from `startProductGeneration()`. As the result is ready, the necessary `productGenerationStatus.SuccessGenerationStatus` will be emitted.

To learn more about all possible `productGenerationStatus`, see the code or API reference.

