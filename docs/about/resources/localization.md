# Providing localized text content

The table below contains all the strings that may be localized or changed for the SDK:

- :material-check: __default__ value is included in the SDK but may be changed or localized
    
- :material-close: __sample__ value that needs to be provided explicitly

- :fontawesome-regular-eye-slash: __sample__ value that can be `null` to hide a label/text field

- :material-code-tags: this field supports subset of `html` tags (e.g., __`b`__, *`i`*, <u>`u`</u>)

- :material-link: this field supports links (`a href`)

- :material-shuffle: alternative variant

!!! tip 
    You can select the table content **excluding the header**, copy and paste it into Google Sheets for translation purposes. 


| Key                     | Default or sample value                                       |
| :---------------------- | :------------------------------------------------------------ |
| [**Welcome Screen**](../pages/welcome-screen.md)                                      | |  
| `welcomeTitle`          | :material-close: Try on you                                   |
| `welcomeDescription`    | :material-close: Welcome to our Virtual try-on.<br>Try on the item directly on your photo |
| `welcomeButtonStart`    | :material-close: Let's start                                  |
| [**Onboarding**](../pages/onboarding.md)                                              | |
| `onboardingButtonNext`  | :material-check: Next                                         |
| `onboardingButtonStart` | :material-check: Start                                        |
| [**Onboarding :octicons-arrow-right-24: HowItWorks**](../pages/onboarding.md#how-it-works) | |
| `onboardingHowItWorksPageTitle` | :material-code-tags: :material-close: :fontawesome-regular-eye-slash: How it works<br><br>:material-shuffle: `<b>Step 1/2</b> - How it works` |
| `onboardingHowItWorksTitle`     | :material-check: Try on before buying                 |
| `onboardingHowItWorksDescription` | :material-check: Upload a photo and see how items look on you |
| [**Onboarding :octicons-arrow-right-24: BestResults**](../pages/onboarding.md#best-results) | |
| `onboardingBestResultsPageTitle` | :material-code-tags: :material-close: :fontawesome-regular-eye-slash: For best results<br><br>:material-shuffle: `<b>Step 2/2</b> - For best results` |
| `onboardingBestResultsTitle`     | :material-close: For best results                    |
| `onboardingBestResultsDescription` | :material-close: Use a photo with good lighting,<br>stand straight a plain background |
| [**Consent :octicons-arrow-right-24: Embedded**](../pages/consent.md#embedded)        | |
| `consentHtml` | :material-code-tags: :material-link: :material-check: Your photos will be processed by <b><a href='https://aiuta.com/legal/terms-of-service.html'>Terms of Use</a> [^1] |
| [**Consent :octicons-arrow-right-24: Standalone**](../pages/consent.md#standalone)    | |
| `consentPageTitle` | :material-code-tags: :material-close: Consent page title           |
| `consentTitle`          | :material-close: Consent title                                |
| `consentDescriptionHtml` | :material-code-tags: :material-link: :material-close: Consent description |
| `consents[].html` | :material-code-tags: :material-link: :material-close: Consents      |
| `consentFooterHtml` | :material-code-tags: :material-link: :material-close: Consent footer |
| `consentButtonAccept`   | :material-close: Accept                                       |
| [**ImagePicker**](../pages/image-picker.md)                                           | |
| `imagePickerTitle`      | :material-check: Upload a photo of you                        |
| `imagePickerDescription` | :material-check: Select a photo where you are standing straight and clearly visible |
| `imagePickerButtonUploadPhoto` | :material-check: Upload a photo                        |
| [**ImagePicker :octicons-arrow-right-24: Camera**](../pages/image-picker.md#camera)   | |
| `cameraButtonTakePhoto` | :material-check: Take a photo                                 |
| `cameraPermissionTitle` | :material-check: Camera permission                            |
| `cameraPermissionDescription` | :material-check: Please allow access to the camera in the application settings |
| `cameraPermissionButtonOpenSettings` | :material-check: Settings                        |
| [**ImagePicker :octicons-arrow-right-24: Gallery**](../pages/image-picker.md#gallery) | |
| `galleryButtonSelectPhoto` | :material-check: Choose from library                       |
| [**ImagePicker :octicons-arrow-right-24: PredefinedModel**](../pages/image-picker.md#predefined-model) | |
| `predefinedModelsTitle` | :material-check: Select your model                            |
| `predefinedModelsOr`    | :material-check: Or                                           |
| `predefinedModelsEmptyListError` | :material-check: The models list is empty            |
| `predefinedModelsCategories` | :material-check: `{"man": "Men", "woman": "Women"}`      |
| [**ImagePicker :octicons-arrow-right-24: UploadsHistory**](../pages/image-picker.md#uploads-history) | |
| `uploadsHistoryButtonNewPhoto` | :material-check: + New photo or model<br><br>:material-shuffle: + Upload new photo [^2] |
| `uploadsHistoryTitle`   | :material-check: Previously used                              |
| `uploadsHistoryButtonChangePhoto` | :material-check: Change photo                       |
| [**TryOn**](../pages/try-on.md)                                                       | |
| `tryOnPageTitle`        | :material-check: Virtual Try-on                               |
| `tryOn`                 | :material-check: Try on                                       |
| [**TryOn :octicons-arrow-right-24: Loading**](../pages/try-on.md#loading)             | |
| `tryOnLoadingStatusUploadingImage` | :material-check: Uploading image                   |
| `tryOnLoadingStatusScanningBody` | :material-check: Scanning the body                   |
| `tryOnLoadingStatusGeneratingOutfit` | :material-check: Generating outfit               |
| [**TryOn :octicons-arrow-right-24: InputValidation**](../pages/try-on.md#input-validation) | |
| `invalidInputImageDescription` | :material-check: We couldn't detect<br>anyone in this photo |
| `invalidInputImageChangePhotoButton` | :material-check: Change photo                    |
| [**TryOn :octicons-arrow-right-24: Cart**](../pages/try-on.md#cart)                   | |
| `addToCart`             | :material-check: Add to cart                                  |
| [**TryOn :octicons-arrow-right-24: FitDisclaimer**](../pages/try-on.md#fit-disclaimer) | |
| `fitDisclaimerTitle`    | :material-check: Results may vary from real-life fit          |
| `fitDisclaimerDescription` | :material-check: Virtual try-on is a visualization tool<br>that shows how items might look and may not perfectly<br>represent how the item will fit in reality |
| `fitDisclaimerCloseButton` | :material-check: Close                                     |
| [**TryOn :octicons-arrow-right-24: Feedback**](../pages/try-on.md#feedback)           | |
| `feedbackTitle`         | :material-check: Can you tell us more?                        |
| `feedbackOptions`       | :material-check: `["This style isn't for me",`<br>`"The item looks off",`<br>`"I look different"]` |
| `feedbackButtonSkip`    | :material-check: Skip                                         |
| `feedbackButtonSend`    | :material-check: Send                                         |
| `feedbackGratitudeText` | :material-check: Thank you for your feedback                  |
| [**TryOn :octicons-arrow-right-24: Feedback :octicons-arrow-right-24: Other**](../pages/try-on.md#feedback-other) | |
| `feedbackOptionOther`   | :material-check: Other                                        |
| `otherFeedbackTitle`    | :material-check: Tell us what we could improve?               |
| `otherFeedbackButtonSend` | :material-check: Send feedback                              |
| `otherFeedbackButtonCancel` | :material-check: :fontawesome-regular-eye-slash: Cancel [^3] |
| [**TryOn :octicons-arrow-right-24: History**](../pages/try-on.md#history)             | |
| `generationsHistoryPageTitle` | :material-check: History                                |
| [**Share**](../pages/share.md)                                                        | |
| `shareButton`           | :material-check: Share                                        |
| [**Wishlist**](../pages/wishlist.md)                                                  | |
| `wishlistButtonAdd`     | :material-check: Wishlist                                     |
| [**Selection**](../pages/selection.md)                                                | |
| `select`                | :material-check: Select                                       |
| `cancel`                | :material-check: Cancel                                       |
| `selectAll`             | :material-check: Select all                                   |
| `unselectAll`           | :material-check: Unselect all                                 |
| [**Error**](../pages/error.md)                                                        | |
| `defaultErrorMessage`   | :material-check: Something went wrong.<br>Please try again later |
| `tryAgainButton`        | :material-check: Try again                                    |
| [**PowerBar**](../pages/power-bar.md)                                                 | |
| `poweredByAiuta`        | :material-check: Powered by Aiuta                             |

[^1]: `<b><a href='https://aiuta.com/legal/terms-of-service.html'>Terms of Use</a>`
[^2]: Use this variant if the try-on with models feature is disabled
[^3]: The Close button with a cross icon will be used if no string is specified