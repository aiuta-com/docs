---
hide:
  - toc
---
# Page Bar Scheme

Navigation bar appearance, including title styling and navigation button icons.

![component](/media/components/pagebar-std.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Page Bar

```typescript
PageBarTheme {
  typography {
    pageTitle: TextStyle // (1)!
  }

  icons {
    back24: Icon // (2)!
    close24: Icon // (3)!
  }

  settings {
    preferCloseButtonOnTheRight: Bool // (4)!
  }
}

```

1. Defines the text style for page titles in the navigation bar, controlling the appearance of header text.
2. Specifies the icon used for the back navigation button.
3. Sets the icon for the close button.
4.  Controls the position of the close button, determining whether it appears on the right side of the navigation bar.

    !!! example ""

        === "Default &nbsp; `false`"

            ![PageBar](../../../../media/components/pagebar-std.png){ width=450 }

        === "`true`"

            ![PageBar](../../../../media/components/pagebar-rev.png){ width=450 } 