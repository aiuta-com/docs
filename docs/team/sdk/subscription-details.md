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

PoweredBySticker {
  urlIos: String | null // (4)!
  urlAndroid: String | null // (5)!
  isVisible: true | false | null // (6)!
}

RetryCounts {
  photoUpload: Int | null // (7)!
  operationStart: Int | null // (8)!
  operationStatus: Int | null // (9)!
  resultDownload: Int | null // (10)!
}

OperationDelay {
  mode: recurring | infinite // (11)!
  delay: Double // (12)!
  repeat: Int // (13)!
}
```

1. Controls the behavior of the [“Powered by Aiuta” label](../../sdk/about/developer/user-interface.md#powered-by) that may be present on some SDK screens (e.g. the progress animation screen).

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

3. Sequence of delays before requesting the generation operation status. If the sequence does not contain an `infinite` value and ends before a successful result is obtained, the operation will fail with a timeout error, the user will be shown a "something went wrong" error.

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

4. URL for iOS to open by click on the "powered by" label. If not specified the label interaction is disabled.

    !!! example ""
        Default is `null` and "powered by" label is not interactive.

5. URL for Android to open by click on the "powered by" label. If not specified the label interaction is disabled.

    !!! example ""
        Default is `null` and "powered by" label is not interactive.

6. The only value to "powered by" label be visible is explicit `true` in the subscription details. In any other case "powered by" is hidden.

    !!! example ""
        Default is `false` and "powered by" label is hidden.

7. Number of retries for photo preparation/compressing/uploading.

    !!! example ""
        `2` by default

8. Number of network request retries, has no effect if the server responds with error.

    !!! example ""
        `0` by default

9. Number of network request retries per loop, if the server responded, the number of retries will reset in the next loop after the delay in the `operationDelaysSequence`

    !!! example ""
        `2` by default

10. Number of retries to load the generated image

    !!! example ""
        `2` by default

11. `recurring` delay will be repeated a specified `repeat` number of times, `infinite` delay will repeat infinitely. If the sequence does not contain an `infinite` value and ends before a successful result is obtained, the operation will fail with a timeout error, the user will be shown a "something went wrong" error.

12. Delay in __seconds__ before next request the operation status.

13. Number of repeates for the `recurring` delay. 

    !!! note ""
        This field is not applicable to delay with `infinite` mode.

