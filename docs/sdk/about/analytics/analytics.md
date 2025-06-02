# Analytics Events

This document describes the analytics events that can be tracked within the Aiuta SDK. These events are triggered in response to user actions or state changes and can be used to track user interactions or system behaviors in your analytics system.

## Event Types

| Type | Parameters | Description | 
| :--- |  :-------- | :---------- |
| `configure` | [`*`](#configuration) | SDK was configured with a features set |
| `session`   | [`flow`](#session) | Start of a new session, SDK about to present it's UI<br>The page event is expected to be the following |
| `page` | [`pageId`](#page)<br>[`productIds`](#products) | Navigation to a specific page in the SDK UI |
| `onboarding` | [`event`](#onboarding)<br>[`pageId`](#page)<br>[`productIds`](#products) | Interactions during the onboarding process, including viewing<br>informational screens and providing necessary consents for<br>data processing |
| `picker` | [`event`](#picker)<br>[`pageId`](#page)<br>[`productIds`](#products) | Interactions with the image selection interface, including camera<br>access, gallery selection, and predefined model selection |
| `tryOn` | [`event`](#try-on)<br>[`pageId`](#page)<br>[`productIds`](#products) | Virtual try-on operations reports, including photo upload,<br>processing status, and completion or error states |
| `results` | [`event`](#results)<br>[`pageId`](#page)<br>[`productIds`](#products) | Interactions with the generated try-on results, including sharing,<br>saving to wishlist, adding to cart, or requesting new generations |
| `feedback` | [`event`](#feedback)<br>[`pageId`](#page)<br>[`productIds`](#products) | Feedback on the generated results, including positive ratings and<br>detailed negative feedback with optional comments |
| `history` | [`event`](#history)<br>[`pageId`](#page)<br>[`productIds`](#products) | Interactions with previously generated results<br>and managing saved generations |
| `share` | [`event`](#share)<br>[`pageId`](#page)<br>[`productIds`](#products) | Events related to the user's desire to share/save generated images |
| `exit` | [`pageId`](#page)<br>[`productIds`](#products) | Exit from the SDK on a specific page,<br>indicating the final point in the user's journey |

## Identifiers

Identifiers to track navigation pages, products, and 3rd party apps in the Aiuta SDK.

### Page

| Page | Description |
| :--- | :---------- |
| `welcome` | Optional [Welcome Screen](../pages/welcome-screen.md) that introduces users to the SDK functionality<br>and provides an entry point to start the try-on process |
| `howItWorks` | Informational screen explaining the virtual try-on process,<br>including samples of expected outcomes |
| `bestResults` | Guide screen showing best practices for achieving optimal<br>try-on results with example images and tips |
| `consent` | Screen for obtaining user consent for data processing and<br>privacy policy acceptance in standalone mode |
| `imagePicker` | Interface for selecting or capturing images, including camera<br>access, gallery browsing, uploads history, and predefined model selection |
| `loading` | Transition screen displayed during image processing and<br>virtual try-on generation |
| `results` | Screen displaying generated try-on results with options to<br>share, save, or request new generations |
| `history` | Screen showing previously generated try-on results with<br>options to view, share, or manage saved generations |


### Products

This is a list of product identifiers in the context of the current try-on session or other SDK interaction. It can be empty, for example, when opening a separate screen to view the user's generation history, where there is no try-on context. In the case of a single try-on, the list will contain one identifier. Accordingly, when using multi-try-on, the list will contain identifiers of all products from the outfit.

### App

A string representing 3rd party app/package/bundle id that was used to receive data from the SDK directly or through system APIs.

## Specific Events

Types, except for `page`, `exit`, `configure` and `session`, contain an `event` parameter that indicates which specific event occurred in that type.

!!! tip "Compatibility"
    In widely used analytics systems, events usually have `name`s and `parameters`. For structure, we wanted to group events into more general `types` and detail them according to specific `events` within the group. You can consider this as a `subtype`, or combine the `type` and `event` into a single event `name`.

### Onboarding

| Event | Parameters | Description | 
|-------|------------|-------------|
| `welcomeStartClicked` | :material-minus: | Initial interaction with the [Welcome Screen](../pages/welcome-screen.md), indicating<br>user's intent to begin the try-on process |
| `onboardingFinished` | :material-minus: | Completion of all onboarding steps |
| `consentsGiven` | `consentIds` | Explicit acceptance of required consents, including<br>data processing and privacy policy agreements |

### Picker

| Event | Description |
|-------|-------------|
| | __Camera__ |
| `cameraOpened` | Activation of the device camera for capturing new<br>photos for the try-on process |
| `newPhotoTaken` | Successful capture of a new photo using the<br>device camera |
| | __System Photos__ |
| `photoGalleryOpened` | Access to the device's photo gallery for selecting<br>existing images |
| `galleryPhotoSelected` | Selection of an existing photo from the device's<br>gallery for try-on |
| | __Uploads history__ |
| `uploadsHistoryOpened` | Access to previously uploaded photos within the<br>SDK's history |
| `uploadedPhotoSelected` | Selection of a previously uploaded photo from<br>the SDK's history |
| `uploadedPhotoDeleted` | Removal of a previously uploaded photo from<br>the SDK's history |
| | __Predefined models__ |
| `predefinedModelsOpened` | Access to the list of predefined model images<br>available for try-on |
| `predefinedModelSelected` | Selection of a predefined model image for<br>the try-on process |

### Try-On

| Event | Parameters |  Description |
|-------|------------|-------------|
| `initiated` | :material-minus: | Start processing photo |
| `photoUploaded` | :material-minus: | Successful upload of a selected or captured<br>photo for processing |
| `tryOnStarted` | :material-minus: | Initiation of the virtual try-on process with<br>the selected image |
| `tryOnFinished` | `uploadDuration`<br>`tryOnDuration`<br>`downloadDuration`<br>`totalDuration` [^1] | Successful completion of the virtual try-on<br>process with generated results<br>`Duration` of each step and the entire process<br>in seconds (floating-point) |
| `tryOnAborted` | [`abortReason`](errors.md#aborts) | Cancellation of the try-on process before<br>completion |
| `tryOnError` | [`errorType`](errors.md#errors)<br>`errorMessage` | Occurrence of an error during the try-on process,<br>requiring user attention. `errorMessage` contains<br>information for developers and is not for users |

### Results

| Event | Description |
|-------|-------------|
| `productAddToWishlist` | Adding of a product from the try-on results<br>to the user's wishlist |
| `productAddToCart` | Adding of a product from the try-on results<br>to the shopping cart |
| `pickOtherPhoto` | Request to start a new try-on process with<br>a different photo |

### Feedback

| Event | Parameters | Description | 
|-------|------------|-------------|
| `positive` | :material-minus: | The user left positive feedback on try-on results with<br>no specific issues reported |
| `negative` | `option`<br>`text` | The user report of issues with try-on results, including<br>specific problem category and optional<br>detailed feedback |

### History

| Event | Description |
|-------|-------------|
| `generatedImageDeleted` | Removal of a previously generated try-on<br>result from the history |

### Share

| Event | Parameters | Description |
|-------|------------|-------------|
| `initiated` | :material-minus: | The user clicked the share button<br> a system dialog will be displayed |
| `succeeded` | [`targetId`](#app) | The images were successfully shared to the 3rd party application |
| `canceled` [^2] | [`targetId?`](#app) | The user canceled the share process |
| `failed` [^2] | [`targetId?`](#app) | A system error occurred while sharing images |
| `screenshot` | :material-minus: | The user took a screenshot of the SDK [page](#page) |

## Parameters

### Configuration

| Parameter |
|-----------|
| [`authenticationType`](../developer/configuration.md#auth) |
| [`welcomeScreenFeatureEnabled`](../developer/features.md#welcome-screen) |
| [`onboardingFeatureEnabled`](../developer/features.md#onboarding) |
| [`consentFeatureType`](../developer/features.md#consent) |
| [`imagePickerCameraFeatureEnabled`](../developer/features.md#camera) |
| [`imagePickerPredefinedModelFeatureEnabled`](../developer/features.md#predefined-models) |
| [`imagePickerUploadsHistoryFeatureEnabled`](../developer/features.md#uploads-history) |
| [`tryOnFitDisclaimerFeatureEnabled`](../developer/features.md#fit-disclaimer) |
| [`tryOnFeedbackFeatureEnabled`](../developer/features.md#feedback) |
| [`tryOnFeedbackOtherFeatureEnabled`](../developer/features.md#other) |
| [`tryOnGenerationsHistoryFeatureEnabled`](../developer/features.md#generations-history) |
| [`tryOnWithOtherPhotoFeatureEnabled`](../developer/features.md#other-photo) |
| [`shareFeatureEnabled`](../developer/features.md#share) |
| [`shareWatermarkFeatureEnabled`](../developer/features.md#watermark) |
| [`wishlistFeatureEnabled`](../developer/features.md#wishlist) |


### Session

| Flow | Description |
|-------|-------------|
| `tryOn` | Starting the SDK with tryOn flow to upload photo and generate results |
| `history` | Starting the SDK to show previously generated gallery |

[^1]: The `totalDuration` time from when the user clicks the "Try On" button to when the results are displayed.
      It may be greater than the sum of the `uploadDuration`, `tryOnDuration`, and `downloadDuration` as it includes the request to start the operation and internal transitions.
[^2]: Available only on iOS.
