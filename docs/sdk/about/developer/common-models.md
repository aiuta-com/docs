# Common Models Schemes

## Product

The product scheme defines the structure and properties of products within the Aiuta platform. This scheme is essential for displaying product information in the SDK's user interface and managing product-related functionality.

```typescript
Product {
  id: String // (1)!
  title: String // (2)!
  brand: String // (3)!
  imageUrls: List<String> // (4)!
  price: Price | null // (5)!
}
```

1.  Unique identifier for the product, used to distinguish it across the platform. Must match the identifiers provided to Aiuta for training try-on models.
2.  The name or title of the product, displayed prominently in the user interface.
3.  The brand associated with the product, identifying the manufacturer or provider.
4.  Collection of URLs pointing to product images. Should contain at least one URL. Flatlay image must be first if `ProductBarTheme` has enabled `applyProductFirstImageExtraPadding`.
5.  Optional pricing details for the product, including current and old prices.

### Price

```typescript
Price {
  current: String // (1)!
  old: String | null // (2)!
}
```

1.  Current price of the product, formatted as a localized string including currency symbol and amount.
2.  Optional old price of the product, formatted as a localized string. If provided, will be displayed as strikethrough near the current price.


## Consent

The Consent type defines how user consent is managed within the SDK, specifying the interaction required from the user and the conditions under which consent is considered given.

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

## History Images

The History Images represent a user's interaction history in the Aiuta SDK, including boths user-uploaded and Aiuta-provided images.

### Input Image

```typescript
InputImage {
    id: String // (1)!
    url: String // (2)!
    ownerType: OwnerType // (3)!
}
```

1.  A unique string identifier assigned to the image by the Aiuta API, ensuring each image can be distinctly recognized and referenced within the system.
2.  The URL pointing to the location of the image resource, which can be accessed and retrieved by the SDK to present in the UI.
3.  The type of the image [owner :octicons-arrow-down-24:](#owner-type).
    
    !!! warning ""
        Please refer to this section in case of using custom [`dataProvider` for the uploads history](configuration.md#uploads-history)

Input images used in the Aiuta SDK for try-on sessions can either be uploaded by users, such as photos taken with their camera or selected from their gallery, or they can be predefined model images provided by Aiuta.

### Generated Image

```typescript
GeneratedImage {
    id: String // (1)!
    url: String // (2)!
    ownerType: OwnerType // (3)!
    productIds: List<String> // (4)!
}
```

1.  A unique string identifier assigned to the image by the Aiuta API, ensuring each image can be distinctly recognized and referenced within the system.
2.  The URL pointing to the location of the image resource, which can be accessed and retrieved by the SDK to present in the UI.
3.  The type of the image [owner :octicons-arrow-down-24:](#owner-type).
    
    !!! warning ""
        Please refer to this section in case of using custom [`dataProvider` for the generations history](configuration.md#generations-history)

4.  A list of product identifiers that were utilized during the image generation process. Each identifier corresponds to a specific product involved in the try-on session, allowing for precise tracking and reference within the system.

Generated images represent the results of try-on sessions. These images are generated based on either a photo uploaded by the user or a predefined model image provided by Aiuta.

### Owner Type

```typescript
enum OwnerType {
    user // (1)!
    aiuta // (2)!
}
```

1.  Image uploaded or generated by the user (using a camera or from a gallery).
    
    !!! note ""
        This image belongs to the user. When the user removes the image from the history, it __may be deleted__ from the storage as well.

2.  Image of the model provided or generated by the Aiuta. 

    !!! note ""
        This image could be linked to the user history, but it is not owned by the user, and __can not be deleted__ from the storage, only unlinked from the user's history in case of removing.


Owner type primarily determines the source of origin of the image — whether it was generated by the user as a result of any chain of operations from upload to generation, possibly including re-generation. Alternatively, the image is not associated with the user's personal data and does not belong to them. This allows different approaches to be taken when deleting images from the history.

!!! warning "Do not delete `aiuta` owned image files"
    Well, you can make a request to delete such an image, nothing terrible will happen, but be prepared that Aiuta API will return an error when you try.

    But ideally, you should only link/unlink those images in the user's history.
