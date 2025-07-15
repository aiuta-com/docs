---
hide:
  - toc
---
# Welcome Screen Scheme

Configures an optional [:material-window-open: welcome screen](/sdk/about/pages/welcome-screen.md) that introduces users to the SDK's functionality.

![Welcome Screen](/media/pages/welcome.png){width=120}

## [:material-arrow-up-left:](/sdk/developer/configuration/features.md#features) Welcome Screen Feature
```typescript
WelcomeScreenFeature {
  images {
    welcomeBackground: Image // (1)!
  }

  icons {
    welcome82: Icon // (2)!
  }

  strings {
    welcomeTitle: String // (3)!
    welcomeDescription: String // (4)!
    welcomeButtonStart: String // (5)!
  }

  typography {
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
