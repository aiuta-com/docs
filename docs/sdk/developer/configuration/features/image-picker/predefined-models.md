---
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  Map: /sdk/developer/definitions/#map
  String: /sdk/developer/definitions/#string
---
# [:material-arrow-up-left:](index.md#image-picker) Predefined Models

![Predefined Models](/media/pages/image-picker-models.png){ width=220 }

Configuration for using predefined model images as an alternative to user photos.
```typescript
ImagePickerPredefinedModelFeature {
  icons {
    selectModels24: Icon // (1)!
  }

  data {
    preferredCategoryId: String // (2)!
  }

  strings {
    predefinedModelsPageTitle: String // (3)!
    predefinedModelsOr: String // (4)!
    predefinedModelsErrorEmptyModelsList: String // (5)!
    predefinedModelsCategories: Map<String, String> // (6)!
  }
}
```

1.  Icon displayed for the predefined models button in the bottom sheet list.
2.  Identifier of the preferred category to show by default when user opens models page.
3.  Title text for the predefined models page and button in the bottom sheet list.
4.  Label text displayed before the predefined models button in the image picker.
5.  Error message shown when the list of predefined models is empty.
6.  Mapping of category identifiers to their display titles, typically covering `man` and `woman` categories.
