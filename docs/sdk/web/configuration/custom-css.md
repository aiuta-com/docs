# Custom CSS Configuration

The Web SDK supports custom CSS styling through the `customCssUrl` parameter in the configuration. This allows you to customize the appearance of UI components to match your brand and design system.

## Configuration

Custom CSS is configured in the `userInterface` section of the SDK configuration as shown in the [Web SDK documentation](/sdk/web/index.md):

```javascript
const aiuta = new Aiuta({
  userInterface: {
    theme: {
      customCssUrl: 'https://your-domain.com/path/to/aiuta-custom.css',
    },
  },
})
```

!!! warn "Cross-Origin Access Required"

    Your custom CSS file must be accessible for loading from the Aiuta SDK iframe hosted on `static.aiuta.com`. Make sure to configure proper CORS headers on your server:

    ```
    Access-Control-Allow-Origin: https://static.aiuta.com
    Access-Control-Allow-Methods: GET
    Access-Control-Allow-Headers: Content-Type
    ```

    Alternatively, you can allow all origins during development (not recommended for production):

    ```
    Access-Control-Allow-Origin: *
    ```

## CSS Variables

The Web SDK uses CSS custom properties (variables) that you can override in your custom CSS file. All variables follow the `--aiuta-` prefix pattern, adhering to the naming convention from the [general theme documentation](/sdk/developer/configuration/ui/theme/index.md).

### Color Scheme

```css
:root {
  /* Brand & Primary Colors */
  --aiuta-color-brand: #000000;
  --aiuta-color-try-on: #4000ff;
  --aiuta-color-primary: #000000;
  --aiuta-color-secondary: #9f9f9f;

  /* Contextual Colors (FOR USE ON SPECIFIC BACKGROUNDS ONLY) */
  --aiuta-color-on-dark: #ffffff; /* White text for use ON dark/brand backgrounds */
  --aiuta-color-on-light: #000000; /* Dark text for use ON light backgrounds (use sparingly) */

  /* Background Colors */
  --aiuta-color-background: #ffffff;
  --aiuta-color-neutral: #f2f2f7;
  --aiuta-color-border: #e5e5ea;

  /* Selection */
  --aiuta-color-selection-background: #000000;

  /* Error */
  --aiuta-color-error-background: #ef5754;

  /* Screen dim for modals */
  --aiuta-color-screen-dim: rgba(0, 0, 0, 0.7);
}
```

### Typography

The Web SDK uses CSS classes for typography styling. You can override these classes in your custom CSS:

```css
/* Global font family */
:root {
  --aiuta-typeface:
    'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, 'Noto Sans',
    sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
}

/* Page Title */
.aiuta-page-title {
  font-size: 17px;
  font-weight: 500;
  line-height: 22px;
}

/* Titles */
.aiuta-title-l {
  font-size: 24px;
  font-weight: 700;
  line-height: normal;
}

.aiuta-title-m {
  font-size: 20px;
  font-weight: 600;
  line-height: normal;
}

/* Labels */
.aiuta-label-regular {
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.aiuta-label-subtle {
  font-size: 13px;
  font-weight: 400;
  line-height: 18px;
}

.aiuta-label-disclaimer {
  font-size: 11px;
  font-weight: 400;
  line-height: 18px;
  letter-spacing: 0.22px;
}

/* Buttons */
.aiuta-button-m {
  font-size: 17px;
  font-weight: 500;
  line-height: 18px;
}

.aiuta-button-s {
  font-size: 14px;
  font-weight: 500;
  line-height: 18px;
  letter-spacing: -0.14px;
}
```

### Component Shapes

The Web SDK uses CSS classes for component shapes. You can override these classes in your custom CSS:

```css
/* Shape for desktop app container and modal popups */
.aiuta-modal {
  border-radius: 24px;
  box-shadow:
    0 8px 28px -6px rgba(0, 0, 0, 0.12),
    0 18px 88px -4px rgba(0, 0, 0, 0.14);
}

/* Button Medium Shape */
.aiuta-button-m {
  border: none;
  border-radius: 12px;
}

/* Button Small Shape */
.aiuta-button-s {
  border: none;
  border-radius: 8px;
}

/* Image Large Shape */
.aiuta-image-l {
  border-radius: 24px;
}

/* Image Medium Shape */
.aiuta-image-m {
  border-radius: 16px;
}

/* Image Small Shape */
.aiuta-image-s {
  border-radius: 8px;
}
```

### Component-Specific Colors

These colors are already included in the main color scheme above, but are highlighted here for component-specific customization:

```css
:root {
  /* Selection components */
  --aiuta-color-selection-background: #000000;

  /* Error components */
  --aiuta-color-error-background: #ef5754;

  /* Modal overlays */
  --aiuta-color-screen-dim: rgba(0, 0, 0, 0.7);
}
```

## Example Custom CSS

Here's an example of a custom CSS file that overrides the brand color, typeface, and some component styling:

```css
:root {
  /* Override brand color to match your brand */
  --aiuta-color-brand: #ff6b35;
  --aiuta-color-try-on: #ff6b35;

  /* Set custom typeface for all text */
  --aiuta-typeface: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

  /* Customize primary text color */
  --aiuta-color-primary: #1a1a1a;

  /* Customize background colors */
  --aiuta-color-background: #fafafa;
  --aiuta-color-neutral: #f0f0f0;
}

/* Override button styling */
.aiuta-button-m {
  border-radius: 16px;
  font-weight: 600;
}

.aiuta-button-s {
  border-radius: 12px;
  font-weight: 600;
}

/* Customize image shapes */
.aiuta-image-l {
  border-radius: 20px;
}

/* Override typography */
.aiuta-title-l {
  font-weight: 800;
  font-size: 28px;
}
```

## Typography System

The Web SDK uses a unified typography system with both CSS variables and classes:

- **CSS Variable Control**: Change `--aiuta-typeface` to update the font family across all SDK components
- **CSS Class Customization**: Override individual typography classes (`.aiuta-title-l`, `.aiuta-button-m`, etc.) for specific styling
- **Consistent Appearance**: All components use the same base font family by default
- **Flexible Customization**: Mix CSS variables for global changes with class overrides for specific elements
- **Fallback Support**: The default typeface includes Roboto and system fonts for optimal cross-platform compatibility

## Notes

- **CSS Variables**: All CSS variables are optional - only override the ones you need to customize
- **CSS Classes**: You can override any of the typography and shape classes to customize specific components
- **Fallback Behavior**: The SDK will fall back to default values for any variables or classes not defined in your custom CSS
- **Global Font Control**: The `--aiuta-typeface` variable applies to all text elements automatically
- **HTTPS Requirement**: Make sure your custom CSS file is accessible via HTTPS when using the SDK in production
- **Cross-Device Testing**: Test your customizations across different devices and screen sizes to ensure compatibility
- **Import Order**: Your custom CSS should be loaded after the SDK's default styles to ensure proper override behavior

## Roadmap

We're continuously working to expand the Web SDK's styling capabilities:

1. **Extended Styling System**: Expand the CSS variable system to provide greater alignment with the [general configuration scheme](/sdk/developer/configuration/ui/theme/index.md), including support for all theme components and advanced styling options available on other platforms.

2. **Granular Element Customization**: Add the ability to fully customize specific elements on specific SDK pages with complete CSS capabilities, allowing developers to target individual components and pages for maximum design flexibility.
