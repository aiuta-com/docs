---
hide:
  - toc
---
# Image Scheme

Shapes, sizes, and error state icon for image views.

![component](/media/components/images.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Image

```typescript
ImageTheme {
  shapes {
    imageL: Shape // (1)!
    imageS: Shape // (2)!
  }

  icons {
    imageError36: Icon // (3)!
  }
}

```

1. Defines the shape configuration for large image views, allowing customization of the visual appearance for prominent images.
2. Specifies the shape configuration for small image views, enabling consistent styling for secondary or thumbnail images.
3. Sets the icon to be displayed when an image fails to load, providing visual feedback for error states. 