# Type Definitions

## `Callback`

Is a function type that can accept parameters and return a value. Additionally, on certain platforms, it might be represented as an interface with a similar method, but the underlying concept and conditions remain consistent.

## `Observable`

An `Observable` is a type that can be watched by the SDK for changes. The specific implementation of an `Observable` may vary depending on the platform: it might be represented as `Flow`, `ValueListenable`, `Stream`, or the SDK will supply a custom implementation to facilitate change observation.

## `List`

A `List` is a collection type that holds an ordered sequence of elements. It can be represented as an `Array`, `List`, or other similar constructs.

## `Map`

A `Map` is a collection type that associates keys with values. It is used to store data in key-value pairs, where each key is unique. The specific implementation may vary depending on the platform, such as `Map`, `Dictionary`, or other similar constructs. 

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

A type that specifies the visual appearance of UI elements, which may be as simple as a decimal number representing a corner radius. Depending on the platform and SDK implementation, it can also offer more configurations like corner curve types.

## `TextStyle`

A type used to define text styling properties for various UI elements.
