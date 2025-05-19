# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

While the implementation details may vary, the core structure and naming conventions remain consistent across platforms to maintain a unified developer experience.

!!! not "Type Definitions"
    Please, refer to the [:octicons-arrow-right-24: platform specific types](platform-types.md) used in this scheme and the [:octicons-arrow-right-24: History Image](history-images.md) description.

## Configuration

```typescript
Configuration {
  auth: Auth,// (1)!
  userInterface: UserInterface,// (2)!
  features: Features,// (3)!
  analytics: Analytics | null,// (4)!
  debugSettings: DebugSettings,// (5)!
}
```

1.  [:material-arrow-down-left:](#auth) Required to authenticate Aiuta SDK to use [API :octicons-link-external-24:](https://developer.aiuta.com/products/digital-try-on/documentation){:target="_blank"} with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`. 

    Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} Obtaining credentials section for instructions on how to get your credentials.

2. [:material-arrow-down-left:](#userinterface) Configuration of the user interface presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

3. [:material-arrow-down-left:](#features) Describes the set of features enabled in the SDK for the user and thier interaction with the app.

4. [:material-arrow-down-left:](#analytics) Allows to receive analytics events from the SDK and send them to your analytics provider.

5. [:material-arrow-down-left:](#debugsettings) Controls the logging settings and validation policies for various parameters.

### [:material-arrow-up-left:](#configuration) Auth

=== "ApiKey"
    ```typescript
    ApiKeyAuth {
      apiKey: string,// (1)!
    }
    ```

    1.  The `apiKey` is used to authenticate all outgoing requests from the Aiuta SDK to the Aiuta API. This key ensures that the requests are linked to your account, allowing the SDK to access the necessary resources and services provided by Aiuta. 
    
        Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} obtaining credentials section for instructions on how to get your `apiKey`.
  
=== "Jwt"
    ```typescript
    JwtAuth {
      subscriptionId: string,// (1)!
      getJwt: Callback(Map<string: string>) => string,// (2)!
    }
    ```

    1.  The `subscriptionId` is used to authenticate requests that do not require secure transmission. It acts as a key to ensure that the requests are properly linked to your subscription and account.

        Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} obtaining credentials section for instructions on how to find your `subscriptionId`.
        
    2.  This method is invoked by the SDK each time a tryOn request necessitates authentication
        through a JSON Web Token. The implementation of this method should securely
        generate the JWT on the server side and subsequently return it to the SDK.

        The SDK will provide a set of key-value pairs that represent the `parameters` of the request
        requiring a JWT. These parameters include identifiers like a `uploaded_image_id` and `product_id` and can be used 
        for associating the JWT with the specific image and product involved in the tryOn request. 
        This ensures that the generated token is tailored specifically to the request being processed, enhancing security and relevance.

        - __Returns__ a string representing the generated JSON Web Token.

        - __Throws__ an error if the JWT cannot be generated. If an error is thrown,
          the SDK will be unable to complete the tryOn request and will display
          an error message to the user.

        See [JWT server-side auth example :octicons-link-external-24:](https://developer.aiuta.com/docs/server-side-auth-component){:target="_blank"} for more details on securely generating JWTs.

### [:material-arrow-up-left:](#configuration) User Interface
```typescript
UserInterface {
  presentationStyle: PresentationStyle,// (1)!
  swipeToDismiss: SwipeToDismissPolicy,// (2)!
  theme: Theme,// (3)!
}

enum PresentationStyle {
  fullScreen,// (4)!
  bottomSheet,// (5)!
  pageSheet,// (6)!
}

enum SwipeToDismissPolicy {
  allowAlways,// (7)!
  allowHeaderSwipeOnly,// (8)!
  protectTheNecessaryPages,// (9)!
}
```

1.  !!! note "iOS and Flutter only"
        
        Specifies the manner in which the SDK's UI overlays the application's existing UI. This setting determines the visual presentation style, such as whether the SDK UI appears as a full-screen overlay, or covers the application with a bottom sheet.

2.  !!! note "iOS only"
        
        This property specifies the policy for dismissing the SDK's user interface through a swipe gesture. It determines how and when the swipe-to-dismiss action can be performed by the user. The policy can vary, allowing for different levels of interaction, such as always allowing a swipe to dismiss, restricting it to certain conditions, or permitting it only when swiping from specific areas of the interface.

3.  [:material-arrow-down-left:](#theme) Specifies the theme configuration settings that determine the appearance and style of the UI components within the SDK. This includes defining color schemes, typography, and other visual elements to ensure a cohesive and customizable user interface experience.

4.  Presents the SDK in full-screen mode. This style occupies the entire screen, hiding the parent view completely.

5.  Opens the SDK in a bottom sheet. This mode is supported on iOS from version `16` onwards. For older versions, it defaults to `pageSheet`. Unlike `pageSheet`, the parent view remains fullscreen but is covered by the sheet, rather than being stacked behind it.

6.  The SDK will be presented in a page sheet. 

    - This mode is recommended starting from __iOS__ 13, as it introduces a new modal presentation style that allows part of the parent view to remain visible. This helps users maintain their original context while interacting with the sheet. For more information, refer to [Best practices from Apple's HIG :octicons-link-external-24:](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices){:target="_blank"}. In this mode, the parent view is stacked behind the sheet, slightly shrinking and moving away from the screen edges. 
    
    - On __Android__, this mode behaves as a `bottomSheet`.

7.  Allows the SDK to be dismissed at any time by swiping down anywhere on the screen.

    This policy provides the most flexibility for users, enabling them to close the SDK from any page or context.    

8.  Restricts dismissal to swiping down on the header area only.

    This policy limits the swipe-to-dismiss gesture to the header area, reducing the likelihood of accidental dismissals.

9.  Applies different swipe-to-dismiss policies based on the page context.
    
    - On pages that are safe to close, such as onboarding or photo picker pages, the `allowAlways` policy is applied, allowing dismissal from anywhere on the screen.
    - On critical pages, such as those waiting for generation or displaying results, the `allowHeaderSwipeOnly` policy is applied to prevent accidental dismissals.
    
    This policy provides a balance between user convenience and protecting critical workflows, ensuring that users can dismiss the SDK when appropriate while safeguarding important pages.    

#### [:material-arrow-up-left:](#user-interface) Theme
```typescript
Theme {
  color: ColorTheme,// (1)!
  label: LabelTheme,// (2)!
  image: ImageTheme,// (3)!
  button: ButtonTheme,// (4)!
  activityIndicator: ActivityIndicatorTheme,// (11)!
  pageBar: PageBarTheme,// (5)!
  bottomSheet: BottomSheetTheme,// (6)!
  selectionSnackbar: SelectionSnackbarTheme,// (7)!
  errorSnackbar: ErrorSnackbarTheme,// (8)!
  productBar: ProductBarTheme,// (9)!
  powerBar: PowerBarTheme,// (10)!
}
```

1. [:material-arrow-down-left:](#color) Defines the color scheme, brand colors, and various color states for UI elements.
    
    !!! note ""
        [:octicons-arrow-right-24: Explore all colors :material-invert-colors:](../../about/resources/colors.md)

2. [:material-arrow-down-left:](#label) Typography and text styling for different label types across the interface.

3. [:material-arrow-down-left:](#image) Shapes, sizes, and error state icon for image views.

4. [:material-arrow-down-left:](#button) Buttons styles, including typography and shape configurations for different button sizes.

5. [:material-arrow-down-left:](#pagebar) Navigation bar appearance, including title styling and navigation button icons.

6. [:material-arrow-down-left:](#bottom-sheet) Bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

7. [:material-arrow-down-left:](#selection) Multi-selection interface for list views, including selection controls and action buttons.

8. [:material-arrow-down-left:](#error) Error message presentation, including error icons and retry button styling.

9. [:material-arrow-down-left:](#product) Product information display, including typography for product details and optional price styling.

10. [:material-arrow-down-left:](#powered-by) "Powered By Aiuta" branding element appearance within the interface.

11. [:material-arrow-down-left:](#activity-indicator) Appearance and customization of loading indicators.

###### [:material-arrow-up-left:](#theme) Color
```typescript
ColorTheme {
  scheme: ColorScheme,// (1)!
  brand: Color,// (2)!
  primary: Color,// (3)!
  secondary: Color,// (4)!
  onDark: Color,// (5)!
  onLight: Color,// (6)!
  background: Color,// (7)!
  screen: Color,// (8)!
  neutral: Color,// (9)!
  border: Color,// (10)!
  outline: Color,// (11)!
}

enum ColorScheme {
  light,// (12)!
  dark,// (13)!
}
```

1.  Defines whether the SDK uses a light or dark theme.
    Provided colors should match the scheme.

    !!! note ""
        On __`iOS only`__ it affects the appearance of system screens (e.g., photo gallery, share activity, etc.) and ensures that their `UIUserInterfaceStyle` matches the selected style. For example, if the SDK is set to a light theme but the system theme on the device is dark, the system windows invoked by the SDK will still use the light theme. Additionally, this setting influences the style of blur components and the tint applied to recolored icons within the SDK.

2. Main accent color for primary actions and highlights throughout the interface.

3. Primary text color used for main content and important information.

4. Secondary text color used for supporting content and less prominent information.

5. Preferably light color __in any scheme__ optimized for use on dark, brand, and neutral backgrounds.

6. Preferably dark color __in any scheme__ optimized for use on light backgrounds.

7. Main background color used throughout the SDK interface.

8.  Zero-elevation background color.

    For full-screen mode in dark scheme, this color is used as a background color, while bottom sheets inside the SDK will still use the background color. In any scheme it will be used for full-screen image galleries.

    !!! note ""
        It's actually supposed to be `black` or close to black in any scheme.

9. Neutral background color used for various UI components.

10. Color used for component borders and dividers.

11. Color used for blur outlines and checkmark borders.

12. Light theme with predominantly light colors in the design.

13. Dark theme with predominantly dark colors in the design.

###### [:material-arrow-up-left:](#theme) Label
```typescript
LabelTheme {
  typography: {
    titleL: TextStyle,
    titleM: TextStyle,
    regular: TextStyle,
    subtle: TextStyle
  }
}
```

###### [:material-arrow-up-left:](#theme) Image
```typescript
ImageTheme {
  shapes: {
    imageL: Shape,
    imageS: Shape
  },
  icons: {
    imageError36: Icon
  }
}

```

###### [:material-arrow-up-left:](#theme) Button
```typescript
ButtonTheme {
  typography: {
    buttonM: TextStyle,
    buttonS: TextStyle
  },
  shapes: {
    buttonM: Shape,
    buttonS: Shape
  }
}

```

###### [:material-arrow-up-left:](#theme) Activity Indicator
```typescript
ActivityIndicatorTheme {
  icons: {
    loading14: Icon | null,// (1)!
  },
  colors: {
    overlay: Color,// (4)!
  }
  settings: {
    indicationDelay: Number,// (2)!
    spinDuration: Number,// (3)!
  }
}

```

1. Optional icon for the activity indicator. If not provided, the system's default indicator will be used.

    !!! example ""
        System activity indicator by default

        ![Activity Indicator](../../media/components/activity-indicator.png){ width=36}

2. The time in milliseconds before the activity indicator appears. If the task completes before this delay, the indicator will not be shown. Otherwise, the indicator will appear.

3. The duration in milliseconds for one complete rotation of the activity indicator. This setting controls how fast the indicator spins, providing a visual cue of activity progress.
    
    !!! note ""
        The spin duration only applies when a custom icon is used for the activity indicator. If the system's default indicator is used, this setting will be ignored and the indicator will spin with the system default speed.

4. Overlay color used to cover any view when it needs to be locked for an activity. The activity indicator will be placed at the center of this overlay.

###### [:material-arrow-up-left:](#theme) PageBar
```typescript
PageBarTheme {
  typography: {
    pageTitle: TextStyle
  },
  icons: {
    back24: Icon,
    close24: Icon
  },
  settings: {
    preferCloseButtonOnTheRight: boolean
  }
}

```

###### [:material-arrow-up-left:](#theme) Bottom Sheet
```typescript
BottomSheetTheme {
  typography: {
    iconButton: TextStyle,
    chipsButton: TextStyle
  },
  shapes: {
    bottomSheet: Shape,
    chipsButton: Shape
  },
  grabber: {
    width: number,
    height: number,
    topPadding: number
  },
  settings: {
    extendDelimitersToTheRight: boolean,
    extendDelimitersToTheLeft: boolean
  }
}

```

###### [:material-arrow-up-left:](#theme) Selection
```typescript
SelectionSnackbarTheme {
  strings: {
    select: string,
    cancel: string,
    selectAll: string,
    unselectAll: string
  },
  icons: {
    trash24: Icon,
    check20: Icon
  },
  colors: {
    selectionBackground: Color
  }
}

```

###### [:material-arrow-up-left:](#theme) Error
```typescript
ErrorSnackbarTheme {
  strings: {
    defaultErrorMessage: string,
    tryAgainButton: string
  },
  icons: {
    error36: Icon
  },
  colors: {
    errorBackground: Color,
    errorPrimary: Color
  }
}

```

###### [:material-arrow-up-left:](#theme) Product
```typescript
ProductBarTheme {
  prices: ProductBarPricesTheme | null,
  typography: {
    product: TextStyle,
    brand: TextStyle
  },
  icons: {
    arrow16: Icon
  },
  settings: {
    applyProductFirstImageExtraPadding: boolean
  }
}

ProductBarPricesTheme {
  typography: {
    price: TextStyle
  },
  colors: {
    discountedPrice: Color
  }
}
```

###### [:material-arrow-up-left:](#theme) Powered By
```typescript

PowerBarTheme {
  strings: {
      poweredByAiuta: string,
   },
   colors: {
      aiuta: PowerBarColorScheme
   }
}

enum PowerBarColorScheme {
  default,
  primary
}

```

### [:material-arrow-up-left:](#configuration) Features
```typescript
Features {
  welcomeScreen: WelcomeScreenFeature | null,
  onboarding: OnboardingFeature | null,
  consent: ConsentFeature | null,
  imagePicker: ImagePickerFeature,
  tryOn: TryOnFeature,
  share: ShareFeature | null,
  wishlist: WishlistFeature | null
}
```

#### [:material-arrow-up-left:](#features) Welcome Screen
```typescript
WelcomeScreenFeature {
  images: {
    welcomeBackground: Image
  },
  icons: {
    welcome82: Icon
  },
  strings: {
    welcomeTitle: string,
    welcomeDescription: string,
    welcomeButtonStart: string
  },
  typography: {
    welcomeTitle: TextStyle,
    welcomeDescription: TextStyle
  }
}

```

#### [:material-arrow-up-left:](#features) Onboarding
```typescript
OnboardingFeature {
  howItWorksPage: OnboardingHowItWorksPageFeature,
  bestResultsPage: OnboardingBestResultsPageFeature | null,
  strings: {
    onboardingButtonNext: string,
    onboardingButtonStart: string
  },
  shapes: {
    onboardingImageL: Shape,
    onboardingImageS: Shape
  },
  dataProvider: BuiltIn | Custom {
    isOnboardingCompleted: Flow<boolean>,
    completeOnboarding: Callback()
  }
}

```

###### [:material-arrow-up-left:](#onboarding) How It Works
```typescript
OnboardingHowItWorksPageFeature {
  images: {
    onboardingHowItWorksItems: {
      itemPhoto: Image,
      itemPreview: Image
    }[]
  },
  strings: {
    onboardingHowItWorksPageTitle: string | null,
    onboardingHowItWorksTitle: string,
    onboardingHowItWorksDescription: string
  }
}

```

###### [:material-arrow-up-left:](#onboarding) Best Results
```typescript
OnboardingBestResultsPageFeature {
  images: {
    onboardingBestResultsGood: Image[],
    onboardingBestResultsBad: Image[]
  },
  icons: {
    onboardingBestResultsGood24: Icon,
    onboardingBestResultsBad24: Icon
  },
  strings: {
    onboardingBestResultsPageTitle: string | null,
    onboardingBestResultsTitle: string,
    onboardingBestResultsDescription: string
  },
  styles: {
    reduceOnboardingBestResultsShadows: boolean
  }
}
```


#### [:material-arrow-up-left:](#features) Consent

=== "Embedded Into Onboarding"
    ```typescript
    ConsentEmbeddedIntoOnboardingFeature {
      strings: {
        consentHtml: string
      }
    }
    ```

=== "Standalone Onboarding Page"
    ```typescript
    ConsentStandaloneOnboardingPageFeature {
      strings: {
        consentPageTitle: string | null,
        consentTitle: string,
        consentDescriptionHtml: string,
        consentFooterHtml: string | null,
        consentButtonAccept: string
      },
      icons: {
        consentTitle24: Icon
      },
      styles: {
        drawBordersAroundConsents: boolean
      },
      data: {
        consents: Consent[]
      },
      dataProvider: BuiltIn | Custom {
        obtainedConsentsIds: Flow<string[]>,
        obtainConsentsIds: Callback(string[])
      }
    }
    ```

=== "Standalone Image Picker Page"
    ```typescript
    ConsentStandaloneImagePickerPageFeature {
      strings: {
        consentPageTitle: string | null,
        consentTitle: string,
        consentDescriptionHtml: string,
        consentFooterHtml: string | null,
        consentButtonAccept: string
      },
      icons: {
        consentTitle24: Icon
      },
      styles: {
        drawBordersAroundConsents: boolean
      },
      data: {
        consents: Consent[]
      },
      dataProvider: BuiltIn | Custom {
        obtainedConsentsIds: Flow<string[]>,
        obtainConsentsIds: Callback(string[])
      }
    }
    ```

```typescript
Consent {
  id: string,
  type: ConsentType,
  html: string,
}

enum ConsentType {
  implicitWithoutCheckbox,
  implicitWithCheckbox,
  explicitRequired,
  explicitOptional,
}
```

#### [:material-arrow-up-left:](#features) Image Picker
```typescript
ImagePickerFeature {
  camera: ImagePickerCameraFeature | null,
  photoGallery: ImagePickerPhotoGalleryFeature,
  predefinedModels: ImagePickerPredefinedModelFeature | null,
  uploadsHistory: ImagePickerUploadsHistoryFeature | null,
  images: {
    examples: Image[]
  },
  strings: {
    imagePickerTitleEmpty: string,
    imagePickerDescriptionEmpty: string,
    imagePickerButtonUploadImage: string
  }
}

```

###### [:material-arrow-up-left:](#image-picker) Camera
```typescript
ImagePickerCameraFeature {
  icons: {
    camera24: Icon
  },
  strings: {
    cameraButtonTakePhoto: string,
    cameraPermissionTitle: string,
    cameraPermissionDescription: string,
    cameraPermissionButtonOpenSettings: string
  }
}
```

###### [:material-arrow-up-left:](#image-picker) Photo Gallery
```typescript
ImagePickerPhotoGalleryFeature {
  icons: {
    gallery24: Icon
  },
  strings: {
    galleryButtonSelectPhoto: string
  }
}
```

###### [:material-arrow-up-left:](#image-picker) Predefined Models
```typescript
ImagePickerPredefinedModelFeature {
  icons: {
    selectModels24: Icon
  },
  data: {
    preferredCategoryId: string
  }
  strings: {
    predefinedModelPageTitle: string,
    predefinedModelOr: string,
    predefinedModelErrorEmptyModelsList: string,
    predefinedModelCategories: {
      [categoryId: string]: string
    }
  }
}
```

###### [:material-arrow-up-left:](#image-picker) Uploads History
```typescript
ImagePickerUploadsHistoryFeature {
  strings: {
    uploadsHistoryButtonNewPhoto: string,
    uploadsHistoryTitle: string,
    uploadsHistoryButtonChangePhoto: string
  },
  styles: {
    changePhotoButtonStyle: primary | blurred
  },
  dataProvider: BuiltIn | Custom {
    uploadedImages: Flow<InputImage>,
    addUploadedImagesAction: Callback(InputImage[]),
    deleteUploadedImagesAction: Callback(InputImage[]),
    selectUploadedImageAction: Callback(InputImage)
  }
}
```

#### [:material-arrow-up-left:](#features) Try On
```typescript
TryOnFeature {
  tryOn: {
    loadingPage: TryOnLoadingPageFeature,
    inputImageValidation: TryOnInputImageValidationFeature,
    cart: TryOnCartFeature,
    fitDisclaimer: TryOnFitDisclaimerFeature | null,
    feedback: TryOnFeedbackFeature | null,
    generationsHistory: TryOnGenerationsHistoryFeature | null,
    multiItem: TryOnMultiItemFeature | null,
    otherPhoto: TryOnWithOtherPhotoFeature | null,
    settings: {
      isBackgroundExecutionAllowed: boolean
    },
    icons: {
      tryOn20: Icon
    },
    strings: {
      tryOnPageTitle: string,
      tryOn: string
    },
    styles: {
      tryOnButtonGradient: Color[] | null
    }
  }
}

```

##### [:material-arrow-up-left:](#try-on) Input Image Validation
```typescript
TryOnInputImageValidationFeature {
  strings: {
    invalidInputImageDescription: string,
    invalidInputImageChangePhotoButton: string
  }
}
```

##### [:material-arrow-up-left:](#try-on) Cart
```typescript
TryOnCartFeature {
  strings: {
    addToCart: string
  },
  handler: {
    addToCartAction: Callback(string)
  }
}
```

##### [:material-arrow-up-left:](#try-on) Multi Item
```typescript
TryOnMultiItemFeature {
  cart: TryOnMultiItemCartFeature,
  strings: {}
}
```

###### [:material-arrow-up-left:](#multi-item) Cart
```typescript
TryOnMultiItemCartFeature {
  strings: {
    shopTheLook: string
  },
  handler: {
    shopTheLook: Callback(string[])
  }
}
```

##### [:material-arrow-up-left:](#try-on) Loading Page
```typescript
TryOnLoadingPageFeature {
  strings: {
    tryOnLoadingStatusUploadingImage: string,
    tryOnLoadingStatusScanningBody: string,
    tryOnLoadingStatusGeneratingOutfit: string
  },
  styles: {
    loadingStatusBackgroundGradient: Color[] | null,
    loadingStatusStyle: "primary" | "blurred" | "blurredWithOutline"
  }
}
```

##### [:material-arrow-up-left:](#try-on) Fit Disclaimer
```typescript
TryOnFitDisclaimerFeature {
  icons: {
    info20: Icon | null
  },
  strings: {
    fitDisclaimerTitle: string,
    fitDisclaimerDescription: string,
    fitDisclaimerButtonClose: string
  }
}
```

##### [:material-arrow-up-left:](#try-on) Feedback
```typescript
TryOnFeedbackFeature {
  otherFeedback: TryOnFeedbackOtherFeature | null,
  icons: {
    like36: Icon,
    dislike36: Icon,
    gratitude40: Icon
  },
  strings: {
    feedbackOptions: string[],
    feedbackTitle: string,
    feedbackButtonSkip: string,
    feedbackButtonSend: string,
    feedbackGratitudeText: string
  }
}
```

###### [:material-arrow-up-left:](#feedback) Other
```typescript
TryOnFeedbackOtherFeature {
  strings: {
    otherFeedbackTitle: string,
    otherFeedbackButtonSend: string,
    otherFeedbackButtonCancel: string,
    otherFeedbackOptionOther: string
  }
}
```

##### [:material-arrow-up-left:](#try-on) Generations History
```typescript
TryOnGenerationsHistoryFeature {
  icons: {
    history24: Icon
  },
  strings: {
    generationsHistoryPageTitle: string
  },
  dataProvider: BuiltIn | Custom {
    generatedImages: Flow<GenegaredImage>,
    addGeneratedImages: Callback(GenegaredImage[]),
    deleteGeneratedImages: Callback(GenegaredImage[])
  }
}
```

##### [:material-arrow-up-left:](#try-on) Other Photo
```typescript
TryOnWithOtherPhotoFeature {
  icons: {
    changePhoto24: Icon
  }
}
```

#### [:material-arrow-up-left:](#features) Share
```typescript

ShareFeature {
  watermark: ShareWatermarkFeature | null,
  icons: {
    share24: Icon
  },
  strings: {
    shareButton: string
  },
  dataProvider: null | Custom {
    getShareText: Callback(productIds: string[]) => string
  }
}

```

###### [:material-arrow-up-left:](#share) Watermark
```typescript

ShareWatermarkFeature {
  images: {
    logo: Image
  }
}
```

#### [:material-arrow-up-left:](#features) Wishlist
```typescript

WishlistFeature {
  icons: {
    wishlist24: Icon,
    wishlistFill24: Icon
  },
  strings: {
    wishlistButtonAdd: string
  },
  dataProvider: {
    wishlistProductIds: Flow<string[]>,
    setProductInWishlist: Callback(productId: string, inWishlist: boolean)
  }
}
```

### [:material-arrow-up-left:](#configuration) Analytics
```typescript
Analytics {
  handler: {
    onAnalyticsEvent: Callback(AnalyticEvent)
  }
}
```

### [:material-arrow-up-left:](#configuration) DebugSettings
```typescript
DebugSettings {
  isLoggingEnabled: boolean,
  emptyStringsPolicy: ValidationPolicy,
  unavailableResourcesPolicy: ValidationPolicy,
  infoPlistDescriptionsPolicy: ValidationPolicy,
  listSizePolicy: ValidationPolicy
}

enum ValidationPolicy {
  ignore,
  warning,
  fatal
}
```
