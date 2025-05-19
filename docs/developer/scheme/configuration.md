# Configuration Scheme

The configuration is structured as a hierarchical object that controls various aspects of the SDK's behavior, appearance, and functionality. The configuration is designed to be flexible and extensible, allowing for customization of features, UI elements, and behavior.

!!! not "Type Definitions"
    Please, refer to the [:octicons-arrow-right-24: platform specific types](platform-types.md) used in this scheme and the [:octicons-arrow-right-24: History Images](history-images.md) description

While the implementation details may vary, the core structure and naming conventions remain consistent across platforms to maintain a unified developer experience.

!!! tip "Annotations"
    Don't miss them - click :material-information-outline: for more details

## Configuration

```typescript
Configuration {
  auth: Auth // (1)!
  userInterface: UserInterface // (2)!
  features: Features // (3)!
  analytics: Analytics | null // (4)!
  debugSettings: DebugSettings // (5)!
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
      apiKey: String // (1)!
    }
    ```

    1.  The `apiKey` is used to authenticate all outgoing requests from the Aiuta SDK to the Aiuta API. This key ensures that the requests are linked to your account, allowing the SDK to access the necessary resources and services provided by Aiuta. 
    
        Please see [API documentation :octicons-link-external-24:](https://developer.aiuta.com/docs/start){:target="_blank"} obtaining credentials section for instructions on how to get your `apiKey`.
  
=== "Jwt"
    ```typescript
    JwtAuth {
      subscriptionId: String // (1)!
      getJwt: Callback(Map<String: String>) => String // (2)!
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

        !!! success "Returns"
            Non-empty string representing the generated JWT

        !!! failure "Throws"
            An error if the JWT cannot be generated. 
            
            If an error is thrown, the SDK will be unable to complete the tryOn request and will display an error message to the user

        See [JWT server-side auth example :octicons-link-external-24:](https://developer.aiuta.com/docs/server-side-auth-component){:target="_blank"} for more details on securely generating JWTs.

### [:material-arrow-up-left:](#configuration) User Interface
```typescript
UserInterface {
  presentationStyle: PresentationStyle // (1)!
  swipeToDismiss: SwipeToDismissPolicy // (2)!
  theme: Theme // (3)!
}

enum PresentationStyle {
  fullScreen // (4)!
  bottomSheet // (5)!
  pageSheet // (6)!
}

enum SwipeToDismissPolicy {
  allowAlways // (7)!
  allowHeaderSwipeOnly // (8)!
  protectTheNecessaryPages // (9)!
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
  color: ColorTheme // (1)!
  label: LabelTheme // (2)!
  image: ImageTheme // (3)!
  button: ButtonTheme // (4)!
  activityIndicator: ActivityIndicatorTheme // (11)!
  pageBar: PageBarTheme // (5)!
  bottomSheet: BottomSheetTheme // (6)!
  selectionSnackbar: SelectionSnackbarTheme // (7)!
  errorSnackbar: ErrorSnackbarTheme // (8)!
  productBar: ProductBarTheme // (9)!
  powerBar: PowerBarTheme // (10)!
}
```

1. [:material-arrow-down-left:](#color) Defines the color scheme, brand colors, and various color states for UI elements.
    
    !!! note ""
        [:octicons-arrow-right-24: Explore all colors :material-invert-colors:](../../about/resources/colors.md)

2. [:material-arrow-down-left:](#label) Typography and text styling for different label types across the interface.

3. [:material-arrow-down-left:](#image) Shapes, sizes, and error state icon for image views.

4. [:material-arrow-down-left:](#button) Buttons styles, including typography and shape configurations for different button sizes.

5. [:material-arrow-down-left:](#page-bar) Navigation bar appearance, including title styling and navigation button icons.

6. [:material-arrow-down-left:](#bottom-sheet) Bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

7. [:material-arrow-down-left:](#selection) Multi-selection interface for list views, including selection controls and action buttons.

8. [:material-arrow-down-left:](#error) Error message presentation, including error icons and retry button styling.

9. [:material-arrow-down-left:](#product) Product information display, including typography for product details and optional price styling.

10. [:material-arrow-down-left:](#powered-by) "Powered By Aiuta" branding element appearance within the interface.

11. [:material-arrow-down-left:](#activity-indicator) Appearance and customization of loading indicators.

###### [:material-arrow-up-left:](#theme) Color
```typescript
ColorTheme {
  scheme: ColorScheme // (1)!
  brand: Color // (2)!
  primary: Color // (3)!
  secondary: Color // (4)!
  onDark: Color // (5)!
  onLight: Color // (6)!
  background: Color // (7)!
  screen: Color // (8)!
  neutral: Color // (9)!
  border: Color // (10)!
  outline: Color // (11)!
}

enum ColorScheme {
  light // (12)!
  dark // (13)!
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
    titleL: TextStyle // (1)!
    titleM: TextStyle // (2)!
    regular: TextStyle // (3)!
    subtle: TextStyle // (4)!
  }
}
```

1. Defines the text style for large titles, typically used for main headings and prominent text elements.
2. Specifies the text style for medium titles, commonly used for section headers and secondary headings.
3. Sets the text style for regular body text and standard content throughout the interface.
4. Determines the text style for subtle or less prominent text, often used for secondary information and supporting content.

###### [:material-arrow-up-left:](#theme) Image
```typescript
ImageTheme {
  shapes: {
    imageL: Shape // (1)!
    imageS: Shape // (2)!
  },
  icons: {
    imageError36: Icon // (3)!
  }
}

