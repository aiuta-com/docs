# Configuration Scheme

The SDK configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

While the implementation details may vary, the core structure and naming conventions remain consistent across platforms to maintain a unified developer experience.

## Scheme

```typescript
Configuration {
  auth: Auth,
  userInterface: UserInterface,
  features: Features,
  analytics: Analytics | null,
  debugSettings: DebugSettings
}
```

### Auth
```typescript
Auth {
  // Authentication configuration
}
```

### UserInterface
```typescript
UserInterface {
  presentationStyle: PresentationStyle,
  swipeToDismiss: SwipeToDismissPolicy,
  actions: UserInterfaceActions,
  theme: Theme
}

enum PresentationStyle {
  fullScreen,
  bottomSheet,
  pageSheet
}

enum SwipeToDismissPolicy {
  allowAlways,
  protectTheNecessary,
  allowHeaderSwipeOnly
}

UserInterfaceActions {
  onCloseClick: Callback()
}
```

### Theme
```typescript
Theme {
  color: ColorTheme,
  label: LabelTheme,
  image: ImageTheme,
  button: ButtonTheme,
  pageBar: PageBarTheme,
  bottomSheet: BottomSheetTheme,
  selectionSnackbar: SelectionSnackbarTheme,
  errorSnackbar: ErrorSnackbarTheme,
  productBar: ProductBarTheme
}

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

LabelTheme {
  typography: {
    titleL: TextStyle,
    titleM: TextStyle,
    regular: TextStyle,
    subtle: TextStyle
  }
}

ImageTheme {
  shapes: {
    imageL: Shape,
    imageS: Shape
  },
  icons: {
    imageError36: Icon
  }
}

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
