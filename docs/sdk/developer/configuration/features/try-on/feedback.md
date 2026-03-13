---
template: scheme.html
hide:
  - toc
code_links:
  TryOnFeedbackOtherFeature: "#other-feedback"
  Icon: /sdk/developer/definitions/#icon
  List: /sdk/developer/definitions/#list
  String: /sdk/developer/definitions/#string
  "null": /sdk/developer/definitions/#optional
---
# [:material-arrow-up-left:](index.md#try-on) Feedback

![Feedback](/media/pages/results-feedback.png){ width=220 }

Optional configuration for collecting user feedback on TryOn results.
```typescript
TryOnFeedbackFeature {
  otherFeedback: TryOnFeedbackOtherFeature | null // (1)!

  icons {
    like36: Icon // (2)!
    dislike36: Icon // (3)!
    gratitude40: Icon // (4)!
  }

  strings {
    feedbackOptions: List<String> // (5)!
    feedbackTitle: String // (6)!
    feedbackButtonSkip: String // (7)!
    feedbackButtonSend: String // (8)!
    feedbackGratitudeText: String // (9)!
  }
}
```

1.  [:material-arrow-down-left:](#other-feedback) Optional configuration for allowing users to provide custom feedback on try-on results.
2.  Icon displayed for the "Like" feedback option.
3.  Icon displayed for the "Dislike" feedback option.
4.  Icon shown after feedback is submitted to express gratitude.
5.  List of available feedback options presented to users.
6.  Title text displayed in the feedback section.
7.  Label text for the button that allows users to skip providing feedback.
8.  Label text for the button that submits the user's feedback.
9.  Message displayed to users after they submit their feedback.

### [:material-arrow-up-left:](#tryonfeedbackfeature) Other Feedback
```typescript
TryOnFeedbackOtherFeature {
  strings {
    otherFeedbackTitle: String // (1)!
    otherFeedbackButtonSend: String // (2)!
    otherFeedbackButtonCancel: String // (3)!
    otherFeedbackOptionOther: String // (4)!
  }
}
```

1.  Title text displayed in the custom feedback section.
2.  Label text for the button that submits the custom feedback.
3.  Label text for the button that cancels the custom feedback.
4.  Text label for the option to provide custom feedback.
