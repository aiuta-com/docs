---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  String: /sdk/developer/definitions/#string
---
# [:material-arrow-up-left:](index.md#image-picker) Photo Gallery

Configuration for accessing and selecting images from the device's photo library.
```typescript
ImagePickerPhotoGalleryFeature {
  icons {
    gallery24: Icon // (1)!
  }

  strings {
    galleryButtonSelectPhoto: String // (2)!
  }
}
```

1.  Icon displayed for the gallery button in the bottom sheet list.
2.  Label text for the button used to select a photo from the gallery.
