---
hide:
  - toc
---
# Button Scheme

Buttons styles, including typography and shape configurations for different button sizes.

![component](/media/components/button-brand.png){ width=130 } ![component](/media/components/button-contrast-inverted.png){ width=150 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Button

```typescript
ButtonTheme {
  typography {
    buttonM: TextStyle // (1)!
    buttonS: TextStyle // (2)!
  }

  shapes {
    buttonM: Shape // (3)!
    buttonS: Shape // (4)!
  }
}

```

1. Defines the text style for a regular medium-sized buttons.
2. Specifies the text style for small buttons.
3. Sets the shape configuration for medium buttons.
4. Configures the shape for small buttons. 