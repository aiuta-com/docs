---
template: scheme.html
hide:
  - toc
code_links:
  String: /sdk/developer/definitions/#string
---
# [:material-arrow-up-left:](index.md#try-on) Input Image Validation

![Input Image Validation](/media/pages/loading-invalid.png){ width=220 }

Configuration for validating input images before processing.
```typescript
TryOnInputImageValidationFeature {
  strings {
    invalidInputImageDescription: String // (1)!
    invalidInputImageChangePhotoButton: String // (2)!
  }
}
```

1.  Message displayed to users when their uploaded image fails validation.
2.  Label text for the button that allows users to select a different photo.
