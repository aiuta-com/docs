---
hide:
  - toc
---
# Selection Snackbar Scheme

Multi-selection interface for list views, including selection controls and action buttons.

![component](/media/components/snack-selection.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/index.md#theme) Selection Snackbar

```typescript
SelectionSnackbarTheme {
  strings {
    select: String // (1)!
    cancel: String // (2)!
    selectAll: String // (3)!
    unselectAll: String // (4)!
  }

  icons {
    trash24: Icon // (5)!
    check20: Icon // (6)!
  }

  colors {
    selectionBackground: Color // (7)!
  }
}

```

1. Defines the text label for the select action button in the selection interface.
2. Specifies the text label for the cancel action button to dismiss the selection mode.
3. Sets the text label for the select all action to choose all available items.
4. Configures the text label for the unselect all action to deselect all chosen items.
5. Specifies the icon used for the delete action in the selection interface.
6. Sets the icon displayed to indicate selected items in the interface.
7. Controls the background color of the selection snackbar component. 