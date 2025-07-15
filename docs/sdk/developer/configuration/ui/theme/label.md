---
hide:
  - toc
---
# Label Scheme

Typography and text styling for different label types across the interface.

![component](/media/components/labels.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Label

```typescript
LabelTheme {
  typography {
    titleL: TextStyle // (1)!
    titleM: TextStyle // (2)!
    regular: TextStyle // (3)!
    subtle: TextStyle // (4)!
  }
}
```

1. Defines the text style for large titles, typically used for main headings and prominent text elements.
2. Specifies the text style for medium titles, commonly used for section headers and secondary headings.
3. Sets the text style for regular body text and standard content throughout the interface.
4. Determines the text style for subtle or less prominent text, often used for secondary information and supporting content. 