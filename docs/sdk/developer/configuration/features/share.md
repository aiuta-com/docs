---
hide:
  - toc
---
# Share Scheme

Enables sharing capabilities for generated try-on images with customizable options.

## [:material-arrow-up-left:](/sdk/developer/configuration/features/#features) Share Feature
```typescript
ShareFeature {
  watermark: ShareWatermarkFeature | null // (1)!

  icons {
    share24: Icon // (2)!
  }

  strings {
    shareButton: String // (3)!
  }

  dataProvider: null | Custom {
    getShareText: Callback(productIds: List<String>) => String // (4)!
  }
}

```

1.  [:material-arrow-down-left:](#watermark) Optional configuration for adding a watermark to shared content.
2.  Icon displayed for the share button in the interface.
3.  Label text for the share button in the fullscreen gallery.
4.  Optional `dataProvider` callback function that generates additional text to be shared along with the image.


### [:material-arrow-up-left:](#share) Watermark
```typescript
ShareWatermarkFeature {
  images {
    logo: Image // (1)!
  }
}
```

1.  Logo image to be used as a watermark on shared content. 


### Sequence Diagram

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation

    USR->>SDK: Tap Share button
    opt Watermark
      SDK->>SDK: Draw logo on the image(s)
    end
    SDK->>APP: Call getShareText (product IDs)
    APP-->>SDK: Return share text
    SDK-->>USR: Show system share dialog
    Note over SDK,USR: Generated image and optional text to share
    USR->>SDK: Complete sharing

```