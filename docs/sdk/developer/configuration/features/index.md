---
template: scheme.html
hide:
  - toc
code_links:
  WelcomeScreenFeature: welcome-screen/
  OnboardingFeature: onboarding/
  ConsentFeature: consent/
  ImagePickerFeature: image-picker/
  TryOnFeature: try-on/
  ShareFeature: share/
  WishlistFeature: wishlist/
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](/sdk/developer/configuration/index.md#configuration) Features
Describes the set of features enabled in the SDK for the users and their interaction with the app.

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

1. [:material-arrow-down-left:](welcome-screen.md) Configures an optional welcome screen that introduces users to the SDK's functionality.
2. [:material-arrow-down-left:](onboarding/index.md) Sets up the onboarding process to guide users through the SDK's features and capabilities.
3. [:material-arrow-down-left:](consent/index.md) Manages user consent options for data processing, which can be integrated with onboarding or used independently.
4. [:material-arrow-down-left:](image-picker/index.md) Controls the image selection interface, allowing users to pick photos, take new ones, use predefined models, or access previous uploads.
5. [:material-arrow-down-left:](try-on/index.md) Configures the core virtual try-on functionality for trying products virtually.
6. [:material-arrow-down-left:](share/index.md) Enables sharing capabilities for generated try-on images with customizable options.
7. [:material-arrow-down-left:](wishlist.md) Integrates with the host app's wishlist functionality for product management.
