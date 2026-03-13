---
template: scheme.html
hide:
  - toc
code_links:
  TryOnCartOutfitFeature: "#cart-outfit"
  Callback: /sdk/developer/definitions/#callback
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](index.md#try-on) Cart

![Cart](/media/pages/results-cart.png){ width=220 }

Configuration for adding products to the cart from the TryOn results screen.
```typescript
TryOnCartFeature {
  outfit: TryOnCartOutfitFeature | null // (1)!

  strings {
    addToCart: String // (2)!
  }

  handler {
    addToCartAction: Callback(String) // (3)!
  }
}
```

1.  [:material-arrow-down-left:](#cart-outfit) Optional configuration for adding all items from a multi-item try-on outfit to the cart at once ("Shop the Look").
2.  Label text for the button that adds the current product to the cart.
3.  Callback function that handles adding a product to the cart using its identifier.

### [:material-arrow-up-left:](#tryoncartfeature) Cart Outfit

Configuration for outfit/multi-item cart functionality. Enables a "Shop the Look" button that adds all products from the current outfit to the cart at once. Only applicable when using multi-item try-on.
```typescript
TryOnCartOutfitFeature {
  strings {
    addToCartOutfit: String // (1)!
  }

  handler {
    addToCartOutfitAction: Callback(List<String>) // (2)!
  }
}
```

1.  Label text for the "Shop the Look" button that adds all outfit products to the cart.
2.  Callback function that handles adding multiple products from an outfit to the cart.
