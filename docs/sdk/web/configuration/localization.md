# Localization Configuration

The Web SDK supports comprehensive localization for UI components and features. You can customize text strings and images to match your brand and language requirements.

## Configuration Structure

Localization is configured through two main sections:

- **`userInterface`** - Basic UI component strings
- **`features`** - Feature-specific strings and images

```javascript
const aiuta = new Aiuta({
  auth: {
    subscriptionId: 'your_subscription_id',
    getJwt: async (params) => 'your_jwt_token',
  },
  userInterface: {
    theme: {
      selectionSnackbar: {
        strings: {
          select: 'Select',
          cancel: 'Cancel',
          selectAll: 'Select All',
          unselectAll: 'Unselect All',
        },
      },
      errorSnackbar: {
        strings: {
          defaultErrorMessage: 'Something went wrong.\nPlease try again later',
          tryAgainButton: 'Try Again',
        },
      },
      poweredBy: {
        strings: {
          poweredByAiuta: 'Powered by Aiuta',
        },
      },
    },
  },
  features: {
    onboarding: {
      strings: {
        onboardingButtonNext: 'Next',
        onboardingButtonStart: 'Start',
      },
      howItWorksPage: {
        strings: {
          onboardingHowItWorksTitle: 'Try on before buying',
          onboardingHowItWorksDescription: 'Upload a photo and see how items look on you',
        },
        images: {
          onboardingHowItWorksItems: [
            {
              itemPhoto: 'https://example.com/item1-photo.jpg',
              itemPreview: 'https://example.com/item1-preview.png',
            },
            {
              itemPhoto: 'https://example.com/item2-photo.jpg',
              itemPreview: 'https://example.com/item2-preview.png',
            },
            {
              itemPhoto: 'https://example.com/item3-photo.jpg',
              itemPreview: 'https://example.com/item3-preview.png',
            },
          ],
          onboardingHowItWorksDesktop: 'https://example.com/how-it-works-desktop.png',
        },
      },
      bestResultsPage: {
        strings: {
          onboardingBestResultsTitle: 'For the best results',
          onboardingBestResultsDescription:
            'Use a photo with good lighting, stand straight on a plain background',
        },
        images: {
          onboardingBestResultsDesktop: 'https://example.com/best-results-desktop.png',
          onboardingBestResultsMobile: 'https://example.com/best-results-mobile.png',
        },
      },
    },
    imagePicker: {
      strings: {
        imagePickerUploadButton: 'Upload a photo of you',
        uploadsHistoryButtonNewPhoto: '+ Upload new photo',
      },
      uploadsHistory: {
        strings: {
          uploadsHistoryTitle: 'Previously used photos',
          uploadsHistoryButtonChangePhoto: 'Change photo',
        },
      },
      qrUpload: {
        strings: {
          qrUploadNextButton: 'Next',
          qrUploadSuccessTitle: 'Your photo has been uploaded',
          qrUploadNextHint: 'It will appear within a few seconds',
        },
      },
      qrPrompt: {
        strings: {
          qrPromptHint: 'Scan the QR code',
          qrPromptOr: 'Or',
          qrPromptUploadButton: 'Click here to upload',
        },
      },
    },
    tryOn: {
      strings: {
        tryOnPageTitle: 'Virtual Try On',
        tryOn: 'Try On',
      },
      loadingPage: {
        strings: {
          tryOnLoadingStatusScanningBody: 'Scanning your body',
          tryOnLoadingStatusGeneratingOutfit: 'Generating outfit',
        },
      },
      inputImageValidation: {
        strings: {
          invalidInputImageDescription: "We couldn't detect anyone in this photo",
          invalidInputImageChangePhotoButton: 'Change photo',
          noPeopleDetectedDescription: "We couldn't detect anyone in this photo. For best results, please upload a well-lit photo of an adult standing straight in front of a pale background.",
          tooManyPeopleDetectedDescription: "We detected multiple people in this photo. For best results, please upload a well-lit photo of an adult standing straight in front of a pale background.",
          childDetectedDescription: "It looks like this photo might be of a child. For best results, please upload a well-lit photo of an adult standing straight in front of a pale background."
        },
      },
      fitDisclaimer: {
        strings: {
          fitDisclaimerTitle: 'Results may vary from real-life fit',
        },
      },
      generationsHistory: {
        strings: {
          generationsHistoryPageTitle: 'History',
        },
      },
    },
    share: {
      strings: {
        shareButton: 'Share',
        sharePageTitle: 'Share with',
        copyButton: 'Copy',
        downloadButton: 'Download',
      },
    },
    consent: {
      strings: {
        consentTitle: 'Consent',
        consentDescriptionHtml:
          'In order to try on items digitally, you agree to allow Aiuta to process your photo. Your data will be processed according to the Aiuta <a href="https://aiuta.com/legal/terms-of-service.html" target="_blank" rel="noopener noreferrer">Terms of Use</a>',
        consentButtonAccept: 'Accept',
      },
      data: {
        consents: [
          {
            id: 'main',
            type: 'explicitRequired',
            html: 'I agree to allow Aiuta to process my photo',
          },
          {
            id: 'age-verification',
            type: 'explicitRequired',
            html: 'I confirm that I am 18 years of age or older',
          },
        ],
      },
    },
  },
})
```

## Key Features

- **User Interface Components**: Localize basic UI elements like selection controls, error messages, and attribution
- **Onboarding Flow**: Customize text and images for the introduction screens
- **Image Picker**: Localize photo upload and management interfaces
- **Try-On Process**: Customize text for the virtual try-on experience
- **Share Functionality**: Localize sharing options and actions
- **Consent Management**: Support multiple consent types with HTML content

## Notes

- **All strings are optional** - The SDK provides English defaults for all text
- **Multi-line text** - Use `\n` for line breaks in strings like error messages
- **HTML content** - Consent descriptions support HTML tags for links and formatting
- **Image requirements** - Custom images must be HTTPS URLs accessible from `static.aiuta.com`
- **Fallback behavior** - Missing strings or images automatically fall back to SDK defaults
