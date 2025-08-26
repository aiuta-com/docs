---
hide:
  - toc
---
# Bottom Sheet Scheme

Bottom sheet presentation, including grabber appearance and sheet shape for both main SDK and internal sheets.

![component](/media/components/bottom-sheet-std.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/index.md#theme) Bottom Sheet

```typescript
BottomSheetTheme {
  shapes {
    bottomSheet: Shape // (1)!
    chipsButton: Shape // (2)!
  }

  grabber {
    width: Number // (3)!
    height: Number // (4)!
    topPadding: Number // (5)!
  }

  settings {
    extendDelimitersToTheRight: Bool // (6)!
    extendDelimitersToTheLeft: Bool // (7)!
  }
}

```

1. Sets the shape configuration for the bottom sheet container, controlling its visual appearance.
2. Configures the shape for chips-style buttons, determining their visual style.
3. Controls the width of the grabber handle used for dragging the bottom sheet.
4. Determines the height of the grabber handle for bottom sheet interaction.
5. Sets the vertical padding between the grabber and the top of the bottom sheet.
6. Controls whether the bottom sheet delimiters extend to the right edge.
7. Determines whether the bottom sheet delimiters extend to the left edge. 
