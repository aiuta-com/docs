# Image Picker Scheme

Controls the image selection interface, allowing users to pick photos, take new ones, use predefined models, or access previous uploads.

## [:material-arrow-up-left:](/sdk/developer/configuration/features/#features) Image Picker Feature

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

1.  [:material-arrow-down-left:](#camera) Configuration for camera functionality, allowing users to take new photos directly within the SDK.
2.  [:material-arrow-down-left:](#photo-gallery) Configuration for accessing and selecting images from the device's photo library.
3.  [:material-arrow-down-left:](#predefined-models) Configuration for using predefined model images as an alternative to user photos.
4.  [:material-arrow-down-left:](#uploads-history) Configuration for managing and reusing previously uploaded images.
5.  List of exactly 2 example of input images to display in the image picker interface.
6.  Title text displayed above images when the image picker is empty.
7.  Description text shown when the image picker is empty.
8.  Label text for the button used to upload new photos.



### [:material-arrow-up-left:](#image-picker-feature) Camera
```typescript
ImagePickerCameraFeature {
  icons {
    camera24: Icon // (1)!
  }

  strings {
    cameraButtonTakePhoto: String // (2)!
    cameraPermissionTitle: String // (3)!
    cameraPermissionDescription: String // (4)!
    cameraPermissionButtonOpenSettings: String // (5)!
  }
}
```

1.  Icon displayed for the camera button in the bottom sheet list.
2.  Label text for the button used to take a photo.
3.  Title text displayed in the alert when camera permissions are denied.
4.  Description text shown in the alert when camera permissions are denied.
5.  Label text for the button that opens app settings to change camera permissions.



### [:material-arrow-up-left:](#image-picker-feature) Photo Gallery
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



### [:material-arrow-up-left:](#image-picker-feature) Predefined Models
```typescript
ImagePickerPredefinedModelFeature {
  icons {
    selectModels24: Icon // (1)!
  }

  data {
    preferredCategoryId: String // (2)!
  }

  strings {
    predefinedModelPageTitle: String // (3)!
    predefinedModelOr: String // (4)!
    predefinedModelErrorEmptyModelsList: String // (5)!
    predefinedModelCategories: Map<String, String> // (6)!
  }
}
```

1.  Icon displayed for the predefined models button in the bottom sheet list.
2.  Identifier of the preferred category to show by default when user opens models page.
3.  Title text for the predefined models page and button in the bottom sheet list.
4.  Label text displayed before the predefined models button in the image picker.
5.  Error message shown when the list of predefined models is empty.
6.  Mapping of category identifiers to their display titles, typically covering `man` and `woman` categories.



### [:material-arrow-up-left:](#image-picker-feature) Uploads History
```typescript
ImagePickerUploadsHistoryFeature {
  strings {
    uploadsHistoryButtonNewPhoto: String // (1)!
    uploadsHistoryTitle: String // (2)!
    uploadsHistoryButtonChangePhoto: String // (3)!
  }

  styles {
    changePhotoButtonStyle: primary | blurred // (4)!
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
    
    !!! warning ""
        Please refer to this section in case of using custom [`dataProvider` for the uploads history](configuration.md#uploads-history)

Input images used in the Aiuta SDK for try-on sessions can either be uploaded by users, such as photos taken with their camera or selected from their gallery, or they can be predefined model images provided by Aiuta.

##### Owner Type

{% include-markdown "sdk/templates/developer/owner-type.md" %}
