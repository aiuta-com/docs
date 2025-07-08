---
hide:
  - toc
---
# Product Bar Scheme

Product information display, including typography for product details and optional price styling.
 
![component](/media/components/product-bar.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Product Bar

```typescript
ProductBarTheme {
  prices: ProductBarPricesTheme | null // (1)!
  typography {
    product: TextStyle // (2)!
    brand: TextStyle // (3)!
  }

  icons {
    arrow16: Icon // (4)!
  }

  settings {
    applyProductFirstImageExtraPadding: Bool // (5)!
  }
}

ProductBarPricesTheme {
  typography {
    price: TextStyle // (6)!
  }

  colors {
    discountedPrice: Color // (7)!
  }
}
```

1. Configures the price display settings for the product bar, including typography and colors for price elements.
2. Defines the text style for product names in the product bar.
3. Specifies the text style for brand names displayed in the product bar.
4. Sets the icon used to indicate expandable product details in the compact view.
5. Controls whether additional padding is applied to the first product image in the list.
6. Configures the text style specifically for price displays in the product bar.
7. Defines the color used to highlight discounted prices in the product bar. 