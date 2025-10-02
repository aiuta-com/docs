# Limited Configuration Support

The Web SDK currently has limited configuration support compared to the [general configuration scheme](/sdk/developer/configuration/index.md). While the full configuration structure is available on other platforms (Android, iOS, Flutter), the Web SDK implementation focuses on essential features for web integration.

## Configuration Support Status

| Configuration                                                     | Support Status | Description                                                   |
| ----------------------------------------------------------------- | -------------- | ------------------------------------------------------------- |
| [`auth`](/sdk/developer/configuration/auth.md)                    | ✅ **Full**    | Complete auth support with both API key and JWT methods       |
| [`analytics`](/sdk/developer/configuration/analytics.md)          | ✅ **Full**    | Analytics event handling with custom callbacks                |
| [`userInterface`](/sdk/developer/configuration/ui/index.md)       | ⚠️ **Partial** | Custom CSS styling + localization strings for UI components   |
| [`features`](/sdk/developer/configuration/features/index.md)      | ⚠️ **Partial** | Localization strings and image customization for key features |
| [`debugSettings`](/sdk/developer/configuration/debug-settings.md) | ⚠️ **Basic**   | Simple logging enable/disable setting                         |

## What's Available

The Web SDK supports comprehensive functionality for virtual try-on experiences:

### ✅ **Full Support**

- **Authentication**: Both API key and JWT-based authentication with callback support
- **Analytics**: Complete analytics event tracking with custom event handlers

### ⚠️ **Partial Support**

- **User Interface**:
  - Custom CSS styling and theme configuration
  - Localization strings for UI components (SelectionSnackbar, ErrorSnackbar, PoweredBy)
- **Features**:
  - Localization strings for key features (Onboarding, ImagePicker, TryOn, Share, Consent)
  - Image customization for onboarding screens
  - Consent management with multiple consent types
- **Debug Settings**: Basic logging enable/disable functionality

### Features Configuration

- ✅ **Onboarding**: Complete localization and image customization
- ✅ **Image Picker**: Localization for upload flows and QR functionality
- ✅ **Try-On**: Localization for try-on process and validation messages
- ✅ **Share**: Localization for sharing functionality
- ✅ **Consent**: Multi-consent management with required/optional types
- ❌ **Feature Toggles**: Individual feature enable/disable not supported
- ❌ **Advanced Workflows**: Custom try-on flows not configurable

## Future Roadmap

We're continuously working to expand Web SDK configuration support to match the full feature set available on mobile platforms.
