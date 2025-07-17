---
hide:
  - toc
---
# Product Scheme

The product scheme defines the structure and properties of products within the Aiuta platform. This scheme is essential for displaying product information in the SDK's user interface and managing product-related functionality.

## Product

```typescript
Product {
  id: String // (1)!
  title: String // (2)!
  brand: String // (3)!
  imageUrls: List<String> // (4)!
  price: Price | null // (5)!
}
```

1.  Unique identifier for the product, used to distinguish it across the platform. Must match the identifiers provided to Aiuta for training try-on models.
2.  The name or title of the product, displayed prominently in the user interface.
3.  The brand associated with the product, identifying the manufacturer or provider.
4.  Collection of URLs pointing to product images. Should contain at least one URL.

    !!! warning "Extra padding for the flat lay image"
        The flat lay image in case of cropping without margins should be the __first__ in the `imageUrls` list if [`ProductBarTheme`](/sdk/developer/configuration/ui/theme/product-bar.md) `applyProductFirstImageExtraPadding` set to `true`

5.  Optional pricing details for the product, including current and old prices.

### Price

```typescript
Price {
  current: String // (1)!
  old: String | null // (2)!
}
```

1.  Current price of the product, formatted as a localized string including currency symbol and amount.
2.  Optional old price of the product, formatted as a localized string. If provided, will be displayed as strikethrough near the current price.

!!! info "Prices Theme"
    You only need to pass product prices if you set up [`PricesTheme`](/sdk/developer/configuration/ui/theme/product-bar.md#prices)
