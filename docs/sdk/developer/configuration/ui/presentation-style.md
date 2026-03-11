---
hide:
  - toc
---
# Presentation Style

Specifies the manner in which the SDK's UI overlays the application's existing UI, such as whether the SDK UI appears as a full-screen overlay, or covers the application with a bottom sheet.

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/index.md#user-interface) PresentationStyle

```typescript
enum PresentationStyle {
  fullScreen // (1)!
  bottomSheet // (2)!
  pageSheet // (3)!
}
```

1.  Presents the SDK in full-screen mode. This style occupies the entire screen, hiding the parent view completely.

2.  Opens the SDK in a bottom sheet.

    !!! note "Partial iOS support"
        This mode is supported on iOS from version `16` onwards. For older versions, it defaults to `pageSheet`. Unlike `pageSheet`, the parent view remains fullscreen but is covered by the sheet, rather than being stacked behind it.

3.  The SDK appears in a page sheet, which partially covers the parent view, allowing users to see some of the underlying content while interacting with the SDK. Unlike a `bottomSheet`, which keeps parent view fullscreen, a page sheet stacking the parent view behind, slightly shrinking and moving it away from the screen edges.

    !!! tip ""
        - This mode is recommended starting from __iOS__ 13. For more information, refer to [Best practices from Apple's HIG :octicons-link-external-24:](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices){:target="_blank"}.
        - On __Android__, this mode behaves as a `bottomSheet`.

!!! note "iOS and Flutter only"

    Specifies the manner in which the SDK's UI overlays the application's existing UI. This setting determines the visual presentation style, such as whether the SDK UI appears as a full-screen overlay, or covers the application with a bottom sheet.
