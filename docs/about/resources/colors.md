---
hide:
  - toc
---

# Colors

The table below contains all the colors used in the SDK:

!!! abstract ""
    :fontawesome-regular-eye-slash: &nbsp; This is optional and can be omitted if you are not using the corresponding feature

<!-- If these colors change, don't forget to update the corresponding styles in exta.css -->

| Key | Description | Default |
| :-- | :---------- | :------ |
| `scheme` | Specifies whether the theme uses a light or dark color scheme.<br>The provided colors should match the selected scheme | :material-invert-colors: `light` |
| [**General**](#general) | |  
| `brand` | The main accent color of your application | :material-square-rounded:{ .cl-brand } `#4000FF` |
| `primary` | Primary text elements and _optionally_<br>secondary button backgrounds | :material-format-color-text:{ .cl-primary } `#000000` |
| `secondary` | Secondary text elements | :material-format-color-text:{ .cl-secondary } `#9F9F9F` |
| `onDark` | Preferably light color in any scheme to be used<br>on dark, brand and neutral backgrounds | :material-square-rounded:{ .cl-on-dark } `#FFFFFF` |
| `onLight` | Preferably dark color in any scheme to be used<br>on light backgrounds | :material-square-rounded:{ .cl-on-light } `#000000` |
| `background` | The main background color of the SDK and bottom sheets | :material-square-rounded:{ .cl-background } `#FFFFFF` |
| `screen` | Zero-elevation background color.<br><br>For full-screen mode in `dark` scheme, this color is used as<br>a background color, while bottom sheets inside the SDK will<br>still use the `background` color. In any scheme it will be used<br>for full-screen image galleries<br><br>:material-information-box:{ .cl-hint } It's actually supposed to be black or _close to black_ in any scheme | :material-square-rounded:{ .cl-screen } `#000000` |
| `neutral` | A neutral background color used for components | :material-square-rounded:{ .cl-neutral } `#F2F2F7` |
| `border` | The color used for component borders | :material-square-rounded:{ .cl-border } `#E5E5EA` |
| `outline` | Blur outlines and checkmark borders | :material-square-rounded:{ .cl-outline } `#C7C7CC` |
| [**Selection**](#selection) | |
| `selectionBackground` | Background color for selection snackbar | :material-square-rounded:{ .cl-selection-background } `#000000` |
| [**Error**](#error) | |
| `errorBackground` | Background color for error snackbar | :material-square-rounded:{ .cl-error-background } `#EF5754` |
| `errorPrimary` | Primary color for error text in the snackbar | :material-format-color-text:{ .cl-error-primary } `#FFFFFF` |
| [**ProductBar :octicons-arrow-right-24: Price**](#productbarprice) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `discountedPrice` | Color for discounted price text | :material-format-color-text:{ .cl-discounted-price } `#FB1010` |
| [**PowerBar**](#powerbar) | |
| `aiuta` | Color for Aiuta branding<br><br>:material-information-box:{ .cl-hint } This is not a fully customizable color,<br>you can choose between:<br>- `standard` to use the Aiuta brand color and<br>- `primary` to not highlight the Aiuta label. | :material-format-color-text:{ .cl-aiuta } `standard`{ title="#4000FF" } |
