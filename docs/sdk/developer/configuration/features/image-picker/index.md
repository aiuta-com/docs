---
hide:
  - toc
code_links:
  ImagePickerCameraFeature: camera/
  ImagePickerPhotoGalleryFeature: photo-gallery/
  ImagePickerPredefinedModelFeature: predefined-models/
  ImagePickerUploadsHistoryFeature: uploads-history/
  ImagePickerProtectionDisclaimerFeature: protection-disclaimer/
  Image: /sdk/developer/definitions/#image
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Image Picker
![Image Picker](/media/pages/image-picker-w-models.png){ width=220 }
![Image Picker](/media/pages/image-picker-bottom-sheet.png){ width=220 }
![Image Picker](/media/pages/image-picker-history-last.png){ width=220 }

Controls [:material-window-open: the image selection interface](/sdk/about/pages/image-picker.md), allowing users to pick photos, take new ones, use predefined models, or access previous uploads.

```typescript
ImagePickerFeature {
  camera: ImagePickerCameraFeature | null // (1)!
  photoGallery: ImagePickerPhotoGalleryFeature // (2)!
  predefinedModels: ImagePickerPredefinedModelFeature | null // (3)!
  protectionDisclaimer: ImagePickerProtectionDisclaimerFeature | null // (4)!
  uploadsHistory: ImagePickerUploadsHistoryFeature | null // (5)!

  images {
    examples: List<Image> // (6)!
  }

  strings {
    imagePickerTitleEmpty: String // (7)!
    imagePickerDescriptionEmpty: String // (8)!
    imagePickerButtonUploadImage: String // (9)!
  }
}
```

1.  [:material-arrow-down-left:](camera.md) Configuration for camera functionality, allowing users to take new photos directly within the SDK.
2.  [:material-arrow-down-left:](photo-gallery.md) Configuration for accessing and selecting images from the device's photo library.
3.  [:material-arrow-down-left:](predefined-models.md) Configuration for using predefined model images as an alternative to user photos.
4.  [:material-arrow-down-left:](protection-disclaimer.md) Optional disclaimer informing users about photo privacy and protection.
5.  [:material-arrow-down-left:](uploads-history.md) Configuration for managing and reusing previously uploaded images.
6.  List of exactly 2 example of input images to display in the image picker interface.
7.  Title text displayed above images when the image picker is empty.
8.  Description text shown when the image picker is empty.
9.  Label text for the button used to upload new photos.

## Sequence Diagrams

=== "Default configuration"

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-default.md" %}

=== "Custom configuration"

    {% include-markdown "sdk/templates/diagrams/pick-a-photo-custom.md" %}
