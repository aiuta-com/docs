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

1.  [:material-arrow-down-left:](#loading-page) Configuration for the loading page displayed during the TryOn process.
2.  [:material-arrow-down-left:](#input-image-validation) Configuration for validating input images before processing.
3.  [:material-arrow-down-left:](#cart) Configuration for cart-related functionality in the TryOn interface.
4.  [:material-arrow-down-left:](#fit-disclaimer) Optional configuration for displaying fit disclaimers to users.
5.  [:material-arrow-down-left:](#feedback) Optional configuration for collecting user feedback on TryOn results.
6.  [:material-arrow-down-left:](#generations-history) Optional configuration for managing the history of generated TryOn results.
7.  [:material-arrow-down-left:](#other-photo) Optional configuration for allowing users to continue with a different photo.
8.  Determines whether the SDK should wait for the generation results in the background when closed.
9.  Enables local person segmentation highlighting during loading on iOS 15+.
10.  Icon displayed for the TryOn magic button in the interface.
11.  Title text displayed at the top of the TryOn page.
12.  Label text used for the "Try On" buttons throughout the interface.
13.  Optional gradient colors for styling the TryOn button.


## Sequence diagram

{% include-markdown "sdk/templates/diagrams/try-on.md" %}

## Sub Features

---

### [:material-arrow-up-left:](#try-on-feature) Loading Page
```typescript
TryOnLoadingPageFeature {
  strings {
    tryOnLoadingStatusUploadingImage: String // (1)!
    tryOnLoadingStatusScanningBody: String // (2)!
    tryOnLoadingStatusGeneratingOutfit: String // (3)!
  }

  styles {
    loadingStatusBackgroundGradient: List<Color> | null // (4)!
    loadingStatusStyle: primary | blurred | blurredWithOutline // (5)!
  }
}
```

1.  Text displayed while uploading the user's image to the server.
2.  Text displayed while scanning and analyzing the body in the image.
3.  Text displayed while generating the virtual try-on outfit.
4.  Optional gradient colors for the loading status background.
5.  Visual style for the loading status indicator, either primary (solid) or blurred (with optional outline).


### [:material-arrow-up-left:](#try-on-feature) Input Image Validation
```typescript
TryOnInputImageValidationFeature {
  strings {
    invalidInputImageDescription: String // (1)!
    invalidInputImageChangePhotoButton: String // (2)!
  }
}
```

1.  Message displayed to users when their uploaded image fails validation.
2.  Label text for the button that allows users to select a different photo.



### [:material-arrow-up-left:](#try-on-feature) Cart
```typescript
TryOnCartFeature {
  strings {
    addToCart: String // (1)!
  }

  handler {
    addToCartAction: Callback(String) // (2)!
  }
}
```

1.  Label text for the button that adds the current product to the cart.
2.  Callback function that handles adding a product to the cart using its identifier.



### [:material-arrow-up-left:](#try-on-feature) Fit Disclaimer
```typescript
TryOnFitDisclaimerFeature {
  icons {
    info20: Icon | null // (1)!
  }

  strings {
    fitDisclaimerTitle: String // (2)!
    fitDisclaimerDescription: String // (3)!
    fitDisclaimerButtonClose: String // (4)!
  }

  typography {
    disclaimer: TextStyle // (5)!
  }
}
```

1.  Optional icon displayed in the fit disclaimer to provide visual context.
2.  Title text displayed in the fit disclaimer message.
3.  Detailed description text explaining the fit disclaimer information.
4.  Label text for the button that dismisses the fit disclaimer.
5.  Defines the text style for the fit diclaimer label text.



### [:material-arrow-up-left:](#try-on-feature) Feedback
```typescript
TryOnFeedbackFeature {
  otherFeedback: TryOnFeedbackOtherFeature | null // (1)!

  icons {
    like36: Icon // (2)!
    dislike36: Icon // (3)!
    gratitude40: Icon // (4)!
  }

  strings {
    feedbackOptions: List<String> // (5)!
    feedbackTitle: String // (6)!
    feedbackButtonSkip: String // (7)!
    feedbackButtonSend: String // (8)!
    feedbackGratitudeText: String // (9)!
  }
}
```

1.  [:material-arrow-down-left:](#other-feedback) Optional configuration for allowing users to provide custom feedback on try-on results.
2.  Icon displayed for the "Like" feedback option.
3.  Icon displayed for the "Dislike" feedback option.
4.  Icon shown after feedback is submitted to express gratitude.
5.  List of available feedback options presented to users.
6.  Title text displayed in the feedback section.
7.  Label text for the button that allows users to skip providing feedback.
8.  Label text for the button that submits the user's feedback.
9.  Message displayed to users after they submit their feedback.



#### [:material-arrow-up-left:](#feedback) Other Feedback
```typescript
TryOnFeedbackOtherFeature {
  strings {
    otherFeedbackTitle: String // (1)!
    otherFeedbackButtonSend: String // (2)!
    otherFeedbackButtonCancel: String // (3)!
    otherFeedbackOptionOther: String // (4)!
  }
}
```

1.  Title text displayed in the custom feedback section.
2.  Label text for the button that submits the custom feedback.
3.  Label text for the button that cancels the custom feedback.
4.  Text label for the option to provide custom feedback.



### [:material-arrow-up-left:](#try-on-feature) Other Photo
```typescript
TryOnWithOtherPhotoFeature {
  icons {
    changePhoto24: Icon // (1)!
  }
}
```

1.  Icon displayed for the "Change Photo" action, allowing users to continue with a different photo. 



### [:material-arrow-up-left:](#try-on-feature) Generations History
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
