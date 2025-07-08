# Consent Scheme

Manages user consent options for data processing, which can be integrated with onboarding or used independently.

## [:material-arrow-up-left:](/sdk/developer/configuration/features/#features) Consent Feature

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
        obtainedConsentIds: Observable<List<string>> // (9)!
        obtainConsentIds: Callback(List<string>) // (10)!
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

        !!! info ""
            See [consent :octicons-arrow-right-24:](consent.md) scheme for more deatils

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
        obtainedConsentIds: Observable<List<string>> // (9)!
        obtainConsentIds: Callback(List<string>) // (10)!
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

        !!! info ""
            See [consent :octicons-arrow-right-24:](consent.md) scheme for more deatils

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

## Data


The Consent type defines how user consent is managed within the SDK, specifying the interaction required from the user and the conditions under which consent is considered given.

### Consent

```typescript
Consent {
  id: String // (1)!
  type: ConsentType // (2)!
  html: String // (3)!
}

```

1. Unique identifier for the consent option.
2. Type of consent determining how it should be presented and handled.
3. HTML content containing the consent terms and conditions.

### Type

```typescript
enum ConsentType {
  implicitWithoutCheckbox // (1)!
  implicitWithCheckbox // (2)!
  explicitRequired // (3)!
  explicitOptional // (4)!
}
```

1. Consent has no checkbox and it is assumed to be given by pressing the accept button. 

    !!! info "GDPR Compliance"
        It can be just an accept button, but only if it's very clear exactly what the user is consenting to at that moment. You can't bundle multiple consents into one accept unless they're strictly necessary. For example, GDPR says marketing consent should always be separate if possible.
        
        !!! danger "" 
            Please consider that this option is not valid for all cases, and it should be used with caution. 
            
            Consult with a legal department if in doubt.

2. Consent has disabled pre-ticked checkbox and it is assumed to be given by pressing the accept button. 

    !!! warning "GDPR Compliance"
        This can be used only for the consent that is necessary for the service, as it's not really "consent" under GDPR — it's processing based on contract necessity (Article 6(1)(b)) or legal obligation, not based on "freely given consent" (Article 6(1)(a)). So, it is just informing the user, not asking them for an additional permission.
        
        !!! danger "" 
            Please consider that this option is not valid for all cases, and it should be used with caution. 
            
            Consult with a legal department if in doubt.

3. Consent has a checkbox and the user must check it in order to continue.
4. Consent has a checkbox and the user may proceed without checking it.

Defines the methods for obtaining consent to process user photos.

!!! warning "GDPR Compliance"
    Be careful when using implicit consent types. 
    
    Ensure to review annotations :material-information-outline: for clarity and compliance.
