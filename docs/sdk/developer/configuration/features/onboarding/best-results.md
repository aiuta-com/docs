---
template: scheme.html
hide:
  - toc
code_links:
  Bool: /sdk/developer/definitions/#bool
  Icon: /sdk/developer/definitions/#icon
  Image: /sdk/developer/definitions/#image
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](index.md#onboarding) Best Results Page

![Best Results](/media/pages/best-results.png){ width=220 }

Sets up an optional page showing examples of photos that yield the best try-on results.

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
    Examples of good source photos are now included into the [Image Picker](/sdk/developer/configuration/features/image-picker/index.md), so we recommend disabling this slide to avoid overwhelming the user with onboarding
