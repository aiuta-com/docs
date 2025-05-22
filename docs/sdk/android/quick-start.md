# Android SDK

!!! info
    Docs under construction
    
In this tutorial, you will learn how to initialize the SDK and figure out how to create
your own application using all the features of [Aiuta](https://aiuta.com/)

> Code example is [here](https://github.com/aiuta-com/android-sdk/tree/main/samples/tryon)

The Aiuta SDK for Android provides the ability to use public methods provided by [Aiuta](https://aiuta.com/)
from [dev portal](https://developer.aiuta.com/).


## Prerequisites

Before starting this tutorial:
- [Install Android Studio](https://developer.android.com/studio)


## Create a new project

First of all, we need to create a project in which we will use the Aiuta SDK

!!! question "How to create new project in Android Studio"
    1. On the Welcome screen, click **New Project**. Otherwise, from the main menu, select **File | New | New Project.**
    2. Choose **Empty Activity** project
    3. Wait for synchronization of IDEA


## Add dependencies

Let's add dependencies required for a Aiuta SDK.

- Be sure, that you use **mavenCentral** for solving dependencies in your **root build.gradle.kts** file

```kotlin
repositories {
    mavenCentral()
}
```

- Solve what the last version of Aiuta sdk on [Github releases page](https://github.com/aiuta-com/android-sdk/releases)

!!! note
    You also can check last version of artifacts on [Central Sonatype](https://central.sonatype.com/search?q=com.aiuta)

- Open the **app/build.gradle.kts** file and add the following artifacts to the dependencies block:

```kotlin
dependencies {
    val fashionVersion: String = "%latest_fashion_version%"
    implementation("com.aiuta:fashionsdk:$fashionVersion")
}
```

!!! note
    Pay your attention on [using the Bill of Materials](android/aiuta/get-started.md)