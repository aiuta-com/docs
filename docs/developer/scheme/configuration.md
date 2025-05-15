# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

While the implementation details may vary, the core structure and naming conventions remain consistent across platforms to maintain a unified developer experience.

## Scheme

```typescript
Configuration {
  auth: Auth,// (1)!
  userInterface: UserInterface,// (2)!
  features: Features,// (3)!
  analytics: Analytics | null,// (4)!
  debugSettings: DebugSettings,// (5)!
}
```

1.  Required to [authenticate  :octicons-link-external-24:](#auth) Aiuta SDK to use [API :octicons-link-external-24:](https://developer.aiuta.com/products/digital-try-on/documentation){:target="_blank"} with your credentials. Supported authentication methods are `ApiKey` or `Jwt` + `subscriptionId`. 

    Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} Obtaining credentials section for instructions on how to get your credentials.

2. Configuration of the [user interface :octicons-arrow-down-24:](#userinterface) presentation style, swipe-to-dismiss policy, and UI components themes for the Aiuta SDK.

3. Describes the set of [features :octicons-arrow-down-24:](#features) enabled in the SDK for the user and thier interaction with the app.

4. Allows to receive [analytics :octicons-arrow-down-24:](#analytics) events from the SDK and send them to your analytics provider.

5. Controls the [logging :octicons-arrow-down-24:](#debugsettings) settings and [validation policies :octicons-arrow-down-24:](#debugsettings) for various parameters.

### Auth

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
      getJwt: Callback([string: string]) => string,// (2)!
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

### UserInterface
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

1.  __`iOS only`__ Specifies the manner in which the SDK's UI overlays the application's existing UI. This setting determines the visual presentation style, such as whether the SDK UI appears as a full-screen overlay, or covers the application with a bottom sheet.

2.  __`iOS only`__ This property specifies the policy for dismissing the SDK's user interface through a swipe gesture. It determines how and when the swipe-to-dismiss action can be performed by the user. The policy can vary, allowing for different levels of interaction, such as always allowing a swipe to dismiss, restricting it to certain conditions, or permitting it only when swiping from specific areas of the interface.

3.  Specifies the theme configuration settings that determine the appearance and style of the UI components within the SDK. This includes defining color schemes, typography, and other visual elements to ensure a cohesive and customizable user interface experience.

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

#### Theme
```typescript
Theme {
  color: ColorTheme,// (1)!
  label: LabelTheme,// (2)!
  image: ImageTheme,// (3)!
  button: ButtonTheme,// (4)!
  pageBar: PageBarTheme,// (5)!
  bottomSheet: BottomSheetTheme,// (6)!
  selectionSnackbar: SelectionSnackbarTheme,// (7)!
  errorSnackbar: ErrorSnackbarTheme,// (8)!
  productBar: ProductBarTheme,// (9)!
  powerBar: PowerBarTheme// (10)!
}
```

1. Defines the color scheme, brand colors, and various color states for UI elements.

2. Controls typography and text styling for different label types across the interface.

3. Manages image shapes, sizes, and error state icons for visual elements.

4. Defines button styles, including typography and shape configurations for different button sizes.

5. Controls navigation bar appearance, including title styling and navigation button icons.

6. Manages bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

7. Defines the multi-selection interface for list views, including selection controls and action buttons.

8. Controls error message presentation, including error icons and retry button styling.

9. Manages product information display, including typography for product details and optional price styling.

10. Controls the "Powered By Aiuta" branding element appearance within the interface.

###### Color
```typescript
ColorTheme {
  scheme: ColorScheme,
  brand: Color,
  primary: Color,
  secondary: Color,
  onDark: Color,
  onLight: Color,
  background: Color,
  screen: Color,
  neutral: Color,
  border: Color,
  outline: Color
}

enum ColorScheme {
  light,
  dark
}

type Color // (1)!
```

1. Hereafter, depending of the platform it could be some of the native type, or a string representing ARGB like `#FFE5E5EA`.

###### Label
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

###### Image
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

###### Button
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

###### PageBar
```typescript
PageBarTheme {
  typography: {
    pageTitle: TextStyle
  },
  icons: {
    back24: Icon,
    close24: Icon
  },
  toggles: {
    preferCloseButtonOnTheRight: boolean
  }
}

```

###### Bottom Sheet
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
    width: Dp,
    topPadding: Dp
  },
  toggles: {
    extendDelimitersToTheRight: boolean,
    extendDelimitersToTheLeft: boolean
  }
}

```

###### Selection
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

###### Error
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

###### Product
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
  toggles: {
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

###### Powered By
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

### Features
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
  dataProvider: {
    isOnboardingCompleted: Flow<boolean>,
    completeOnboarding: Callback()
  }
}

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
    toggles: {
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

ShareFeature {
  watermark: ShareWatermarkFeature | null,
  icons: {
    share24: Icon
  },
  strings: {
    shareButton: string
  },
  dataProvider: {
    getShareText: Callback(productIds: string[]) => string
  } | null
}

WishlistFeature {
  icons: {
    wishlist24: Icon,
    wishlistFill24: Icon
  },
  strings: {
    wishlistButtonAdd: string
  },
  dataProvider: {
    wishlistProductsIds: Flow<string[]>,
    setProductInWishlist: Callback(productId: string, inWishlist: boolean)
  }
}
```

### Analytics
```typescript
Analytics {
  handler: {
    onAnalyticsEvent: Callback(AnalyticEvent)
  }
}
```

### DebugSettings
```typescript
DebugSettings {
  isLoggingEnabled: boolean,
  emptyStringsPolicy: ValidationPolicy,
  unavailableResourcesPolicy: ValidationPolicy, // Flutter only
  infoPlistDescriptionsPolicy: ValidationPolicy, // iOS only
  listSizePolicy: ValidationPolicy
}

enum ValidationPolicy {
  ignore,
  warning,
  fatal
}
```
