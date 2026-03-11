# Type Definitions

Implementation and naming details may vary depending on the specific platform, but the core concepts and overall structure remain consistent across all platforms.


## Custom Types

### `Color`

A platform-specific color type or `#ARGB` `string` representation, e.g. :material-square-rounded:{ .cl-error-background } `"#FFEF5754"`

=== "Android"

    `String` in hex format (`#AARRGGBB` or `#RRGGBB`), converted internally to `androidx.compose.ui.graphics.Color`.

=== "iOS"

    `Aiuta.Color` — custom wrapper around `UIColor`. Supports hex string literals (`#AARRGGBB`, `#RRGGBB`) and integer literals.

=== "Flutter"

    `String` in hex format (`#AARRGGBB` or `#RRGGBB`), e.g. `"#FF4000FF"`.

=== "Web"

    `string` in hex format (`#RRGGBB` or `#AARRGGBB`) or CSS color values.

### `Icon`

Type used for various UI icons throughout the SDK. Icons can be used in two ways:

- As a `template` image — the SDK will automatically color it based on where it's used
- As an `original` image — used without any color changes

=== "Android"

    `AiutaIcon` — data class with `path: String` and `renderMode: AiutaRenderMode`.

=== "iOS"

    `Aiuta.Icon` — enum with cases `.url(URL, renderingMode:)` and `.image(UIImage)`.

=== "Flutter"

    `AiutaIcon` — class with `path: String` and `renderMode: AiutaRenderMode`.

=== "Web"

    `string` — SVG path, external URL, or inline SVG content.

### `Image`

A platform-specific type or `string` representing path to the image resource.

=== "Android"

    URL string or asset path.

=== "iOS"

    `Aiuta.Image` — enum with cases `.url(URL)` and `.image(UIImage)`.

=== "Flutter"

    URL string or Flutter asset path.

=== "Web"

    `string` — image URL.

### `Observable`

A type that can be watched by the SDK for changes.

=== "Android"

    `Flow<T>` or `StateFlow<T>` — Kotlin coroutine Flows.

=== "iOS"

    `Aiuta.Observable<T>` — custom wrapper class provided by the SDK.

=== "Flutter"

    `Stream<T>` or event callbacks — native Dart streams.

=== "Web"

    Callback-based event handling via RPC methods.

### `Shape`

A type that specifies the visual appearance of UI elements, such as corner radius. Depending on the platform and SDK implementation, it can also offer more configurations like corner curve types.

=== "Android"

    `Double` — corner radius value in pixels.

=== "iOS"

    `Aiuta.Shape` — enum with cases `.continuous(radius:)`, `.circular(radius:)`, `.capsule`, and `.rectangular`.

=== "Flutter"

    `double` — corner radius value.

=== "Web"

    `number` — border radius in pixels.

### `TextStyle`

A type used to define text styling properties for various UI elements.

=== "Android"

    `AiutaTextStyle` — data class with properties: `fontFamily`, `fontSize`, `fontWeight`, `letterSpacing`, `lineHeight`.

=== "iOS"

    `Aiuta.TextStyle` — struct with properties: `font: UIFont`, `size: CGFloat`, `weight: UIFont.Weight`, `kern: CGFloat?`, `lineHeightMultiple: CGFloat?`.

=== "Flutter"

    `AiutaTextStyle` — class with properties: `fontFamily`, `fontSize`, `fontWeight`, `letterSpacing`, `lineHeight`.

=== "Web"

    CSS styles via theme configuration or inline `style` properties.


## Basic Types

### `Bool`

A boolean value (`true` or `false`).

=== "Android"

    `Boolean` — native Kotlin type.

=== "iOS"

    `Bool` — native Swift type.

=== "Flutter"

    `bool` — native Dart type.

=== "Web"

    `boolean` — native TypeScript type.

### `Callback`

A function type that can accept parameters and return a value.

=== "Android"

    Function type such as `(T) -> Unit` or a SAM interface with a similar method.

=== "iOS"

    Closure type such as `(T) -> Void`.

=== "Flutter"

    Function type such as `void Function(T)` or `VoidCallback`.

=== "Web"

    Function type such as `(params: Record<string, any>) => void`.

### `List`

A collection type that holds an ordered sequence of elements.

=== "Android"

    `List<T>` — Kotlin List interface.

=== "iOS"

    `[T]` — native Swift Array type.

=== "Flutter"

    `List<T>` — native Dart List type.

=== "Web"

    `T[]` or `Array<T>` — native TypeScript array.

### `Map`

A collection type that associates keys with values, where each key is unique.

=== "Android"

    `Map<String, T>` — Kotlin Map interface.

=== "iOS"

    `[String: T]` — native Swift Dictionary type.

=== "Flutter"

    `Map<String, dynamic>` — native Dart Map type.

=== "Web"

    `Record<string, T>` — TypeScript record type.

### `Number`

A numeric value (integer or floating-point).

=== "Android"

    `Double` — Kotlin Double type.

=== "iOS"

    `CGFloat` — CoreGraphics floating-point type.

=== "Flutter"

    `double` — native Dart type.

=== "Web"

    `number` — native TypeScript type.

### `String`

A text value.

=== "Android"

    `String` — native Kotlin type.

=== "iOS"

    `String` — native Swift type.

=== "Flutter"

    `String` — native Dart type.

=== "Web"

    `string` — native TypeScript type.

---

!!! info "Naming Convention"
    Implementation and naming details may vary depending on the specific platform, but the core concepts and overall structure remain consistent across all platforms.
    For example type names, described in the schemes, like:

    - `Configuration`

        - in Swift it will be `Aiuta.Configuration`
        - in Kotlin and Dart - `AiutaConfiguration`

    - `UserInterface`

        - in Swift it will be `Aiuta.Configuration.UserInterface`
        - in Kotlin and Dart - `AiutaUserInterfaceConfiguration`

    - `Product`

        - in Swift it will be `Aiuta.Product`
        - in Kotlin and Dart - `AiutaProduct`

    and so on - the key part of the name is the same.
