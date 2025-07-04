# SDK Analytics

## API Endpoint

```
{% include-markdown "api/templates/endpoint-analytics.md" %}
```

## Event Scheme

``` typescript
{
  data {
    type: String // (1)!
    event: String | null // (2)!
    pageId: String | null // (3)!
    productIds: List<String> | null // (4)!
    parameter1...N: Any | null // (5)!
  }

  env {
    platform: ios | android | web
    sdkVersion: String
    hostId: String // (6)!
    hostVersion: String | null // (7)!
    installationId: String // (8)!
  }
  
  localDateTime: String // (9)!
}
```

1. Primary event type
2. Some events of [public type](../../sdk/about/analytics/analytics.md#event-types) may contain a detailed field, indicating which specific `event` of this `type` occurred
3. Events of [public type](../../sdk/about/analytics/analytics.md#event-types) are always linked to some [page](../../sdk/about/analytics/analytics.md#page-identifiers)
4. Current active [priduct/sku ids](../../sdk/about/analytics/analytics.md#products-identifiers)
5. Any other additional event parameter in the flattened structure
6. Host Android application id / iOS bundle id
7. Host application version if possible
8. UUID of installation written in the SDK local storage generated and saved if it does not exist there
9. ISO-8601 date time string when the event occurred on the device

## Event Types

!!! doc "See all [events tracked](../../sdk/about/analytics/analytics.md#event-types)"
