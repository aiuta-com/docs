---
hide:
  - toc
---
# Bottom Sheet Scheme

Bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

![component](/media/components/bottom-sheet-std.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Bottom Sheet

```typescript
BottomSheetTheme {
  typography {
    iconButton: TextStyle // (1)!
    chipsButton: TextStyle // (2)!
  }

  shapes {
    bottomSheet: Shape // (3)!
    chipsButton: Shape // (4)!
  }

  grabber {
    width: Number // (5)!
    height: Number // (6)!
    topPadding: Number // (7)!
  }

  settings {
    extendDelimitersToTheRight: Bool // (8)!
    extendDelimitersToTheLeft: Bool // (9)!
  }
}

```

1. Defines the text style for icon buttons within the bottom sheet.
2. Specifies the text style for chips-style buttons in the bottom sheet interface.
3. Sets the shape configuration for the bottom sheet container, controlling its visual appearance.
4. Configures the shape for chips-style buttons, determining their visual style.
5. Controls the width of the grabber handle used for dragging the bottom sheet.
6. Determines the height of the grabber handle for bottom sheet interaction.
7. Sets the vertical padding between the grabber and the top of the bottom sheet.
8. Controls whether the bottom sheet delimiters extend to the right edge.
9. Determines whether the bottom sheet delimiters extend to the left edge. 