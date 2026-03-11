---
template: scheme.html
hide:
  - toc
code_links:
  Icon: /sdk/developer/definitions/#icon
  String: /sdk/developer/definitions/#string
---
# [:material-arrow-up-left:](index.md#image-picker) Protection Disclaimer

Displays an optional disclaimer message informing users about photo privacy and protection.

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
