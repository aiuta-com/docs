---
hide:
  - toc
---

# Providing localized text content

The table below contains all the strings that may be localized or changed for the SDK:

!!! abstract ""
    :material-check: &nbsp; __default__ value is included in the SDK but may be changed or localized
        
    :material-close: &nbsp; __sample__ value that needs to be provided explicitly

    :fontawesome-regular-eye-slash: &nbsp; sample value that can be `null` [^5] to __hide__ a label/text field

    :material-code-tags: &nbsp; this field supports subset of `html` __tags__ (e.g., __`b`__, *`i`*, <u>`u`</u>)

    :material-link: &nbsp; this field supports __links__ (`a href`)

    :material-apple-keyboard-option: &nbsp; alternative variant

!!! tip 
    You can select the table content **excluding the header**, copy and paste it into Google Sheets for translation purposes. 

| Key |     | Default or sample value |
| :-- | :-: | ----------------------- |
| [**Welcome Screen**](/sdk/about/pages/welcome-screen.md) :fontawesome-regular-eye-slash:{ title="Optional" } | |  
| `welcomeTitle` | :material-close:{ title="Sample value" } | Try on you |
| `welcomeDescription` | :material-close:{ title="Sample value" } | Welcome to our Virtual try-on.<br>Try on the item directly on your photo |
| `welcomeButtonStart` | :material-close:{ title="Sample value" } | Let's start |
| [**Onboarding**](/sdk/about/pages/onboarding.md) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `onboardingButtonNext` | :material-check:{ title="Deafult value" } | Next |
| `onboardingButtonStart` | :material-check:{ title="Deafult value" } | Start |
| [**Onboarding :octicons-arrow-right-24: HowItWorks**](/sdk/about/pages/onboarding.md#how-it-works) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `onboardingHowItWorksPageTitle` | :material-code-tags:{ title="Supports html tags" } :material-close:{ title="Sample value" } :fontawesome-regular-eye-slash:{ title="Nullable to hide" }<br><br>:material-apple-keyboard-option:{ title="Alternative variant" } | How it works<br><br>`<b>Step 1/2</b> - How it works` |
| `onboardingHowItWorksTitle` | :material-check:{ title="Deafult value" } | Try on before buying |
| `onboardingHowItWorksDescription` | :material-check:{ title="Deafult value" } | Upload a photo and see how items look on you |
| [**Onboarding :octicons-arrow-right-24: BestResults**](/sdk/about/pages/onboarding.md#best-results) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `onboardingBestResultsPageTitle` | :material-code-tags:{ title="Supports html tags" } :material-close:{ title="Sample value" } :fontawesome-regular-eye-slash:{ title="Nullable to hide" }<br><br>:material-apple-keyboard-option:{ title="Alternative variant" } | For best results<br><br>`<b>Step 2/2</b> - For best results` |
| `onboardingBestResultsTitle` | :material-close:{ title="Sample value" } | For best results |
| `onboardingBestResultsDescription` | :material-close:{ title="Sample value" } | Use a photo with good lighting, stand straight a plain background |
| [**Consent :octicons-arrow-right-24: Embedded**](/sdk/about/pages/consent.md#embedded) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `consentHtml` | :material-code-tags:{ title="Supports html tags" } :material-link:{ title="Supports links" } :material-check:{ title="Deafult value" } [^1] | Your photos will be processed by <b><a href='https://aiuta.com/legal/terms-of-service.html'>Terms of Use</a> |
| [**Consent :octicons-arrow-right-24: Standalone**](/sdk/about/pages/consent.md#standalone) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `consentPageTitle` | :material-code-tags:{ title="Supports html tags" } :material-close:{ title="Sample value" } :fontawesome-regular-eye-slash:{ title="Nullable to hide" } | Consent page title |
| `consentTitle` | :material-close:{ title="Sample value" } | Consent title |
| `consentDescriptionHtml` | :material-code-tags:{ title="Supports html tags" } :material-link:{ title="Supports links" } :material-close:{ title="Sample value" } | Consent description |
| `consents[].html` | :material-code-tags:{ title="Supports html tags" } :material-link:{ title="Supports links" } :material-close:{ title="Sample value" } | Consents |
| `consentFooterHtml` | :material-code-tags:{ title="Supports html tags" } :material-link:{ title="Supports links" } :material-close:{ title="Sample value" } | Consent footer |
| `consentButtonAccept` | :material-close:{ title="Sample value" } | Accept |
| [**ImagePicker**](/sdk/about/pages/image-picker.md) | |
| `imagePickerTitle` | :material-check:{ title="Deafult value" } | Upload a photo of you |
| `imagePickerDescription` | :material-check:{ title="Deafult value" } | Select a photo where you are standing straight and clearly visible |
| `imagePickerButtonUploadPhoto` | :material-check:{ title="Deafult value" } | Upload a photo |
| [**ImagePicker :octicons-arrow-right-24: Camera**](/sdk/about/pages/image-picker.md#camera) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `cameraButtonTakePhoto` | :material-check:{ title="Deafult value" } | Take a photo |
| `cameraPermissionTitle` | :material-check:{ title="Deafult value" } | Camera permission |
| `cameraPermissionDescription` | :material-check:{ title="Deafult value" } | Please allow access to the camera in the application settings |
| `cameraPermissionButtonOpenSettings` | :material-check:{ title="Deafult value" } | Settings |
| [**ImagePicker :octicons-arrow-right-24: Gallery**](/sdk/about/pages/image-picker.md#gallery) | |
| `galleryButtonSelectPhoto` | :material-check:{ title="Deafult value" } | Choose from library |
| [**ImagePicker :octicons-arrow-right-24: PredefinedModel**](/sdk/about/pages/image-picker.md#predefined-model) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `predefinedModelsTitle` | :material-check:{ title="Deafult value" } | Select your model |
| `predefinedModelsOr` | :material-check:{ title="Deafult value" } | Or |
| `predefinedModelsEmptyListError` | :material-check:{ title="Deafult value" } | The models list is empty |
| `predefinedModelsCategories` | :material-check:{ title="Deafult value" } [^4] | `{"man": "Men", "woman": "Women"}` |
| [**ImagePicker :octicons-arrow-right-24: UploadsHistory**](/sdk/about/pages/image-picker.md#uploads-history) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `uploadsHistoryButtonNewPhoto` | :material-check:{ title="Deafult value" }<br><br>:material-apple-keyboard-option:{ title="Alternative variant" } [^2] | + New photo or model<br><br>+ Upload new photo |
| `uploadsHistoryTitle` | :material-check:{ title="Deafult value" } | Previously used |
| `uploadsHistoryButtonChangePhoto` | :material-check:{ title="Deafult value" } | Change photo |
| [**TryOn**](/sdk/about/pages/image-picker.md) | |
| `tryOnPageTitle` | :material-check:{ title="Deafult value" } | Virtual Try-on |
| `tryOn` | :material-check:{ title="Deafult value" } | Try on |
| [**TryOn :octicons-arrow-right-24: Loading**](/sdk/about/pages/loading-screen.md) | |
| `tryOnLoadingStatusUploadingImage` | :material-check:{ title="Deafult value" } | Uploading image |
| `tryOnLoadingStatusScanningBody` | :material-check:{ title="Deafult value" } | Scanning the body |
| `tryOnLoadingStatusGeneratingOutfit` | :material-check:{ title="Deafult value" } | Generating outfit |
| [**TryOn :octicons-arrow-right-24: InputValidation**](/sdk/about/pages/loading-screen.md#__tabbed_1_1) | |
| `invalidInputImageDescription` | :material-check:{ title="Deafult value" } | We couldn't detect anyone in this photo |
| `invalidInputImageChangePhotoButton` | :material-check:{ title="Deafult value" } | Change photo |
| [**TryOn :octicons-arrow-right-24: Cart**](/sdk/about/pages/results-screen.md) | |
| `addToCart` | :material-check:{ title="Deafult value" } | Add to cart |
| [**TryOn :octicons-arrow-right-24: FitDisclaimer**](/sdk/about/pages/results-screen.md#__tabbed_1_6) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `fitDisclaimerTitle` | :material-check:{ title="Deafult value" } | Results may vary from real-life fit |
| `fitDisclaimerDescription` | :material-check:{ title="Deafult value" } | Virtual try-on is a visualization tool that shows how items might look<br>and may not perfectly represent how the item will fit in reality |
| `fitDisclaimerCloseButton` | :material-check:{ title="Deafult value" } | Close |
| [**TryOn :octicons-arrow-right-24: Feedback**](/sdk/about/pages/results-screen.md#__tabbed_1_3) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `feedbackTitle` | :material-check:{ title="Deafult value" } | Can you tell us more? |
| `feedbackOptions` | :material-check:{ title="Deafult value" } | `["This style isn't for me",`<br>`"The item looks off",`<br>`"I look different"]` |
| `feedbackButtonSkip` | :material-check:{ title="Deafult value" } | Skip |
| `feedbackButtonSend` | :material-check:{ title="Deafult value" } | Send |
| `feedbackGratitudeText` | :material-check:{ title="Deafult value" } | Thank you for your feedback |
| [**TryOn :octicons-arrow-right-24: Feedback :octicons-arrow-right-24: Other**](/sdk/about/pages/results-screen.md#__tabbed_2_2) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `feedbackOptionOther` | :material-check:{ title="Deafult value" } | Other |
| `otherFeedbackTitle` | :material-check:{ title="Deafult value" } | Tell us what we could improve? |
| `otherFeedbackButtonSend` | :material-check:{ title="Deafult value" } | Send feedback |
| `otherFeedbackButtonCancel` | :material-check:{ title="Deafult value" } :fontawesome-regular-eye-slash:{ title="Nullable to hide" } [^3] | Cancel |
| [**TryOn :octicons-arrow-right-24: History**](/sdk/about/pages/results-screen.md#__tabbed_1_5) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `generationsHistoryPageTitle` | :material-check:{ title="Deafult value" } | History |
| [**Share**](/sdk/about/pages/results-screen.md) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `shareButton` | :material-check:{ title="Deafult value" } | Share |
| [**Wishlist**](/sdk/about/pages/results-screen.md#__tabbed_1_2) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `wishlistButtonAdd` | :material-check:{ title="Deafult value" } | Wishlist |
| [**Selection**](#) | |
| `select` | :material-check:{ title="Deafult value" } | Select |
| `cancel` | :material-check:{ title="Deafult value" } | Cancel |
| `selectAll` | :material-check:{ title="Deafult value" } | Select all |
| `unselectAll` | :material-check:{ title="Deafult value" } | Unselect all |
| [**Error**](/sdk/about/pages/loading-screen.md#__tabbed_1_2) | |
| `defaultErrorMessage` | :material-check:{ title="Deafult value" } | Something went wrong.<br>Please try again later |
| `tryAgainButton` | :material-check:{ title="Deafult value" } | Try again |
| [**PowerBar**](/sdk/about/pages/loading-screen.md) | |
| `poweredByAiuta` | :material-check:{ title="Deafult value" } | Powered by Aiuta |

[^5]: In most cases an empty string will have the same effect, but the SDK has validation for developers to check the configuration is correct. To clearly distinguish between erroneously empty strings and explicitly hidden ones, we recommend using `null`  to hide and never using empty strings.
[^1]: `<b><a href='https://aiuta.com/legal/terms-of-service.html'>Terms of Use</a>`
[^4]: 
    This is a map from models category identifiers to their names. 
    The `predefinedModelCategories` are usually should cover 2 categories 
    with ids `man` and `woman`, but can be extended in the future or by
    your agreement with Aiuta.
[^2]: Use this variant if the try-on with models feature is disabled
[^3]: The Close button with a cross icon will be used if no string is specified
