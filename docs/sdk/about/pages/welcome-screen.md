# Welcome Screen

![Welcome Screen](/media/pages/welcome.png){width=300}

The Welcome Screen is an optional feature that can be displayed when users first open the SDK. It serves as an introduction to your virtual try-on experience and can be customized to match your brand identity.

## When to Use

- Show the welcome screen on the first launch of the SDK
- Use it to introduce users to the virtual try-on experience
- Set the tone for the user journey

!!! info "Behavior"
    The Welcome Screen is displayed only if the user has not completed the [Onboarding](/sdk/about/pages/onboarding.md).
    Thus, it is bound to the Onboarding feature. If the Onboarding is not provided,
    the Welcome Screen will be displayed every time the SDK is opened and you
    should care of enabling or disabling the Welcome Screen feature in
    the configuration to control the Welcome Screen visibility yourself.

---

??? tip "Customization"

    ## Customization

    ##### [Images](/sdk/about/resources/images.md)
    - Custom `welcomeBackground` image that fills the entire screen

    !!! note ""
        Make sure image itself is dimmed to be contrast enough with `onDark` color

    ##### [Icons](/sdk/about/resources/icons.md)
    - Custom central `welcome82` icon displayed above the title (82x82 points)
    - General `close24` icon for close button

    ##### [Text Elements](/sdk/about/resources/localization.md)
    - Main `welcomeTitle` heading that introduces the feature
    - Supporting `welcomeDescription` explaining the virtual try-on experience
    - Call-to-action `welcomeButtonStart` to begin the experience

    ##### [Typography](/sdk/about/resources/typography.md)
    - Custom `welcomeTitle` text style for the title
    - Custom `welcomeDescription` text style for the description text
    - General `buttonM` text style for the start button

    ##### [Shapes](/sdk/about/resources/shapes.md)
    - General `buttonM` shape of start button

    ##### [Colors](/sdk/about/resources/colors.md)
    - General `onDark` color for close button, title, description and start button background
    - General `onLight` color for start button label

---

## [Analytics](/sdk/about/analytics/analytics.md)

The following analytics events are tracked on the Welcome Screen:

| Type | Event | Page Id | Description |
|------|-------|---------|-------------|
| [`page`](/sdk/about/analytics/analytics.md#event-types) | :material-minus: | [`welcome`](/sdk/about/analytics/analytics.md#page) | Triggered when the welcome screen is displayed |
| [`onboarding`](/sdk/about/analytics/analytics.md#event-types) | [`welcomeStartClicked`](/sdk/about/analytics/analytics.md#onboarding) | [`welcome`](/sdk/about/analytics/analytics.md#page) | Triggered when user clicks the start button<br>to start the journey |
| [`exit`](/sdk/about/analytics/analytics.md#event-types) | :material-minus: | [`welcome`](/sdk/about/analytics/analytics.md#page) | SDK was closed on the welcome screen |

---

## How to implement

<div class="grid cards" markdown>

- :fontawesome-brands-android: __Android__
- :fontawesome-brands-apple: __iOS__
- :fontawesome-brands-flutter: __Flutter__

</div>
