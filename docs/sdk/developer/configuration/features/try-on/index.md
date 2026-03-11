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
---
# Try On Scheme

Configures the core virtual try-on functionality for trying products virtually.

![Loading Screen](/media/pages/loading-screen.png){width=120}
![Results Screen](/media/pages/results.png){width=120}

## [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Try On Feature

```typescript
TryOnFeature {
  tryOn {
    loadingPage: TryOnLoadingPageFeature // (1)!
    inputImageValidation: TryOnInputImageValidationFeature // (2)!
    cart: TryOnCartFeature // (3)!
    fitDisclaimer: TryOnFitDisclaimerFeature | null // (4)!
    feedback: TryOnFeedbackFeature | null // (5)!
    generationsHistory: TryOnGenerationsHistoryFeature | null // (6)!
    otherPhoto: TryOnWithOtherPhotoFeature | null // (7)!

    settings {
      isBackgroundExecutionAllowed: Bool // (8)!
      tryGeneratePersonSegmentation: Bool // (9)!
    }

    icons {
      tryOn20: Icon // (10)!
    }

    strings {
      tryOnPageTitle: String // (11)!
      tryOn: String // (12)!
    }

    styles {
      tryOnButtonGradient: List<Color> | null // (13)!
    }
  }
}
```

1.  [:material-subdirectory-arrow-right:](loading-page.md) Configuration for the loading page displayed during the TryOn process.
2.  [:material-subdirectory-arrow-right:](input-image-validation.md) Configuration for validating input images before processing.
3.  [:material-subdirectory-arrow-right:](cart.md) Configuration for cart-related functionality in the TryOn interface.
4.  [:material-subdirectory-arrow-right:](fit-disclaimer.md) Optional configuration for displaying fit disclaimers to users.
5.  [:material-subdirectory-arrow-right:](feedback.md) Optional configuration for collecting user feedback on TryOn results.
6.  [:material-subdirectory-arrow-right:](generations-history.md) Optional configuration for managing the history of generated TryOn results.
7.  [:material-subdirectory-arrow-right:](other-photo.md) Optional configuration for allowing users to continue with a different photo.
8.  Determines whether the SDK should wait for the generation results in the background when closed.
9.  Enables local person segmentation highlighting during loading on iOS 15+.
10.  Icon displayed for the TryOn magic button in the interface.
11.  Title text displayed at the top of the TryOn page.
12.  Label text used for the "Try On" buttons throughout the interface.
13.  Optional gradient colors for styling the TryOn button.

## Sequence diagram

{% include-markdown "sdk/templates/diagrams/try-on.md" %}
