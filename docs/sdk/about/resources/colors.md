---
hide:
  - toc
---

# Colors

The table below contains all the colors used in the SDK:

!!! abstract ""
    :fontawesome-regular-eye-slash: &nbsp; This is optional and can be omitted if you are not using the corresponding feature

<!-- If these colors change, don't forget to update the corresponding styles in exta.css -->

| Key | Description | Default &nbsp; `#ARGB` |
| :-- | :---------- | :------ |
| `scheme` | Specifies whether the theme uses a light or dark color scheme.<br>The provided colors should match the selected scheme | :material-invert-colors: `light` |
| [**General**](#general) | |  
| `brand` | The main accent color of your application | :material-square-rounded:{ .cl-brand } `#FF4000FF` |
| `primary` | Primary text elements | :material-format-color-text:{ .cl-primary } `#FF000000` |
| `secondary` | Secondary text elements | :material-format-color-text:{ .cl-secondary } `#FF9F9F9F` |
| `onDark` | Preferably __light__ color in __any scheme__ to be used<br>on dark, brand and neutral backgrounds<br><br>:material-information:{ .cl-hint } It should be contrast enough with `brand` color | :material-square-rounded:{ .cl-on-dark } `#FFFFFFFF` |
| `onLight` | Preferably __dark__ color in __any scheme__ to be used<br>on light backgrounds<br><br>:material-information:{ .cl-hint } It should be high contrast with `onDark` color | :material-square-rounded:{ .cl-on-light } `#FF000000` |
| `background` | The main background color of the SDK and bottom sheets | :material-square-rounded:{ .cl-background } `#FFFFFFFF` |
| `screen` | Zero-elevation background color.<br><br>For full-screen mode in `dark` scheme, this color is used as<br>a background color, while bottom sheets inside the SDK will<br>still use the `background` color. In any scheme it will be used<br>for full-screen image galleries<br><br>:material-information:{ .cl-hint } It's actually supposed to be black or _close to black_ <br>in __any scheme__ | :material-square-rounded:{ .cl-screen } `#FF000000` |
| `neutral` | A neutral background color used for components | :material-square-rounded:{ .cl-neutral } `#FFF2F2F7` |
| `border` | The color used for component borders | :material-square-rounded:{ .cl-border } `#FFE5E5EA` |
| `outline` | Blur outlines and checkmark borders | :material-square-rounded:{ .cl-outline } `#FFC7C7CC` |
| [**Selection**](#selection) | |
| `selectionBackground` | Background color for selection snackbar | :material-square-rounded:{ .cl-selection-background } `#FF000000` |
| [**Error**](#error) | |
| `errorBackground` | Background color for error snackbar | :material-square-rounded:{ .cl-error-background } `#FFEF5754` |
| `errorPrimary` | Primary color for error text in the snackbar | :material-format-color-text:{ .cl-error-primary } `#FFFFFFFF` |
| [**ProductBar :octicons-arrow-right-24: Price**](#productbarprice) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `discountedPrice` | Color for discounted price text | :material-format-color-text:{ .cl-discounted-price } `#FFFB1010` |
| [**PowerBar**](#powerbar) | |
| `aiuta` | Color for Aiuta branding<br><br>:material-information:{ .cl-hint } This is not a fully customizable color,<br>you can choose between:<br>- `standard` to use the Aiuta brand color and<br>- `primary` to not highlight the Aiuta label. | :material-format-color-text:{ .cl-aiuta } `standard`{ title="#FF4000FF" } |
