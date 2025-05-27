# Paging

In this tutorial, you will learn how to use default implementation of paging with Paging 3 library and Aiuta Try On.

## Prerequisites

Before starting this tutorial:

- [Initialize Aiuta Try On](making-try-ons.md)


## Add dependencies

Let's add dependencies required for default paging implementation:

=== "Kotlin"
    ```kotlin
    dependencies {
        implementation("com.aiuta:fashionsdk-tryon-paging:<version>")
    }
    ```

=== "Groovy"
    ```groovy
    dependencies {
        implementation "com.aiuta:fashionsdk-tryon-paging:<version>"
    }
    ```

## Paging usage

Now you can use `Pager` from Paging 3 library to implement pagination behaviour using our `ContainerPagingSource` like that:

```kotlin
val pagingFlow = Pager(
    config = PagingConfig(
        pageSize = DEFAULT_PAGE_SIZE,
    ),
    pagingSourceFactory = {
        ContainerPagingSource {
            // Method, which provide PageContainer<T> items
        }
    },
).flow
```

Example of usage such approach you can find in `implementation("com.aiuta:fashionsdk-tryon-paging:<version>")` to get list of SKU item.
