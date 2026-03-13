---
template: scheme.html
hide:
  - toc
code_links:
  TextStyle: /sdk/developer/definitions/#textstyle
---
# [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/index.md#theme) Label
![component](/media/components/labels.png){ width=300 }

Typography and text styling for different label types across the interface.

```typescript
LabelTheme {
  typography {
    titleL: TextStyle // (1)!
    titleM: TextStyle // (2)!
    regular: TextStyle // (3)!
    subtle: TextStyle // (4)!
    footnote: TextStyle // (5)!
  }
}
```

1. Defines the text style for large titles, typically used for main headings and prominent text elements.
2. Specifies the text style for medium titles, commonly used for section headers and secondary headings.
3. Sets the text style for regular body text and standard content throughout the interface.
4. Determines the text style for subtle or less prominent text, often used for secondary information and supporting content.
5. Specifies the text style for footnotes and the smallest text elements in the interface.