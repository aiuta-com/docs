# Custom CSS Configuration

The Web SDK supports custom CSS styling through the `customCssUrl` parameter in the configuration. This allows you to customize the appearance of UI components to match your brand and design system.

## Configuration

Custom CSS is configured in the `userInterface` section of the SDK configuration as shown in the [Web SDK documentation](/sdk/web/index.md):

```javascript
const aiuta = new Aiuta({
  userInterface: {
    customCssUrl: "https://your-domain.com/path/to/aiuta-custom.css"
  }
});
```

## CSS Variables

The Web SDK uses CSS custom properties (variables) that you can override in your custom CSS file. All variables follow the `--aiuta-` prefix pattern, adhering to the naming convention from the [general theme documentation](/sdk/developer/configuration/ui/theme/index.md).

### Color Scheme

```css
:root {
  /* Brand Colors */
  --aiuta-color-brand: #4000FF;
  --aiuta-color-primary: #000000;
  --aiuta-color-secondary: #9F9F9F;
  
  /* Text Colors */
  --aiuta-color-on-dark: #FFFFFF;
  --aiuta-color-on-light: #000000;
  
  /* Background Colors */
  --aiuta-color-background: #FFFFFF;
  --aiuta-color-screen: #000000;
  --aiuta-color-neutral: #F2F2F7;
  --aiuta-color-border: #E5E5EA;
}
```

### Typography

```css
:root {
  /* Global Typeface */
  --aiuta-typeface: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  
  /* Label Typography */
  --aiuta-label-title-l-font-size: 24px;
  --aiuta-label-title-l-font-weight: 600;
  
  --aiuta-label-title-m-font-size: 20px;
  --aiuta-label-title-m-font-weight: 600;
  
  --aiuta-label-regular-font-size: 16px;
  --aiuta-label-regular-font-weight: 400;
  
  --aiuta-label-subtle-font-size: 14px;
  --aiuta-label-subtle-font-weight: 400;
  
  /* Button Typography */
  --aiuta-button-m-font-size: 16px;
  --aiuta-button-m-font-weight: 500;
  
  --aiuta-button-s-font-size: 14px;
  --aiuta-button-s-font-weight: 500;
  
  /* Page Bar Typography */
  --aiuta-page-title-font-size: 18px;
  --aiuta-page-title-font-weight: 600;
}
```

### Component Shapes

```css
:root {
  /* Button Shapes */
  --aiuta-button-m-border-radius: 8px;
  --aiuta-button-s-border-radius: 6px;
  
  /* Image Shapes */
  --aiuta-image-l-border-radius: 12px;
  --aiuta-image-s-border-radius: 8px;
  
  /* Bottom Sheet Shapes */
  --aiuta-bottom-sheet-border-radius: 16px;
}
```

### Component Colors

```css
:root {
  /* Selection Snackbar */
  --aiuta-selection-background: #F2F2F7;
  
  /* Error Snackbar */
  --aiuta-error-background: #FFEBEE;
  --aiuta-error-primary: #D32F2F;
  
  /* Activity Indicator */
  --aiuta-activity-overlay: rgba(0, 0, 0, 0.3);
}
```

## Example Custom CSS

Here's an example of a custom CSS file that overrides the brand color, typeface, and some component styling:

```css
:root {
  /* Override brand color to match your brand */
  --aiuta-color-brand: #000000;
  
  /* Set custom typeface for all text */
  --aiuta-typeface: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  
  /* Customize primary text color */
  --aiuta-color-primary: #1A1A1A;
  
  /* Override button styling */
  --aiuta-button-m-border-radius: 12px;
  --aiuta-button-m-font-weight: 600;
  
  /* Customize bottom sheet appearance */
  --aiuta-bottom-sheet-border-radius: 20px;
  --aiuta-grabber-background-color: #000000;
}
```

## Typography System

The Web SDK uses a unified typography system where all text elements inherit from the `--aiuta-typeface` variable. This means:

- **Single font control**: Change `--aiuta-typeface` to update all text across the SDK
- **Consistent appearance**: All components use the same font family by default
- **Easy customization**: Override individual font properties (size, weight) as needed
- **Fallback support**: The default typeface includes system fonts for optimal cross-platform compatibility

## Notes

- All CSS variables are optional - only override the ones you need to customize
- The SDK will fall back to default values for any variables not defined in your custom CSS
- The `--aiuta-typeface` variable applies to all text elements automatically
- Make sure your custom CSS file is accessible via HTTPS when using the SDK in production
- Test your customizations across different devices and screen sizes to ensure compatibility

## Roadmap

We're continuously working to expand the Web SDK's styling capabilities:

1. **Extended Styling System**: Expand the CSS variable system to provide greater alignment with the [general configuration scheme](/sdk/developer/configuration/ui/theme/index.md), including support for all theme components and advanced styling options available on other platforms.

2. **Granular Element Customization**: Add the ability to fully customize specific elements on specific SDK pages with complete CSS capabilities, allowing developers to target individual components and pages for maximum design flexibility.
