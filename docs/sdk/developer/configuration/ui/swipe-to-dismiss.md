---
hide:
  - toc
---
# Swipe To Dismiss

Specifies the policy for dismissing the SDK's user interface through a swipe gesture. It determines how and when the swipe-to-dismiss action can be performed by the user.

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/index.md#user-interface) SwipeToDismissPolicy

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
