---
hide:
  - toc
---
# Theme Scheme

Specifies the theme configuration settings that determine the appearance and style of the UI components within the SDK. This includes defining color schemes, typography, and other visual elements to ensure a cohesive and customizable user interface experience.

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/#user-interface) Theme

```typescript
Theme {
  color: ColorTheme // (1)!
  label: LabelTheme // (2)!
  image: ImageTheme // (3)!
  button: ButtonTheme // (4)!
  pageBar: PageBarTheme // (5)!
  bottomSheet: BottomSheetTheme // (6)!
  activityIndicator: ActivityIndicatorTheme // (11)!
  selectionSnackbar: SelectionSnackbarTheme // (7)!
  errorSnackbar: ErrorSnackbarTheme // (8)!
  productBar: ProductBarTheme // (9)!
  powerBar: PowerBarTheme // (10)!
}
```

1. [:material-arrow-down-left:](color) Defines the color scheme, brand colors, and various color states for UI elements.

    ![component](/media/components/colors-brand.png){ width=400 }

2. [:material-arrow-down-left:](label) Typography and text styling for different label types across the interface.

    ![component](/media/components/labels.png){ width=400 }

3. [:material-arrow-down-left:](image) Shapes, sizes, and error state icon for image views.

    ![component](/media/components/images.png){ width=400 }

4. [:material-arrow-down-left:](button) Buttons styles, including typography and shape configurations for different button sizes.

    ![component](/media/components/button-brand.png){ width=172 } ![component](/media/components/button-contrast-inverted.png){ width=200 }

5. [:material-arrow-down-left:](page-bar) Navigation bar appearance, including title styling and navigation button icons.

    ![component](/media/components/pagebar-std.png){ width=400 }

6. [:material-arrow-down-left:](bottom-sheet) Bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

    ![component](/media/components/bottom-sheet-std.png){ width=400 }

7. [:material-arrow-down-left:](selection) Multi-selection interface for list views, including selection controls and action buttons.

    ![component](/media/components/snack-selection.png){ width=400 }

8. [:material-arrow-down-left:](error) Error message presentation, including error icons and retry button styling.

    ![component](/media/components/snack-error.png){ width=400 }

9. [:material-arrow-down-left:](product-bar) Product information display, including typography for product details and optional price styling.
 
    ![component](/media/components/product-bar.png){ width=400 }

10. [:material-arrow-down-left:](powered-by) "Powered By Aiuta" branding element appearance.

    ![component](/media/components/power-bar.png){ width=150 }

11. [:material-arrow-down-left:](activity-indicator) Appearance and customization of loading indicators.

    ![component](/media/components/activity-indicator.png){ width=36}
