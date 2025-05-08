# Welcome Screen

![Welcome Screen](../../media/pages/welcome-screen.png){width=300}

The Welcome Screen is an optional feature that can be displayed when users first open the SDK. It serves as an introduction to your virtual try-on experience and can be customized to match your brand identity.

## When to Use

- Show the welcome screen on the first launch of the SDK
- Use it to introduce users to your virtual try-on experience
- Set the tone for the user journey

## Customization

#### [Images](../resources/images.md)
- Custom `welcomeBackground` image that fills the entire screen

#### [Icons](../resources/icons.md)
- Custom central `welcome82` icon displayed above the title (82x82 points)

#### [Text Elements](../resources/localization.md)
- Main `welcomeTitle` heading that introduces the feature
- Supporting `welcomeDescription` explaining the virtual try-on experience
- Call-to-action `welcomeButtonStart` to begin the experience

#### [Typography](../resources/typography.md)
- Custom `welcomeTitle` text style for the title
- Custom `welcomeDescription` text style for the description text

#### General styles
- [Icon](../resources/icons.md) and [position](../resources/other.md) of close button
- [Shape](../resources/shapes.md), [colors](../resources/colors.md) and [text style](../resources/typography.md) of start button

## [Analytics](../analytics/analytics.md)

The following analytics events are tracked on the Welcome Screen:

| Type | Event | Page Id | Description |
|------|-------|---------|-------------|
| [`page`](../analytics/analytics.md#event-categories) | :material-minus: | [`welcome`](../analytics/analytics.md#page-identifiers) | Triggered when the welcome screen is displayed |
| [`onboarding`](../analytics/analytics.md#event-categories) | [`welcomeStartClicked`](../analytics/analytics.md#onboarding-events) | [`welcome`](../analytics/analytics.md#page-identifiers) | Triggered when user clicks the start button<br>to begin the try-on process |
| [`exit`](../analytics/analytics.md#event-categories) | :material-minus: | [`welcome`](../analytics/analytics.md#page-identifiers) | SDK was closed on the welcome screen |
