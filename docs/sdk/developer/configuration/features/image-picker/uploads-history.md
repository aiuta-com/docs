---
template: scheme.html
hide:
  - toc
code_links:
  Callback: /sdk/developer/definitions/#callback
  ComponentStyle: /sdk/developer/definitions/#componentstyle
  List: /sdk/developer/definitions/#list
  Observable: /sdk/developer/definitions/#observable
  String: /sdk/developer/definitions/#string
  InputImage: "#input-image"
  OwnerType: "#owner-type"
---
# [:material-arrow-up-left:](index.md#image-picker-feature) Uploads History

![Uploads History](/media/pages/image-picker-history.png){ width=220 }

Configuration for managing and reusing previously uploaded images.
```typescript
ImagePickerUploadsHistoryFeature {
  strings {
    uploadsHistoryButtonNewPhoto: String // (1)!
    uploadsHistoryTitle: String // (2)!
    uploadsHistoryButtonChangePhoto: String // (3)!
  }

  styles {
    changePhotoButtonStyle: ComponentStyle // (4)!
  }

  dataProvider: BuiltIn | Custom {
    uploadedImages: Observable<List<InputImage>> // (5)!
    addUploadedImages: Callback(List<InputImage>) // (6)!
    deleteUploadedImages: Callback(List<InputImage>) // (7)!
    selectUploadedImage: Callback(InputImage) // (8)!
  }
}
```

1.  Text label for the button to upload a new photo.
2.  Title text displayed at the top of the uploads history bottom sheet.
3.  Text label for the button to change the currently selected photo.
4.  Visual style for the change photo button, either primary (solid) or blurred (with optional outline).
5.  Observable collection of images previously uploaded by the user, with most recent first.
6.  Callback to add new images to the uploads history.
7.  Callback to remove images from the uploads history.
8.  Callback to move a selected image to the top of the history when reused.

---

#### Input Image

```typescript
InputImage {
    id: String // (1)!
    url: String // (2)!
    ownerType: OwnerType // (3)!
}
```

1.  A unique string identifier assigned to the image by the Aiuta API, ensuring each image can be distinctly recognized and referenced within the system.
2.  The URL pointing to the location of the image resource, which can be accessed and retrieved by the SDK to present in the UI.
3.  The type of the image [owner :octicons-arrow-down-24:](#owner-type).

Input images used in the Aiuta SDK for try-on sessions can either be uploaded by users, such as photos taken with their camera or selected from their gallery, or they can be predefined model images provided by Aiuta.

##### Owner Type

{% include-markdown "sdk/templates/developer/owner-type.md" %}
