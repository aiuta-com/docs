## Import

```swift
import AiutaSDK
```

## Configure

For quick test purposes you can use test `apiKey`

```swift
await Aiuta.setup(configuration: .debug(auth: .apiKey("{{ aiuta.api.demo_key }}")))
```

## Start TryOn

You can use one of the following product examples that will work with the test `apiKey`

=== "Product 1"
    ```swift
    let testProduct = Aiuta.Product(
        id: "{{ test_product(0).sku_id }}",
        title: "{{ test_product(0).title }}",
        imageUrls: {{ dumps(test_product(0).image_urls) | indent(8) }})
    await Aiuta.tryOn(product: testProduct)
    ```

    {{ md_images(test_product(0).image_urls) | indent(4) }}

=== "Product 2"
    ```swift
    let testProduct = Aiuta.Product(
        id: "{{ test_product(1).sku_id }}",
        title: "{{ test_product(1).title }}",
        imageUrls: {{ dumps(test_product(1).image_urls) | indent(8) }})
    await Aiuta.tryOn(product: testProduct)
    ```

    {{ md_images(test_product(1).image_urls) | indent(4) }}


=== "Product 3"
    ```swift
    let testProduct = Aiuta.Product(
        id: "{{ test_product(2).sku_id }}",
        title: "{{ test_product(2).title }}",
        imageUrls: {{ dumps(test_product(2).image_urls) | indent(8) }})
    await Aiuta.tryOn(product: testProduct)
    ```

    {{ md_images(test_product(2).image_urls) | indent(4) }}

## Show History

```swift
await Aiuta.showHistory()
```
