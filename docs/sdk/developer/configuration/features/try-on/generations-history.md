---
hide:
  - toc
code_links:
  BuiltIn: /sdk/developer/definitions/#dataprovider
  Custom: /sdk/developer/definitions/#dataprovider
  Callback: /sdk/developer/definitions/#callback
  Icon: /sdk/developer/definitions/#icon
  List: /sdk/developer/definitions/#list
  Observable: /sdk/developer/definitions/#observable
  String: /sdk/developer/definitions/#string
  GeneratedImage: "#generated-image"
  OwnerType: "#owner-type"
---
# [:material-arrow-up-left:](index.md#try-on) Generations History

Optional configuration for managing the history of generated TryOn results.
```typescript
TryOnGenerationsHistoryFeature {
  icons {
    history24: Icon // (1)!
  }

  strings {
    generationsHistoryPageTitle: String // (2)!
  }

  dataProvider: BuiltIn | Custom {
    generatedImages: Observable<List<GeneratedImage>> // (3)!
    addGeneratedImages: Callback(List<GeneratedImage>) // (4)!
    deleteGeneratedImages: Callback(List<GeneratedImage>) // (5)!
  }
}
```

1.  Icon displayed for the History button in the page bar.
2.  Title text displayed at the top of the generations history page.
3.  Observable collection of previously generated try-on images.
4.  Callback function to add new generated images to the history.
5.  Callback function to remove images from the generations history.

---

#### Generated Image

```typescript
GeneratedImage {
    id: String // (1)!
    url: String // (2)!
    ownerType: OwnerType // (3)!
    productIds: List<String> // (4)!
}
```

1.  A unique string identifier assigned to the image by the Aiuta API, ensuring each image can be distinctly recognized and referenced within the system.
2.  The URL pointing to the location of the image resource, which can be accessed and retrieved by the SDK to present in the UI.
3.  The type of the image [owner :octicons-arrow-down-24:](#owner-type).
4.  A list of product identifiers that were utilized during the image generation process. Each identifier corresponds to a specific product involved in the try-on session, allowing for precise tracking and reference within the system.

Generated images represent the results of try-on sessions. These images are generated based on either a photo uploaded by the user or a predefined model image provided by Aiuta.

##### Owner Type

{% include-markdown "sdk/templates/developer/owner-type.md" %}
