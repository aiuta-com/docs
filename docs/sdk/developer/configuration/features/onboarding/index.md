---
template: scheme.html
hide:
  - toc
code_links:
  OnboardingHowItWorksPageFeature: how-it-works/
  OnboardingBestResultsPageFeature: best-results/
  BuiltIn: /sdk/developer/definitions/#dataprovider
  Custom: /sdk/developer/definitions/#dataprovider
  Callback: /sdk/developer/definitions/#callback
  Observable: /sdk/developer/definitions/#observable
  Shape: /sdk/developer/definitions/#shape
  Bool: /sdk/developer/definitions/#bool
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Onboarding
![How It Works](/media/pages/how-it-works.png){ width=320 }

Sets up [:material-window-open: the onboarding](/sdk/about/pages/onboarding.md) process to guide users through the SDK's features and capabilities.

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

1. [:material-arrow-down-left:](how-it-works.md) Configures the first page of onboarding that demonstrates how virtual try-on works through interactive examples.
2. [:material-arrow-down-left:](best-results.md) Sets up an optional page showing examples of photos that yield the best try-on results.
3. Defines the text label for the navigation button to proceed to the next onboarding page.
4. Specifies the text label for the button that completes onboarding and starts the main interface.
5. Controls the shape configuration for large images displayed in the onboarding process.
6. Sets the shape configuration for small images used in the onboarding interface.
7. Provides an observable property that tracks whether the user has completed the onboarding process.
8. Defines the callback function to mark onboarding as completed when the user finishes the process.
