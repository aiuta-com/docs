---
template: scheme.html
hide:
  - toc
code_links:
  TryOnLoadingPageFeature: loading-page/
  TryOnInputImageValidationFeature: input-image-validation/
  TryOnCartFeature: cart/
  TryOnFitDisclaimerFeature: fit-disclaimer/
  TryOnFeedbackFeature: feedback/
  TryOnGenerationsHistoryFeature: generations-history/
  TryOnWithOtherPhotoFeature: other-photo/
  Color: /sdk/developer/definitions/#color
  Icon: /sdk/developer/definitions/#icon
  List: /sdk/developer/definitions/#list
  Bool: /sdk/developer/definitions/#bool
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Try On
![Loading Screen](/media/pages/loading-screen.png){ width=220 }
![Results Screen](/media/pages/results.png){ width=220 }

Configures the core virtual try-on functionality for trying products virtually.

```typescript
TryOnFeature {
  loadingPage: TryOnLoadingPageFeature // (1)!
  inputImageValidation: TryOnInputImageValidationFeature // (2)!
  cart: TryOnCartFeature // (3)!
  fitDisclaimer: TryOnFitDisclaimerFeature | null // (4)!
  feedback: TryOnFeedbackFeature | null // (5)!
  generationsHistory: TryOnGenerationsHistoryFeature | null // (6)!
  otherPhoto: TryOnWithOtherPhotoFeature | null // (7)!

  icons {
    tryOn20: Icon // (8)!
  }

  styles {
    tryOnButtonGradient: List<Color> | null // (9)!
  }

  strings {
    tryOnPageTitle: String // (10)!
    tryOn: String // (11)!
  }

  settings {
    isBackgroundExecutionAllowed: Bool // (12)!
    tryGeneratePersonSegmentation: Bool // (13)!
  }
}
```

1.  [:material-arrow-down-left:](loading-page.md) Configuration for the loading page displayed during the TryOn process.
2.  [:material-arrow-down-left:](input-image-validation.md) Configuration for validating input images before processing.
3.  [:material-arrow-down-left:](cart.md) Configuration for cart-related functionality in the TryOn interface.
4.  [:material-arrow-down-left:](fit-disclaimer.md) Optional configuration for displaying fit disclaimers to users.
5.  [:material-arrow-down-left:](feedback.md) Optional configuration for collecting user feedback on TryOn results.
6.  [:material-arrow-down-left:](generations-history.md) Optional configuration for managing the history of generated TryOn results.
7.  [:material-arrow-down-left:](other-photo.md) Optional configuration for allowing users to continue with a different photo.
8.  Icon displayed for the TryOn magic button in the interface.
9.  Optional gradient colors for styling the TryOn button.
10.  Title text displayed at the top of the TryOn page.
11.  Label text used for the "Try On" buttons throughout the interface.
12.  Determines whether the SDK should wait for the generation results in the background when closed.
13.  Enables local person segmentation highlighting during loading on iOS 15+.

## Sequence diagram

{% include-markdown "sdk/templates/diagrams/try-on.md" %}
