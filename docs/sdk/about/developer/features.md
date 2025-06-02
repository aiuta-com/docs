<!-- part of `configuration.md` -->

### [:material-arrow-up-left:](configuration.md#configuration) Features
```typescript
Features {
  welcomeScreen: WelcomeScreenFeature | null // (1)!
  onboarding: OnboardingFeature | null // (2)!
  consent: ConsentFeature | null // (3)!
  imagePicker: ImagePickerFeature // (4)!
  tryOn: TryOnFeature // (5)!
  share: ShareFeature | null // (6)!
  wishlist: WishlistFeature | null // (7)!
}
```

1. [:material-arrow-down-left:](#welcome-screen) Configures an optional welcome screen that introduces users to the SDK's functionality.
2. [:material-arrow-down-left:](#onboarding) Sets up the onboarding process to guide users through the SDK's features and capabilities.
3. [:material-arrow-down-left:](#consent) Manages user consent options for data processing, which can be integrated with onboarding or used independently.
4. [:material-arrow-down-left:](#image-picker) Controls the image selection interface, allowing users to pick photos, take new ones, use predefined models, or access previous uploads.
5. [:material-arrow-down-left:](#try-on) Configures the core virtual try-on functionality for trying products virtually.
6. [:material-arrow-down-left:](#share) Enables sharing capabilities for generated try-on images with customizable options.
7. [:material-arrow-down-left:](#wishlist) Integrates with the host app's wishlist functionality for product management.



#### [:material-arrow-up-left:](#features) Welcome Screen
```typescript
WelcomeScreenFeature {
  images {
    welcomeBackground: Image // (1)!
  }

  icons {
    welcome82: Icon // (2)!
  }

  strings {
    welcomeTitle: String // (3)!
    welcomeDescription: String // (4)!
    welcomeButtonStart: String // (5)!
  }

  typography {
    welcomeTitle: TextStyle // (6)!
    welcomeDescription: TextStyle // (7)!
  }
}

```

1. Sets the background image that covers the entire welcome screen.
2. Defines the main icon displayed in the center of the welcome screen above the title.
3. Specifies the main title text displayed on the welcome screen.
4. Configures the descriptive text that appears below the title on the welcome screen.
5. Sets the text label for the button that initiates the onboarding process or main interface.
6. Controls the text style for the welcome screen's main title.
7. Defines the text style for the welcome screen's description text.



#### [:material-arrow-up-left:](#features) Onboarding
```typescript
OnboardingFeature {
  howItWorksPage: OnboardingHowItWorksPageFeature // (1)!
  bestResultsPage: OnboardingBestResultsPageFeature | null // (2)!

  strings {
    onboardingButtonNext: String // (3)!
    onboardingButtonStart: String // (4)!
  }

  shapes {
    onboardingImageL: Shape // (5)!
    onboardingImageS: Shape // (6)!
  }

  dataProvider: BuiltIn | Custom {
    isOnboardingCompleted: Observable<Bool> // (7)!
    completeOnboarding: Callback() // (8)!
  }
}

```

1. [:material-arrow-down-left:](#how-it-works) Configures the first page of onboarding that demonstrates how virtual try-on works through interactive examples.
2. [:material-arrow-down-left:](#best-results) Sets up an optional page showing examples of photos that yield the best try-on results.
3. Defines the text label for the navigation button to proceed to the next onboarding page.
4. Specifies the text label for the button that completes onboarding and starts the main interface.
5. Controls the shape configuration for large images displayed in the onboarding process.
6. Sets the shape configuration for small images used in the onboarding interface.
7. Provides an observable property that tracks whether the user has completed the onboarding process.
8. Defines the callback function to mark onboarding as completed when the user finishes the process.



###### [:material-arrow-up-left:](#onboarding) How It Works
```typescript
OnboardingHowItWorksPageFeature {
  images {
    onboardingHowItWorksItems: List<{ // (6)!
      itemPhoto: Image // (1)!
      itemPreview: Image // (2)!
    }>
  }

  strings {
    onboardingHowItWorksPageTitle: String | null // (3)!
    onboardingHowItWorksTitle: String // (4)!
    onboardingHowItWorksDescription: String // (5)!
  }
}

```

1. Defines the example photo showing a person wearing the item for the try-on demonstration.
2. Specifies the flatlay image of the item with a transparent background for the try-on preview.
3. Sets an optional title for the "How It Works" page at the top of the screen.
4. Defines the main title displayed below the interactive try-on demonstration section.
5. Configures the descriptive text explaining how the virtual try-on feature works.
6. List of exactly 3 objects, each containing images for the interactive onboarding.



###### [:material-arrow-up-left:](#onboarding) Best Results
```typescript
OnboardingBestResultsPageFeature {
  images {
    onboardingBestResultsGood: List<Image> // (1)!
    onboardingBestResultsBad: List<Image> // (2)!
  }

  icons {
    onboardingBestResultsGood24: Icon // (3)!
    onboardingBestResultsBad24: Icon // (4)!
  }

  strings {
    onboardingBestResultsPageTitle: String | null // (5)!
    onboardingBestResultsTitle: String // (6)!
    onboardingBestResultsDescription: String // (7)!
  }

  styles {
    reduceOnboardingBestResultsShadows: Bool // (8)!
  }
}
```

1. List of exactly 2 example photos that demonstrate optimal conditions for virtual try-on results.
2. List of exactly 2 of example photos showing conditions that may lead to suboptimal try-on results.
3. Icon displayed next to good example photos to indicate positive results.
4. Icon displayed next to bad example photos to indicate potential issues.
5. Optional title for the "Best Results" page at the top of the screen.
6. Main title displayed above the example photos section.
7. Descriptive text explaining what makes a good photo for virtual try-on.
8. Controls whether to reduce shadow effects on example photos for better visibility.



#### [:material-arrow-up-left:](#features) Consent

=== "Embedded Into Onboarding"
    ```typescript
    ConsentEmbeddedIntoOnboardingFeature {
      strings {
        consentHtml: String // (1)!
      }
    }
    ```
    
    1. HTML content displayed at the bottom of the onboarding screen for embedded consent.

=== "Standalone Onboarding Page"
    ```typescript
    ConsentStandaloneOnboardingPageFeature {
      strings {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      }

      icons {
        consentTitle24: Icon // (6)!
      }

      styles {
        drawBordersAroundConsents: Bool // (7)!
      }

      data {
        consents: List<Consent> // (8)!
      }

      dataProvider: BuiltIn | Custom {
        obtainedConsentIds: Observable<List<string>> // (9)!
        obtainConsentIds: Callback(List<string>) // (10)!
      }
    }
    ```

    1. Optional title for the standalone consent page at the top of the screen.
    2. Main title displayed on the standalone consent page.
    3. HTML content describing the consent terms and conditions.
    4. Optional HTML footer content for additional information.
    5. Text label for the button that accepts the consent terms.
    6. Icon displayed next to the consent title in the standalone page.
    7. Controls whether to display borders around consent sections.
    8. List of consent options that users must and may accept.

        !!! info ""
            See [consent :octicons-arrow-right-24:](consent.md) scheme for more deatils

    9. Observable property tracking which consent options have been already accepted.
    10. Callback function triggered when user accepts consents.

        !!! info ""
            You should save the consent IDs that are passed and  provide them in the `obtainedConsentsIds` property for future use. If not stored, the SDK will show the consent screen again during the next Try-On session.

=== "Standalone Image Picker Page"
    ```typescript
    ConsentStandaloneImagePickerPageFeature {
      strings {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      }

      icons {
        consentTitle24: Icon // (6)!
      }

      styles {
        drawBordersAroundConsents: Bool // (7)!
      }

      data {
        consents: List<Consent> // (8)!
      }

      dataProvider: BuiltIn | Custom {
        obtainedConsentsIds: Observable<List<string>> // (9)!
        obtainConsentsIds: Callback(List<string>) // (10)!
      }
    }
    ```

    1. Optional title for the standalone consent page at the top of the screen.
    2. Main title displayed on the standalone consent page.
    3. HTML content describing the consent terms and conditions.
    4. Optional HTML footer content for additional information.
    5. Text label for the button that accepts the consent terms.
    6. Icon displayed next to the consent title in the standalone page.
    7. Controls whether to display borders around consent sections.
    8. List of consent options that users must and may accept.

        !!! info ""
            See [consent :octicons-arrow-right-24:](consent.md) scheme for more deatils

    9. Observable property tracking which consent options have been already accepted.
    10. Callback function triggered when user accepts consents.

        !!! info ""
            You should save the consent IDs that are passed and  provide them in the `obtainedConsentsIds` property for future use. If not stored, the SDK will show the consent screen again during the next Try-On session.



#### [:material-arrow-up-left:](#features) Image Picker
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



###### [:material-arrow-up-left:](#image-picker) Camera
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



###### [:material-arrow-up-left:](#image-picker) Photo Gallery
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



###### [:material-arrow-up-left:](#image-picker) Predefined Models
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



###### [:material-arrow-up-left:](#image-picker) Uploads History
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
    addUploadedImagesAction: Callback(List<InputImage>) // (6)!
    deleteUploadedImagesAction: Callback(List<InputImage>) // (7)!
    selectUploadedImageAction: Callback(InputImage) // (8)!
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



#### [:material-arrow-up-left:](#features) Try On
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
2.  [:material-arrow-down-left:](#inout-image-validation) Configuration for validating input images before processing.
3.  [:material-arrow-down-left:](#cart) Configuration for cart-related functionality in the TryOn interface.
4.  [:material-arrow-down-left:](fit-disclaimer) Optional configuration for displaying fit disclaimers to users.
5.  [:material-arrow-down-left:](#feedback) Optional configuration for collecting user feedback on TryOn results.
6.  [:material-arrow-down-left:](#generations-history) Optional configuration for managing the history of generated TryOn results.
7.  [:material-arrow-down-left:](#other-photo) Optional configuration for allowing users to continue with a different photo.
8.  Determines whether the SDK should wait for the generation results in the background when closed.
9.  Enables local person segmentation highlighting during loading on iOS 15+.
10.  Icon displayed for the TryOn magic button in the interface.
11.  Title text displayed at the top of the TryOn page.
12.  Label text used for the "Try On" buttons throughout the interface.
13.  Optional gradient colors for styling the TryOn button.



##### [:material-arrow-up-left:](#try-on) Loading Page
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



##### [:material-arrow-up-left:](#try-on) Input Image Validation
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



##### [:material-arrow-up-left:](#try-on) Cart
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



##### [:material-arrow-up-left:](#try-on) Fit Disclaimer
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
}
```

1.  Optional icon displayed in the fit disclaimer to provide visual context.
2.  Title text displayed in the fit disclaimer message.
3.  Detailed description text explaining the fit disclaimer information.
4.  Label text for the button that dismisses the fit disclaimer.



##### [:material-arrow-up-left:](#try-on) Feedback
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

1.  [:material-arrow-down-left:](#other) Optional configuration for allowing users to provide custom feedback on try-on results.
2.  Icon displayed for the "Like" feedback option.
3.  Icon displayed for the "Dislike" feedback option.
4.  Icon shown after feedback is submitted to express gratitude.
5.  List of available feedback options presented to users.
6.  Title text displayed in the feedback section.
7.  Label text for the button that allows users to skip providing feedback.
8.  Label text for the button that submits the user's feedback.
9.  Message displayed to users after they submit their feedback.



###### [:material-arrow-up-left:](#feedback) Other
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



##### [:material-arrow-up-left:](#try-on) Generations History
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



##### [:material-arrow-up-left:](#try-on) Other Photo
```typescript
TryOnWithOtherPhotoFeature {
  icons {
    changePhoto24: Icon // (1)!
  }
}
```

1.  Icon displayed for the "Change Photo" action, allowing users to continue with a different photo.



#### [:material-arrow-up-left:](#features) Share
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



###### [:material-arrow-up-left:](#share) Watermark
```typescript
ShareWatermarkFeature {
  images {
    logo: Image // (1)!
  }
}
```

1.  Logo image to be used as a watermark on shared content.



#### [:material-arrow-up-left:](#features) Wishlist
```typescript
WishlistFeature {
  icons {
    wishlist24: Icon // (1)!
    wishlistFill24: Icon // (2)!
  }

  strings {
    wishlistButtonAdd: String // (3)!
  }
  
  dataProvider {
    wishlistProductIds: Observable<List<String>> // (4)!
    setProductInWishlist: Callback(productId: String, inWishlist: Bool) // (5)!
  }
}
```

1.  Icon displayed for the Wishlist button in its default state.
2.  Icon displayed for the Wishlist button when the product is in the wishlist.
3.  Label text for the "Add to Wishlist" button.
4.  Observable collection of product IDs currently in the wishlist.
5.  Callback function to add or remove a product from the wishlist.
