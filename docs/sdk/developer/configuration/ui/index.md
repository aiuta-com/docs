---
hide:
  - toc
---
# User Interface Scheme

The User Interface Scheme defines the configuration options for the presentation style, swipe-to-dismiss policy, and theme settings of the SDK's UI components.

## [:material-arrow-up-left:](/sdk/developer/configuration/index.md#configuration) User Interface

```typescript
UserInterface {
  presentationStyle: PresentationStyle
  swipeToDismiss: SwipeToDismissPolicy
  theme: Theme // (1)!
}
```

1.  [:material-arrow-down-left:](/sdk/developer/configuration/ui/theme/index.md) Specifies the theme configuration settings that determine the appearance and style of the UI components within the SDK. This includes defining color schemes, typography, and other visual elements to ensure a cohesive and customizable user interface experience.


## PresentationStyle

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

## SwipeToDismissPolicy

```typescript
enum SwipeToDismissPolicy {
  allowAlways // (1)!
  allowHeaderSwipeOnly // (2)!
  protectTheNecessaryPages // (3)!
}
```

1.  Allows the SDK to be dismissed at any time by swiping down anywhere on the screen.
    
    !!! tip ""
        This policy provides the most flexibility for users, enabling them to close the SDK from any page or context.    

2.  Restricts dismissal to swiping down on the header area only.
    
    !!! tip ""
        This policy limits the swipe-to-dismiss gesture to the header area, reducing the likelihood of accidental dismissals.

3.  Applies different swipe-to-dismiss policies based on the page context.
    
    !!! tip ""
        
        - On pages that are safe to close, such as onboarding or photo picker pages, the `allowAlways` policy is applied, allowing dismissal from anywhere on the screen.
        - On critical pages, such as those waiting for generation or displaying results, the `allowHeaderSwipeOnly` policy is applied to prevent accidental dismissals.
    
    This policy provides a balance between user convenience and protecting critical workflows, ensuring that users can dismiss the SDK when appropriate while safeguarding important pages.    

!!! note "iOS only"
        
    This property specifies the policy for dismissing the SDK's user interface through a swipe gesture. It determines how and when the swipe-to-dismiss action can be performed by the user. The policy can vary, allowing for different levels of interaction, such as always allowing a swipe to dismiss, restricting it to certain conditions, or permitting it only when swiping from specific areas of the interface.

