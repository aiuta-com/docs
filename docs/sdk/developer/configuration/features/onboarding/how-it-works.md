---
template: scheme.html
hide:
  - toc
code_links:
  Image: /sdk/developer/definitions/#image
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
---
# How It Works

Configures the first page of onboarding that demonstrates how virtual try-on works through interactive examples.

![How It Works](/media/pages/how-it-works-1.png){ width=120 }

## [:material-arrow-up-left:](index.md#onboarding-feature) OnboardingHowItWorksPageFeature

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
