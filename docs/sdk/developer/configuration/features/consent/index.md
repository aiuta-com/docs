---
template: scheme.html
hide:
  - toc
code_links:
  Callback: /sdk/developer/definitions/#callback
  Consent: /sdk/developer/configuration/features/consent/data/#consent
  Icon: /sdk/developer/definitions/#icon
  List: /sdk/developer/definitions/#list
  Observable: /sdk/developer/definitions/#observable
  Bool: /sdk/developer/definitions/#bool
  String: /sdk/developer/definitions/#string
---
# Consent Scheme

Manages user [:material-window-open: consent](/sdk/about/pages/consent.md) options for data processing, which can be integrated with onboarding or used independently.

![Consent](/media/pages/consent-explicit.png){ width=220 }
![Consent](/media/pages/consent-implicit-wo-check.png){ width=220 }

## [:material-arrow-up-left:](/sdk/developer/configuration/features/index.md#features) Consent Feature

=== "Standalone Onboarding Page"
    ```typescript
    ConsentStandaloneOnboardingPageFeature {
      strings {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      }

      icons {
        consentTitle24: Icon // (6)!
      }

      styles {
        drawBordersAroundConsents: Bool // (7)!
      }

      data {
        consents: List<Consent> // (8)!
      }

      dataProvider: BuiltIn | Custom {
        obtainedConsentIds: Observable<List<String>> // (9)!
        obtainConsentIds: Callback(List<String>) // (10)!
      }
    }
    ```

    1. Optional title for the standalone consent page at the top of the screen.
    2. Main title displayed on the standalone consent page.
    3. HTML content describing the consent terms and conditions.
    4. Optional HTML footer content for additional information.
    5. Text label for the button that accepts the consent terms.
    6. Icon displayed next to the consent title in the standalone page.
    7. Controls whether to display borders around consent sections.
    8. List of consent options that users must and may accept.
    9. Observable property tracking which consent options have been already accepted.
    10. Callback function triggered when user accepts consents.

        !!! info ""
            You should save the consent IDs that are passed and  provide them in the `obtainedConsentsIds` property for future use. If not stored, the SDK will show the consent screen again during the next Try-On session.

=== "Standalone Image Picker Page"
    ```typescript
    ConsentStandaloneImagePickerPageFeature {
      strings {
        consentPageTitle: String | null // (1)!
        consentTitle: String // (2)!
        consentDescriptionHtml: String // (3)!
        consentFooterHtml: String | null // (4)!
        consentButtonAccept: String // (5)!
      }

      icons {
        consentTitle24: Icon // (6)!
      }

      styles {
        drawBordersAroundConsents: Bool // (7)!
      }

      data {
        consents: List<Consent> // (8)!
      }

      dataProvider: BuiltIn | Custom {
        obtainedConsentIds: Observable<List<String>> // (9)!
        obtainConsentIds: Callback(List<String>) // (10)!
      }
    }
    ```

    1. Optional title for the standalone consent page at the top of the screen.
    2. Main title displayed on the standalone consent page.
    3. HTML content describing the consent terms and conditions.
    4. Optional HTML footer content for additional information.
    5. Text label for the button that accepts the consent terms.
    6. Icon displayed next to the consent title in the standalone page.
    7. Controls whether to display borders around consent sections.
    8. List of consent options that users must and may accept.
    9. Observable property tracking which consent options have been already accepted.
    10. Callback function triggered when user accepts consents.

        !!! info ""
            You should save the consent IDs that are passed and  provide them in the `obtainedConsentsIds` property for future use. If not stored, the SDK will show the consent screen again during the next Try-On session.

=== "Embedded Into Onboarding"
    ```typescript
    ConsentEmbeddedIntoOnboardingFeature {
      strings {
        consentHtml: String // (1)!
      }
    }
    ```

    1. HTML content displayed at the bottom of the onboarding screen for embedded consent.
