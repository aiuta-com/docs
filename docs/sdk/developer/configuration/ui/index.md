---
template: scheme.html
hide:
  - toc
code_links:
  Theme: theme/
  PresentationStyle: presentation-style/
  SwipeToDismissPolicy: swipe-to-dismiss/
---
# User Interface Scheme

The User Interface Scheme defines the configuration options for the presentation style, swipe-to-dismiss policy, and theme settings of the SDK's UI components.

## [:material-arrow-up-left:](/sdk/developer/configuration/index.md#configuration) User Interface

```typescript
UserInterface {
  presentationStyle: PresentationStyle // (1)!
  swipeToDismiss: SwipeToDismissPolicy // (2)!
  theme: Theme // (3)!
}
```

1.  [:material-arrow-down-left:](presentation-style.md) Specifies the manner in which the SDK's UI overlays the application's existing UI, such as whether the SDK UI appears as a full-screen overlay, or covers the application with a bottom sheet.

2.  [:material-arrow-down-left:](swipe-to-dismiss.md) Specifies the policy for dismissing the SDK's user interface through a swipe gesture.

3.  [:material-arrow-down-left:](/sdk/developer/configuration/ui/theme/index.md) Specifies the theme configuration settings that determine the appearance and style of the UI components within the SDK. This includes defining color schemes, typography, and other visual elements to ensure a cohesive and customizable user interface experience.

