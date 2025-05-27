# Installation
    
In this tutorial, you will learn how to initialize the SDK and figure out how to create
your own application using all the features of [Aiuta](https://aiuta.com/)


## Add dependencies

{% include-markdown "sdk/templates/android/latest-version-tip.md" %}

??? tip "Using the Bill of Materials"
    For better dependency management and version compatibility, consider using the [Bill of Materials (BOM)](/sdk/android/setup/bom/). BOM helps ensure all SDK components use compatible versions.

Open the **app/build.gradle.kts** file and add Aiuta artifacts to the dependencies block:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk:<version>")
        implementation("com.aiuta:fashionsdk-configuration:<version>")
        ...
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk:<version>"
        implementation "com.aiuta:fashionsdk-configuration:<version>"
        ...
    }
    ```

## Initialize Aiuta

- After adding the dependencies, create an instance of `Aiuta` class which serves as the main entry point to the SDK: 

```kotlin
import com.aiuta.fashionsdk.Aiuta
import com.aiuta.fashionsdk.aiuta

val aiuta: Aiuta = aiuta {
    authenticationStrategy = ...
    platformContext = ...
}
```

!!! tip "Detailed description of setup Aiuta instance"

    For more detailed explanation of configuration `Aiuta` class, please check [getting started guide](/sdk/android/setup/aiuta-getting-started/)

- That's it! You are ready to explore all Aiuta possibilities