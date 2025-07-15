---
hide:
  - toc
---
# Wishlist Scheme

Integrates with the host app's wishlist functionality for product management.

## [:material-arrow-up-left:](/sdk/developer/configuration/features/#features) Wishlist Feature
```typescript
WishlistFeature {
  icons {
    wishlist24: Icon // (1)!
    wishlistFill24: Icon // (2)!
  }

  strings {
    wishlistButtonAdd: String // (3)!
  }
  
  dataProvider {
    wishlistProductIds: Observable<List<String>> // (4)!
    setProductInWishlist: Callback(productId: String, inWishlist: Bool) // (5)!
  }
}
```

1.  Icon displayed for the Wishlist button in its default state.
2.  Icon displayed for the Wishlist button when the product is in the wishlist.
3.  Label text for the "Add to Wishlist" button.
4.  Observable collection of product IDs currently in the wishlist.
5.  Callback function to add or remove a product from the wishlist. 


### Sequence Diagram

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation

    USR->>SDK: Tap Wishlist button
    SDK->>APP: Toggle setProductInWishlist (product ID)
    APP->>BE: Update wishlist
    APP-->>SDK: Update observable wishlistProductIds
    SDK->>SDK: Update wishlist button state

```