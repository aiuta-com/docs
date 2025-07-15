---
hide:
  - toc
---
# Color Scheme

Defines the color scheme, brand colors, and various color states for UI elements.

![component](/media/components/colors-brand.png){ width=300 }

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/#theme) Color Theme

```typescript
ColorTheme {
  scheme: ColorScheme // (1)!
  brand: Color // (2)!
  primary: Color // (3)!
  secondary: Color // (4)!
  onDark: Color // (5)!
  onLight: Color // (6)!
  background: Color // (7)!
  screen: Color // (8)!
  neutral: Color // (9)!
  border: Color // (10)!
  outline: Color // (11)!
}
```

1.  Defines whether the SDK uses a light or dark theme.
    Provided colors should match the scheme.

2. Main accent color for primary actions and highlights throughout the interface.

    ![color](/media/components/colors-brand.png){ width=400 }

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-brand } `#FF4000FF`

3. Primary color used for main content labels and icons, and important information.

    ![color](/media/components/pagebar-std.png){ width=300 }

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-primary } `#FF000000`


4. Secondary color used for supporting content and less prominent information.

    ![color](/media/components/colors-secondary.png){ width=300 }

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-secondary } `#FF9F9F9F`

5. Preferably light color __in any scheme__ optimized for use on dark, brand, and neutral backgrounds.

    ![color](/media/components/button-contrast.png){ width=200 }

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-on-dark } `#FFFFFFFF`

6. Preferably dark color __in any scheme__ optimized for use on light backgrounds.

    ![color](/media/components/button-contrast-inverted.png){ width=200 }

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-on-light } `#FF000000`

7. Main background color used throughout the SDK interface.

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-background } `#FFFFFFFF`

8.  Zero-elevation background color.

    For the full-screen mode in the `dark` scheme, this color is used as a page background color, while bottom sheets inside the SDK will still use the `background` color. In any scheme, it will be used for full-screen image galleries.

    !!! note ""
        It's actually supposed to be black or close to black in any scheme.

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-screen } `#FF000000`

9. Neutral background color used for various UI components.

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-neutral } `#FFF2F2F7`

10. Color used for component borders and dividers.

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-border } `#FFE5E5EA`

11. Color used for blur outlines and checkmark borders.

    !!! example ""
        Default ARGB :material-square-rounded:{ .cl-outline } `#FFC7C7CC`


### [:material-arrow-up-left:](#color-theme) Color Scheme

```typescript
enum ColorScheme {
  light // (1)!
  dark // (2)!
}
```

1. Light theme with predominantly light colors in the design.

2. Dark theme with predominantly dark colors in the design. 

!!! note ""
    Affects the style of blur components

!!! note ""
    On __`iOS only`__ it affects the appearance of system screens (e.g., photo gallery, share activity, etc.) and ensures that their `UIUserInterfaceStyle` matches the selected style. For example, if the SDK is set to a light theme but the system theme on the device is dark, the system windows invoked by the SDK will still use the light theme.
    