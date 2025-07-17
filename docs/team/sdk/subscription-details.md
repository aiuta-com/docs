# Subscription Details

This scheme describes internal configuration / subscription details that SDK will request by calling `/subscription_details`.

{% include-markdown "team/sdk/templates/common-reminders.md" %}

## Scheme

```typescript
SubscriptionDetails {
  poweredBySticker: PoweredBySticker | null // (1)!
  retryCounts: RetryCounts | null // (2)!
  operationDelaysSequence: List<OperationDelay> | null // (3)!
}
```

1. Controls the behavior of the [“Powered by Aiuta” label](/sdk/developer/configuration/ui/theme/powered-by.md) that may be present on some SDK screens (e.g. the progress animation screen).

    !!! example "Defaults"
        ```typescript
        urlIos: null
        urlAndroid: null
        isVisible: false
        ```

2. Specifies the number of __additional__ attempts if an error occurs on a particular action before the user is shown an error telling them that something went wrong (the user can click the try again button to restart the process).

    !!! example "Defaults"
        ```typescript
        photoUpload: 2
        operationStart: 0
        operationStatus: 2
        resultDownload: 2
        ```

3. Sequence of delays before requesting the generation operation status. 

    !!! warning ""
        If the sequence does not contain a value with an `infinite` mode and ends before a successful result is obtained, the operation will fail with a timeout error, the user will be shown a "something went wrong" error.

    !!! example "Defaults"
        ```typescript
        [
          {
            mode: recurring
            delay: 1
            repeat: 4
          },
          {
            mode: recurring
            delay: 0.5
            repeat: 20
          },
          {
            mode: infinite
            delay: 3
          }
        ]
        ```

### Powered By Sticker

```typescript
PoweredBySticker {
  urlIos: String | null // (1)!
  urlAndroid: String | null // (2)!
  isVisible: true | false | null // (3)!
}
```

1. URL for iOS to open by click on the "powered by" label. If not specified the label interaction is disabled.

    !!! example ""
        Default is `null` and "powered by" label is not interactive.

2. URL for Android to open by click on the "powered by" label. If not specified the label interaction is disabled.

    !!! example ""
        Default is `null` and "powered by" label is not interactive.

3. The only value to "powered by" label be visible is explicit `true` in the subscription details. In any other case "powered by" is hidden.

    !!! example ""
        Default is `false` and "powered by" label is hidden.

### Retry Counts     

```typescript
RetryCounts {
  photoUpload: Int | null // (1)!
  operationStart: Int | null // (2)!
  operationStatus: Int | null // (3)!
  resultDownload: Int | null // (4)!
}
```

1. Number of retries for photo uploading

    !!! example ""
        `2` by default

2. Number of network request retries to start try-on operation, has no effect if the server responds with error

    !!! example ""
        `0` by default

3. Number of network request retries per loop to check operation status, if the server responded, the number of retries will reset in the next loop after the delay in the `operationDelaysSequence`

    !!! example ""
        `2` by default

4. Number of retries to load the generated image

    !!! example ""
        `2` by default

### Operation Delays

=== "`recurring` mode"
    ```typescript
    OperationDelay {
      mode: recurring // (1)!
      delay: Double // (2)!
      repeat: Int // (3)!
    }
    ```

    1. `recurring` delay will be repeated a specified `repeat` number of times. 

    2. Delay in __seconds__ before next request the operation status.

    3. Number of repeates for the `recurring` delay. 

=== "`infinite` mode"
    ```typescript
    OperationDelay {
      mode: infinite // (1)!
      delay: Double // (2)!
    }
    ```

    1. `infinite` delay will repeat infinitely.

    2. Delay in __seconds__ before next request the operation status.

!!! warning "Timeout error"
    If the sequence does not contain a value with an `infinite` mode and ends before a successful result is obtained, the operation will fail with a timeout error, the user will be shown a "something went wrong" error.
