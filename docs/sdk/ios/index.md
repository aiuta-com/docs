# iOS SDK

```swift
import AiutaSDK

await Aiuta.setup(.debug(auth: .apiKey(" {{ demo_api_key }}")))

let testProduct = Aiuta.Product(
    id: "{{ test_product(0).sku_id }}",
    title: "{{ test_product(0).title }}",
    imageUrls: {{ dumps(test_product(0).image_urls) }})
await Aiuta.tryOn(product: testProduct)
```
    
## Requirements

{% include-markdown "sdk/templates/ios/requirements.md" %}
