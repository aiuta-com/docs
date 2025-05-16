# Type Definitions

## `Callback`

Is a function type that can accept parameters and return a value. Additionally, on certain platforms, it might be represented as an interface with a similar method, but the underlying concept and conditions remain consistent.

## `Color`

Platform-specific `Color` type or `#ARGB` `string` representation, e.g. :material-square-rounded:{ .cl-error-background } `"#FFEF5754"`

## `Icon`

A type used for various UI icons throughout the SDK. Icons can be used in two ways:

- As a `template` image - the SDK will automatically color it based on where it's used
- As an `original` image - used without any color changes

!!! note ""
    Depending on the platform, if the standard type supports defining this rendering modes, it will be used. Otherwise, the SDK will supply a type to configure the rendering mode and provide the graphics resource as platform-specific `Image` type or `string` representing path to the icon resource.


## `Image`

Platform-specific `Image` type or `string` representing path to the image resource.

## `Shape`

A type that defines the visual appearance of UI elements, particularly their corner radius.

## `TextStyle`

A type used to define text styling properties for various UI elements.
