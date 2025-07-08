---
hide:
  - toc
---
# Error Snackbar Scheme

 Error message presentation, including error icons and retry button styling.

![component](/media/components/snack-error.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Error Snackbar

```typescript
ErrorSnackbarTheme {
  strings {
    defaultErrorMessage: String // (1)!
    tryAgainButton: String // (2)!
  }

  icons {
    error36: Icon // (3)!
  }

  colors {
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