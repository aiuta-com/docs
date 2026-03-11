---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  String: /sdk/developer/definitions/#string
---
# [:material-arrow-up-left:](index.md#try-on-feature) Fit Disclaimer

![Fit Disclaimer](/media/pages/results-fit.png){ width=220 }

Optional configuration for displaying fit disclaimers to users.
```typescript
TryOnFitDisclaimerFeature {
  icons {
    info20: Icon | null // (1)!
  }

  strings {
    fitDisclaimerTitle: String // (2)!
    fitDisclaimerDescription: String // (3)!
    fitDisclaimerButtonClose: String // (4)!
  }
}
```

1.  Optional icon displayed in the fit disclaimer to provide visual context.
2.  Title text displayed in the fit disclaimer message.
3.  Detailed description text explaining the fit disclaimer information.
4.  Label text for the button that dismisses the fit disclaimer.
