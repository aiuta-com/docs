---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  String: /sdk/developer/definitions/#string
---
# Camera

Configuration for camera functionality, allowing users to take new photos directly within the SDK.

## [:material-arrow-up-left:](index.md#image-picker-feature) ImagePickerCameraFeature
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
