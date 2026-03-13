---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  Shape: /sdk/developer/definitions/#shape
---
# [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/index.md#theme) Image
![component](/media/components/images.png){ width=300 }

Shapes, sizes, and error state icon for image views.

```typescript
ImageTheme {
  shapes {
    imageL: Shape // (1)!
    imageM: Shape // (2)!
    imageS: Shape // (3)!
  }

  icons {
    imageError36: Icon // (4)!
  }
}

```

1. Defines the shape configuration for large image views, allowing customization of the visual appearance for prominent images.
2. Sets the shape configuration for medium image views, used for standard content images.
3. Specifies the shape configuration for small image views, enabling consistent styling for secondary or thumbnail images.
4. Sets the icon to be displayed when an image fails to load, providing visual feedback for error states.