# Onboarding Scheme

Sets up [:material-window-open: the onboarding](/sdk/about/pages/onboarding.md) process to guide users through the SDK's features and capabilities.

![How It Works](/media/pages/how-it-works.png){ width=220 }

## [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Onboarding Feature
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

## Slides

---

### [:material-arrow-up-left:](#onboarding-feature) How It Works

![How It Works](/media/pages/how-it-works-1.png){ width=120 }

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

### [:material-arrow-up-left:](#onboarding-feature) Best Results

![Best Results](/media/pages/best-results.png){ width=120 }

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

!!! warning "Deprecated"
    Examples of good source photos are now included into the [Image Picker](/sdk/developer/configuration/features/image-picker.md), so we recommend disabling this slide to avoid overwhelming the user with onboarding