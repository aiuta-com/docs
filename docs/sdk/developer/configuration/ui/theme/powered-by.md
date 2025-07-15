---
hide:
  - toc
---
# Power Bar Scheme

"Powered By Aiuta" branding element appearance.

![component](/media/components/power-bar.png){ width=120 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Power Bar

```typescript
PowerBarTheme {
  strings {
    poweredByAiuta: String // (1)!
  }

  colors {
    aiuta: PowerBarColorScheme // (2)!
  }
}
```

1. Defines the text label for the "Powered By Aiuta" branding element in the interface.
2. Controls the color scheme used to highlight "Aiuta" in the `poweredByAiuta` label.

### [:material-arrow-up-left:](#power-bar) Color Scheme

```typescript
enum PowerBarColorScheme {
  standard // (1)!
  primary // (2)!
}
```

1. Uses the default Aiuta-brand color to highlight "Aiuta" in the `poweredByAiuta` label, which is :material-square-rounded:{ .cl-aiuta } `#FF4000FF`
2. Applies the [`primary` color](color.md) to the entire label without highlighting "Aiuta". 
