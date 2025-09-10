# Limited Configuration Support

The Web SDK currently has limited configuration support compared to the [general configuration scheme](/sdk/developer/configuration/index.md). While the full configuration structure is available on other platforms (Android, iOS, Flutter), the Web SDK implementation focuses on essential features for web integration.

## Configuration Support Status

| Configuration | Support Status | Description |
|---------------------|----------------|-------------|
| [`auth`](/sdk/developer/configuration/auth.md) | ✅ **Full** | Auth support with both API key and JWT methods |
| [`analytics`](/sdk/developer/configuration/analytics.md) | ✅ **Full** | Analytics event handling |
| [`userInterface`](/sdk/developer/configuration/ui/index.md) | ⚠️ **Partial** | Only styling configuration is available wia [custom CSS](/sdk/web/configuration/custom-css.md) |
| [`features`](/sdk/developer/configuration/features/index.md) | ❌ **Not Supported** | Feature toggles and advanced functionality not available |
| [`debugSettings`](/sdk/developer/configuration/debug-settings.md) | ❌ **Not Supported** | Debug logging and validation settings not available |

## What's Available

The Web SDK supports the core functionality needed for virtual try-on experiences:

- **Authentication**: Both API key and JWT-based authentication
- **Analytics**: Complete analytics event tracking and custom handlers
- **Basic UI**: Custom CSS styling and theme configuration
- **Core Features**: Virtual try-on functionality with standard UI components

## What's Not Available

Advanced configuration options that are available on mobile platforms:

- **Feature Toggles**: Individual feature enable/disable controls
- **Debug Settings**: Logging levels and validation policies
- **Advanced UI Configuration**: Detailed component customization beyond CSS

## Future Roadmap

We're continuously working to expand Web SDK configuration support.
