---
template: scheme.html
hide:
  - toc
code_links:
  Callback: /sdk/developer/definitions/#callback
  String: /sdk/developer/definitions/#string
---
# Cart

Configuration for cart-related functionality in the TryOn interface.

## [:material-arrow-up-left:](index.md#try-on-feature) TryOnCartFeature
```typescript
TryOnCartFeature {
  strings {
    addToCart: String // (1)!
  }

  handler {
    addToCartAction: Callback(String) // (2)!
  }
}
```

1.  Label text for the button that adds the current product to the cart.
2.  Callback function that handles adding a product to the cart using its identifier.
