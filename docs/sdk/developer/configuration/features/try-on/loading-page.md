---
template: scheme.html
hide:
  - toc
code_links:
  Color: /sdk/developer/definitions/#color
  ComponentStyle: /sdk/developer/definitions/#componentstyle
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](index.md#try-on-feature) Loading Page

![Loading Page](/media/pages/loading-screen.png){ width=220 }

Configuration for the loading page displayed during the TryOn process.
```typescript
TryOnLoadingPageFeature {
  strings {
    tryOnLoadingStatusUploadingImage: String // (1)!
    tryOnLoadingStatusScanningBody: String // (2)!
    tryOnLoadingStatusGeneratingOutfit: String // (3)!
  }

  styles {
    loadingStatusBackgroundGradient: List<Color> | null // (4)!
    loadingStatusStyle: ComponentStyle // (5)!
  }
}
```

1.  Text displayed while uploading the user's image to the server.
2.  Text displayed while scanning and analyzing the body in the image.
3.  Text displayed while generating the virtual try-on outfit.
4.  Optional gradient colors for the loading status background.
5.  Visual style for the loading status indicator, either primary (solid) or blurred (with optional outline).
