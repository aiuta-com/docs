# Consent

The Consent type defines how user consent is managed within the SDK, specifying the interaction required from the user and the conditions under which consent is considered given.

```typescript
Consent {
  id: string,// (1)!
  type: ConsentType,// (2)!
  html: string,// (3)!
}

```

1. Unique identifier for the consent option.
2. Type of consent determining how it should be presented and handled.
3. HTML content containing the consent terms and conditions.

## Type

```typescript
enum ConsentType {
  implicitWithoutCheckbox,// (1)!
  implicitWithCheckbox,// (2)!
  explicitRequired,// (3)!
  explicitOptional,// (4)!
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
    Be careful when using implicit consent types. Ensure to review annotations :material-information-symbol: for clarity and compliance.
