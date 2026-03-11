---
template: scheme.html
hide:
  - toc
code_links:
  ImagePickerCameraFeature: camera/
  ImagePickerPhotoGalleryFeature: photo-gallery/
  ImagePickerPredefinedModelFeature: predefined-models/
  ImagePickerUploadsHistoryFeature: uploads-history/
  Image: /sdk/developer/definitions/#image
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
---
# Image Picker Scheme

Controls [:material-window-open: the image selection interface](/sdk/about/pages/image-picker.md), allowing users to pick photos, take new ones, use predefined models, or access previous uploads.

![Image Picker](/media/pages/image-picker-w-models.png){width=120}
![Image Picker](/media/pages/image-picker-bottom-sheet.png){width=120}
![Image Picker](/media/pages/image-picker-history-last.png){width=120}

## [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Image Picker Feature

```typescript
ImagePickerFeature {
  camera: ImagePickerCameraFeature | null // (1)!
  photoGallery: ImagePickerPhotoGalleryFeature // (2)!
  predefinedModels: ImagePickerPredefinedModelFeature | null // (3)!
  uploadsHistory: ImagePickerUploadsHistoryFeature | null // (4)!

  images {
    examples: List<Image> // (5)!
  }

  strings {
    imagePickerTitleEmpty: String // (6)!
    imagePickerDescriptionEmpty: String // (7)!
    imagePickerButtonUploadImage: String // (8)!
  }
}
```

1.  [:material-subdirectory-arrow-right:](camera.md) Configuration for camera functionality, allowing users to take new photos directly within the SDK.
2.  [:material-subdirectory-arrow-right:](photo-gallery.md) Configuration for accessing and selecting images from the device's photo library.
3.  [:material-subdirectory-arrow-right:](predefined-models.md) Configuration for using predefined model images as an alternative to user photos.
4.  [:material-subdirectory-arrow-right:](uploads-history.md) Configuration for managing and reusing previously uploaded images.
5.  List of exactly 2 example of input images to display in the image picker interface.
6.  Title text displayed above images when the image picker is empty.
7.  Description text shown when the image picker is empty.
8.  Label text for the button used to upload new photos.

## Sequence Diagrams

=== "Default configuration"

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-default.md" %}

=== "Custom configuration"

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-custom.md" %}
