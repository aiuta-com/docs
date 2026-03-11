---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  String: /sdk/developer/definitions/#string
---
# Protection Disclaimer

Displays an optional disclaimer message informing users about photo privacy and protection.

## [:material-arrow-up-left:](index.md#image-picker-feature) ImagePickerProtectionDisclaimerFeature

```typescript
ImagePickerProtectionDisclaimerFeature {
  icons {
    protection16: Icon // (1)!
  }

  strings {
    protectionDisclaimer: String // (2)!
  }
}
```

1.  Icon displayed alongside the protection disclaimer text.
2.  Text informing the user that their photos are protected and private.