```

1. Defines the shape configuration for large image views, allowing customization of the visual appearance for prominent images.
2. Specifies the shape configuration for small image views, enabling consistent styling for secondary or thumbnail images.
3. Sets the icon to be displayed when an image fails to load, providing visual feedback for error states.

###### [:material-arrow-up-left:](#theme) Button
```typescript
ButtonTheme {
  typography: {
    buttonM: TextStyle // (1)!
    buttonS: TextStyle // (2)!
  },
  shapes: {
    buttonM: Shape // (3)!
    buttonS: Shape // (4)!
  }
}

```

1. Defines the text style for a regular medium-sized buttons.
2. Specifies the text style for small buttons.
3. Sets the shape configuration for medium buttons.
4. Configures the shape for small buttons.

###### [:material-arrow-up-left:](#theme) Activity Indicator
```typescript
ActivityIndicatorTheme {
  icons: {
    loading14: Icon | null // (1)!
  },
  colors: {
    overlay: Color // (4)!
  }
  settings: {
    indicationDelay: Number // (2)!
    spinDuration: Number // (3)!
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

###### [:material-arrow-up-left:](#theme) Page Bar
```typescript
PageBarTheme {
  typography: {
    pageTitle: TextStyle // (1)!
  },
  icons: {
    back24: Icon // (2)!
    close24: Icon // (3)!
  },
  settings: {
    preferCloseButtonOnTheRight: Bool // (4)!
  }
}

```

1. Defines the text style for page titles in the navigation bar, controlling the appearance of header text.
2. Specifies the icon used for the back navigation button.
3. Sets the icon for the close button.
4.  Controls the position of the close button, determining whether it appears on the right side of the navigation bar.

    !!! example ""
        `false` by default

###### [:material-arrow-up-left:](#theme) Bottom Sheet
```typescript
BottomSheetTheme {
  typography: {
    iconButton: TextStyle // (1)!
    chipsButton: TextStyle // (2)!
  },
  shapes: {
    bottomSheet: Shape // (3)!
    chipsButton: Shape // (4)!
  },
  grabber: {
    width: Number // (5)!
    height: Number // (6)!
    topPadding: Number // (7)!
  },
  settings: {
    extendDelimitersToTheRight: Bool // (8)!
    extendDelimitersToTheLeft: Bool // (9)!
  }
}

```

1. Defines the text style for icon buttons within the bottom sheet.
2. Specifies the text style for chips-style buttons in the bottom sheet interface.
3. Sets the shape configuration for the bottom sheet container, controlling its visual appearance.
4. Configures the shape for chips-style buttons, determining their visual style.
5. Controls the width of the grabber handle used for dragging the bottom sheet.
6. Determines the height of the grabber handle for bottom sheet interaction.
7. Sets the vertical padding between the grabber and the top of the bottom sheet.
8. Controls whether the bottom sheet delimiters extend to the right edge.
9. Determines whether the bottom sheet delimiters extend to the left edge.

###### [:material-arrow-up-left:](#theme) Selection
```typescript
SelectionSnackbarTheme {
  strings: {
    select: String // (1)!
    cancel: String // (2)!
    selectAll: String // (3)!
    unselectAll: String // (4)!
  },
  icons: {
    trash24: Icon // (5)!
    check20: Icon // (6)!
  },
  colors: {
    selectionBackground: Color // (7)!
  }
}

```

1. Defines the text label for the select action button in the selection interface.
2. Specifies the text label for the cancel action button to dismiss the selection mode.
3. Sets the text label for the select all action to choose all available items.
4. Configures the text label for the unselect all action to deselect all chosen items.
5. Specifies the icon used for the delete action in the selection interface.
6. Sets the icon displayed to indicate selected items in the interface.
7. Controls the background color of the selection snackbar component.

###### [:material-arrow-up-left:](#theme) Error
```typescript
ErrorSnackbarTheme {
  strings: {
    defaultErrorMessage: String // (1)!
    tryAgainButton: String // (2)!
  },
  icons: {
    error36: Icon // (3)!
  },
  colors: {
    errorBackground: Color // (4)!
    errorPrimary: Color // (5)!
  }
}

```

1. Defines the default text message displayed when an error occurs in the interface.
2. Specifies the text label for the retry action button in the error snackbar.
3. Sets the icon displayed to indicate the error state in the snackbar.
4. Controls the background color of the error snackbar component.
5. Defines the primary color used for error-related elements in the snackbar.

###### [:material-arrow-up-left:](#theme) Product
```typescript
ProductBarTheme {
  prices: ProductBarPricesTheme | null // (1)!
  typography: {
    product: TextStyle // (2)!
    brand: TextStyle // (3)!
  },
  icons: {
    arrow16: Icon // (4)!
  },
  settings: {
    applyProductFirstImageExtraPadding: Bool // (5)!
  }
}

ProductBarPricesTheme {
  typography: {
    price: TextStyle // (6)!
  },
  colors: {
    discountedPrice: Color // (7)!
  }
}
```

1. Configures the price display settings for the product bar, including typography and colors for price elements.
2. Defines the text style for product names in the product bar.
3. Specifies the text style for brand names displayed in the product bar.
4. Sets the icon used to indicate expandable product details in the compact view.
5. Controls whether additional padding is applied to the first product image in the list.
6. Configures the text style specifically for price displays in the product bar.
7. Defines the color used to highlight discounted prices in the product bar.

###### [:material-arrow-up-left:](#theme) Powered By
```typescript
PowerBarTheme {
  strings: {
    poweredByAiuta: String // (1)!
  },
  colors: {
    aiuta: PowerBarColorScheme // (2)!
  }
}

enum PowerBarColorScheme {
  standard // (3)!
  primary // (4)!
}
```

1. Defines the text label for the "Powered By Aiuta" branding element in the interface.
2. Controls the color scheme used to highlight "Aiuta" in the `poweredByAiuta` label.
3. Uses the default Aiuta-brand color to highlight "Aiuta" in the `poweredByAiuta` label, which is :material-square-rounded:{ .cl-aiuta } `#FF4000FF`
4. Applies the [`primary` color](#color) to the entire label without highlighting "Aiuta".

### [:material-arrow-up-left:](#configuration) Features
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
2. [:material-arrow-down-left:](#oboarding) Sets up the onboarding process to guide users through the SDK's features and capabilities.
3. [:material-arrow-down-left:](#consent) Manages user consent options for data processing, which can be integrated with onboarding or used independently.
4. [:material-arrow-down-left:](#image-picker) Controls the image selection interface, allowing users to pick photos, take new ones, use predefined models, or access previous uploads.
5. [:material-arrow-down-left:](#try-on) Configures the core virtual try-on functionality for trying products virtually.
6. [:material-arrow-down-left:](#share) Enables sharing capabilities for generated try-on images with customizable options.
7. [:material-arrow-down-left:](#wishlist) Integrates with the host app's wishlist functionality for product management.

#### [:material-arrow-up-left:](#features) Welcome Screen
```typescript
WelcomeScreenFeature {
  images: {
    welcomeBackground: Image // (1)!
  },
  icons: {
    welcome82: Icon // (2)!
  },
  strings: {
    welcomeTitle: String // (3)!
    welcomeDescription: String // (4)!
    welcomeButtonStart: String // (5)!
  },
  typography: {
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
  strings: {
    onboardingButtonNext: String // (3)!
    onboardingButtonStart: String // (4)!
  },
  shapes: {
    onboardingImageL: Shape // (5)!
    onboardingImageS: Shape // (6)!
  },
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
  images: {
    onboardingHowItWorksItems: List<{ // (6)!
      itemPhoto: Image // (1)!
      itemPreview: Image // (2)!
    }>
  },
  strings: {
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
  images: {
    onboardingBestResultsGood: List<Image> // (1)!
    onboardingBestResultsBad: List<Image> // (2)!
  },
  icons: {
    onboardingBestResultsGood24: Icon // (3)!
    onboardingBestResultsBad24: Icon // (4)!
  },
  strings: {
    onboardingBestResultsPageTitle: String | null // (5)!
    onboardingBestResultsTitle: String // (6)!
    onboardingBestResultsDescription: String // (7)!
  },
  styles: {
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
      strings: {
        consentHtml: String // (1)!
      }
    }
    ```
    
    1. HTML content displayed at the bottom of the onboarding screen for embedded consent.

=== "Standalone Onboarding Page"
    ```typescript
    ConsentStandaloneOnboardingPageFeature {
      strings: {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      },
      icons: {
        consentTitle24: Icon // (6)!
      },
      styles: {
        drawBordersAroundConsents: Bool // (7)!
      },
      data: {
        consents: List<Consent> // (8)!
      },
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

=== "Standalone Image Picker Page"
    ```typescript
    ConsentStandaloneImagePickerPageFeature {
      strings: {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      },
      icons: {
        consentTitle24: Icon // (6)!
      },
      styles: {
        drawBordersAroundConsents: Bool // (7)!
      },
      data: {
        consents: List<Consent> // (8)!
      },
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
  images: {
    examples: List<Image> // (5)!
  }
  strings: {
    imagePickerTitleEmpty: String // (6)!
    imagePickerDescriptionEmpty: String // (7)!
    imagePickerButtonUploadImage: String // (8)!
  }
}
```

1.  [:material-arrow-down-left:](#camera) Configuration for camera functionality, allowing users to take new photos directly within the SDK.
2.  [:material-arrow-down-left:](#photo-gallery) Configuration for accessing and selecting images from the device's photo library.
3.  [:material-arrow-down-left:](#predefined-models) Configuration for using predefined model images as an alternative to user photos.
4.  [:material-arrow-down-left:](uploads-history) Configuration for managing and reusing previously uploaded images.
5.  List of exactly 2 example of input images to display in the image picker interface.
6.  Title text displayed above images when the image picker is empty.
7.  Description text shown when the image picker is empty.
8.  Label text for the button used to upload new photos.

###### [:material-arrow-up-left:](#image-picker) Camera
```typescript
ImagePickerCameraFeature {
  icons: {
    camera24: Icon // (1)!
  }
  strings: {
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
  icons: {
    gallery24: Icon // (1)!
  }
  strings: {
    galleryButtonSelectPhoto: String // (2)!
  }
}
```

1.  Icon displayed for the gallery button in the bottom sheet list.
2.  Label text for the button used to select a photo from the gallery.

###### [:material-arrow-up-left:](#image-picker) Predefined Models
```typescript
ImagePickerPredefinedModelFeature {
  icons: {
    selectModels24: Icon // (1)!
  }
  data: {
    preferredCategoryId: String // (2)!
  }
  strings: {
    predefinedModelPageTitle: String // (3)!
    predefinedModelOr: String // (4)!
    predefinedModelErrorEmptyModelsList: String // (5)!
    predefinedModelCategories: Map<String: String> // (6)!
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
  strings: {
    uploadsHistoryButtonNewPhoto: String // (1)!
    uploadsHistoryTitle: String // (2)!
    uploadsHistoryButtonChangePhoto: String // (3)!
  }
  styles: {
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
  tryOn: {
    loadingPage: TryOnLoadingPageFeature // (1)!
    inputImageValidation: TryOnInputImageValidationFeature // (2)!
    cart: TryOnCartFeature // (3)!
    fitDisclaimer: TryOnFitDisclaimerFeature | null // (4)!
    feedback: TryOnFeedbackFeature | null // (5)!
    generationsHistory: TryOnGenerationsHistoryFeature | null // (6)!
    otherPhoto: TryOnWithOtherPhotoFeature | null // (7)!
    settings: {
      isBackgroundExecutionAllowed: Bool // (8)!
      tryGeneratePersonSegmentation: Bool // (9)!
    }
    icons: {
      tryOn20: Icon // (10)!
    }
    strings: {
      tryOnPageTitle: String // (11)!
      tryOn: String // (12)!
    }
    styles: {
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
  strings: {
    tryOnLoadingStatusUploadingImage: String // (1)!
    tryOnLoadingStatusScanningBody: String // (2)!
    tryOnLoadingStatusGeneratingOutfit: String // (3)!
  }
  styles: {
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
  strings: {
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
  strings: {
    addToCart: String // (1)!
  }
  handler: {
    addToCartAction: Callback(String) // (2)!
  }
}
```

1.  Label text for the button that adds the current product to the cart.
2.  Callback function that handles adding a product to the cart using its identifier.

##### [:material-arrow-up-left:](#try-on) Fit Disclaimer
```typescript
TryOnFitDisclaimerFeature {
  icons: {
    info20: Icon | null // (1)!
  }
  strings: {
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
  icons: {
    like36: Icon // (2)!
    dislike36: Icon // (3)!
    gratitude40: Icon // (4)!
  }
  strings: {
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
  strings: {
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
  icons: {
    history24: Icon // (1)!
  }
  strings: {
    generationsHistoryPageTitle: String // (2)!
  }
  dataProvider: BuiltIn | Custom {
    generatedImages: Flow<GenegaredImage> // (3)!
    addGeneratedImages: Callback(GenegaredImage[]) // (4)!
    deleteGeneratedImages: Callback(GenegaredImage[]) // (5)!
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
  icons: {
    changePhoto24: Icon // (1)!
  }
}
```

1.  Icon displayed for the "Change Photo" action, allowing users to continue with a different photo.

#### [:material-arrow-up-left:](#features) Share
```typescript
ShareFeature {
  watermark: ShareWatermarkFeature | null // (1)!
  icons: {
    share24: Icon // (2)!
  }
  strings: {
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
  images: {
    logo: Image // (1)!
  }
}
```

1.  Logo image to be used as a watermark on shared content.

#### [:material-arrow-up-left:](#features) Wishlist
```typescript
WishlistFeature {
  icons: {
    wishlist24: Icon // (1)!
    wishlistFill24: Icon // (2)!
  }
  strings: {
    wishlistButtonAdd: String // (3)!
  }
  dataProvider: {
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

### [:material-arrow-up-left:](#configuration) Analytics
```typescript
Analytics {
  handler: {
    onAnalyticsEvent: Callback(AnalyticEvent) // (1)!
  }
}
```

1.  Callback function that processes analytics events generated by the SDK, allowing integration with external analytics services or custom event handling.

### [:material-arrow-up-left:](#configuration) DebugSettings
```typescript
DebugSettings {
  isLoggingEnabled: Bool // (1)!
  emptyStringsPolicy: ValidationPolicy // (2)!
  unavailableResourcesPolicy: ValidationPolicy // (3)!
  infoPlistDescriptionsPolicy: ValidationPolicy // (4)!
  listSizePolicy: ValidationPolicy // (5)!
}

enum ValidationPolicy {
  ignore // (6)!
  warning // (7)!
  fatal // (8)!
}
```

1.  Controls whether the SDK should log debug information, providing detailed logs to help developers understand its behavior.
2.  Validation policy for checking whether required strings in the SDK configuration are not empty, preventing runtime issues.
3.  Validation policy for checking whether required resources are available and properly configured.
4.  Validation policy for checking whether the `info.plist` file contains all required descriptions for enabled features.
5.  Validation policy for checking whether lists required by the SDK are of the correct size.
6.  Ignores all validation errors, allowing the SDK to proceed without taking any action.
7.  Logs validation errors to the console for debugging purposes without interrupting execution.
8.  Stops the application's execution with a fatal error when validation errors occur.
