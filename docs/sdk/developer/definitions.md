# Type Definitions

Implementation and naming details may vary depending on the specific platform, but the core concepts and overall structure remain consistent across all platforms.


## Custom Types

### `Color`

A platform-specific color type or `#ARGB` `string` representation, e.g. :material-square-rounded:{ .cl-error-background } `"#FFEF5754"`

=== "Android"

    ```kotlin
    // Compose Color from hex value
    val brand: Color = Color(0xFF4000FF)
    ```

=== "iOS"

    ```swift
    // Custom wrapper around UIColor
    // Supports hex string literals and integer literals
    let brand: Aiuta.Color = "#FF4000FF"
    ```

=== "Flutter"

    ```dart
    // String in hex format (#AARRGGBB or #RRGGBB)
    final String brand = "#FF4000FF";
    ```

=== "Web"

    ```typescript
    // Hex format (#RRGGBB or #AARRGGBB) or CSS color values
    brand: "#4000FF"
    ```

### `ComponentStyle`

A style that defines the visual appearance of specific UI components like buttons and status views. Controls the background, foreground, and optional outline styling.

=== "Android"

    ```kotlin
    enum class AiutaComponentStyle {
        BRAND,
        CONTRAST,
        CONTRAST_INVERTED,
        BLURRED,
        BLURRED_WITH_OUTLINE
    }
    ```

=== "iOS"

    ```swift
    enum ComponentStyle {
        case brand
        case contrast
        case contrastInverted
        case blurred(hasOutline: Bool)
    }
    ```

=== "Flutter"

    ```dart
    enum AiutaComponentStyle {
        brand,
        contrast,
        contrastInverted,
        blurred,
        blurredWithOutline
    }
    ```

=== "Web"

    ```typescript
    type ComponentStyle = "brand" | "contrast" | "contrastInverted"
                        | "blurred" | "blurredWithOutline"
    ```

!!! info ""
    Shapes are independent and are not affected by component styles.

=== "`brand`"

    ![Button](/media/components/button-brand.png){ width=172 }

    - [`brand`](/sdk/developer/configuration/ui/theme/color.md#color-theme) background color
    - [`onDark`](/sdk/developer/configuration/ui/theme/color.md#color-theme) foreground color for labels and icons

=== "`contrast`"

    ![Button](/media/components/button-contrast.png){ width=200 }

    - [`onLight`](/sdk/developer/configuration/ui/theme/color.md#color-theme) background color
    - [`onDark`](/sdk/developer/configuration/ui/theme/color.md#color-theme) foreground color for labels and icons

=== "`contrastInverted`"

    ![Button](/media/components/button-contrast-inverted.png){ width=200 }

    - [`onDark`](/sdk/developer/configuration/ui/theme/color.md#color-theme) background color
    - [`onLight`](/sdk/developer/configuration/ui/theme/color.md#color-theme) foreground color for labels and icons

=== "`blurred`"

    ![Button](/media/components/button-blurred.png){ width=164 }

    - apply a blurred background that matches the color [`scheme`](/sdk/developer/configuration/ui/theme/color.md#color-scheme) (`light` or `dark`)
    - [`primary`](/sdk/developer/configuration/ui/theme/color.md#color-theme) foreground color for labels and icons

=== "`blurredWithOutline`"

    ![Button](/media/components/button-blurred-outline.png){ width=164 }

    - apply a blurred background that matches the color [`scheme`](/sdk/developer/configuration/ui/theme/color.md#color-scheme) (`light` or `dark`)
    - [`primary`](/sdk/developer/configuration/ui/theme/color.md#color-theme) foreground color for labels and icons
    - [`border`](/sdk/developer/configuration/ui/theme/color.md#color-theme) color for the outline

### `DataProvider`

Some SDK features need to persist data (e.g. upload history, generation history, onboarding completion, consent state). A `DataProvider` controls where and how this data is stored.

- **`BuiltIn`** — the SDK handles storage internally. No extra code is needed.
- **`Custom`** — you provide your own storage by implementing the required observable properties and callbacks. This lets you sync SDK state with your backend or use a custom persistence layer.

Each feature that supports a data provider declares its own specific properties and callbacks in its scheme page. The type is always `BuiltIn | Custom { ... }`.

=== "Android"

    ```kotlin
    // Sealed interface with two implementations
    sealed interface DataProvider

    // BuiltIn — singleton, SDK stores data internally
    object DataProviderBuiltIn : DataProvider

    // Custom — implement the interface
    interface DataProviderCustom : DataProvider {
        val items: StateFlow<List<T>>
        suspend fun addItems(items: List<T>)
        suspend fun deleteItems(items: List<T>)
    }
    ```

=== "iOS"

    ```swift
    // Enum with associated protocol for custom
    enum HistoryProvider {
        case userDefaults   // SDK stores in UserDefaults
        case dataProvider(DataProvider)
    }

    // Custom — implement the protocol
    protocol DataProvider {
        var items: Aiuta.Observable<[T]> { get async }
        func add(items: [T]) async
        func delete(items: [T]) async
    }
    ```

=== "Flutter"

    ```dart
    // Sealed class with two implementations
    sealed class DataProvider {}

    // BuiltIn — SDK stores data internally
    class DataProviderBuiltIn extends DataProvider {}

    // Custom — provide ValueListenable and callbacks
    class DataProviderCustom extends DataProvider {
        final ValueListenable<List<T>> items;
        final Future<void> Function(List<T>) addItems;
        final Future<void> Function(List<T>) deleteItems;
    }
    ```

=== "Web"

    ```typescript
    // BuiltIn uses IndexedDB (localStorage fallback)
    // Custom — provide callbacks in SDK configuration
    ```

### `Icon`

Type used for various UI icons throughout the SDK. Icons can be used in two ways:

- As a `template` image — the SDK will automatically color it based on where it's used
- As an `original` image — used without any color changes

=== "Android"

    ```kotlin
    class AiutaIcon(
        val iconResource: AiutaDrawableResource,
        val shouldDrawAsIs: Boolean = false
    )
    ```

=== "iOS"

    ```swift
    enum Icon {
        case url(URL, renderingMode: RenderingMode)
        case image(UIImage) // UIImage has its own renderingMode, SDK uses it
    }
    ```

=== "Flutter"

    ```dart
    class AiutaIcon {
        final String path;
        final AiutaRenderMode renderMode;
    }
    ```

=== "Web"

    ```typescript
    // SVG path data
    icon: "M12 2C6.48 2 2 6.48 2 12s4.48 10 ..."

    // External URL
    icon: "https://example.com/icon.svg"

    // Inline SVG elements
    icon: '<path d="M12 2..." fill="currentColor"/>'

    // Full SVG
    icon: '<svg viewBox="0 0 24 24">...</svg>'
    ```

### `Image`

A platform-specific type or `string` representing path to the image resource.

=== "Android"

    ```kotlin
    // Platform-agnostic drawable resource interface
    interface AiutaDrawableResource

    // Compose Multiplatform resource
    AiutaComposeDrawableResource(Res.drawable.my_image)

    // Android drawable resource ID
    AiutaAndroidDrawableRes(R.drawable.my_image)

    // Android Drawable instance
    AiutaAndroidDrawable(drawable)
    ```

=== "iOS"

    ```swift
    enum Image {
        case url(URL)
        case image(UIImage)
    }
    ```

=== "Flutter"

    ```dart
    // URL string or Flutter asset path
    final String image = "https://example.com/image.png";
    ```

=== "Web"

    ```typescript
    // Image URL
    image: string
    ```

### `Observable`

A type that can be watched by the SDK for changes.

=== "Android"

    ```kotlin
    // Kotlin coroutine StateFlow
    val state: StateFlow<T>
    ```

=== "iOS"

    ```swift
    // Custom wrapper class provided by the SDK
    let value: Aiuta.Observable<T>
    ```

=== "Flutter"

    ```dart
    // Flutter ValueListenable for reactive state
    ValueListenable<T> value;
    ```

=== "Web"

    ```typescript
    // Callback-based event handling via RPC methods
    onChanged: (value: T) => void
    ```

### `Shape`

A type that specifies the visual appearance of UI elements, such as corner radius. Depending on the platform and SDK implementation, it can also offer more configurations like corner curve types.

=== "Android"

    ```kotlin
    // Corner radius in density-independent pixels
    val imageL: Dp = 24.dp
    ```

=== "iOS"

    ```swift
    enum Shape {
        case continuous(radius: CGFloat)
        case circular(radius: CGFloat)
        case capsule
        case rectangular
    }
    ```

=== "Flutter"

    ```dart
    // Corner radius value
    final double imageL = 24.0;
    ```

=== "Web"

    ```typescript
    // Border radius in pixels
    imageL: number
    ```

### `TextStyle`

A type used to define text styling properties for various UI elements.

=== "Android"

    ```kotlin
    // Compose TextStyle
    val titleL: TextStyle = TextStyle(
        fontFamily = FontFamily.Default,
        fontSize = 24.sp,
        fontWeight = FontWeight.Bold,
        letterSpacing = (-0.01).sp,
        lineHeight = 28.sp
    )
    ```

=== "iOS"

    ```swift
    struct TextStyle {
        let font: UIFont
        let size: CGFloat
        let weight: UIFont.Weight
        let kern: CGFloat?
        let lineHeightMultiple: CGFloat?
    }
    ```

=== "Flutter"

    ```dart
    class AiutaTextStyle {
        final String fontFamily;
        final double fontSize;
        final FontWeight fontWeight;
        final double letterSpacing;
        final double lineHeight;
    }
    ```

=== "Web"

    ```typescript
    // CSS styles via theme configuration
    // or inline style properties
    ```

## Basic Types

### `Bool`

A boolean value (`true` or `false`).

=== "Android"

    ```kotlin
    val value: Boolean = true
    ```

=== "iOS"

    ```swift
    let value: Bool = true
    ```

=== "Flutter"

    ```dart
    final bool value = true;
    ```

=== "Web"

    ```typescript
    value: boolean
    ```

### `Callback`

A function type that can accept parameters and return a value.

=== "Android"

    ```kotlin
    val callback: (T) -> Unit
    ```

=== "iOS"

    ```swift
    let callback: (T) -> Void
    ```

=== "Flutter"

    ```dart
    void Function(T) callback;
    ```

=== "Web"

    ```typescript
    callback: (value: T) => void
    ```

### `List`

A collection type that holds an ordered sequence of elements.

=== "Android"

    ```kotlin
    val items: List<T>
    ```

=== "iOS"

    ```swift
    let items: [T]
    ```

=== "Flutter"

    ```dart
    final List<T> items;
    ```

=== "Web"

    ```typescript
    items: T[]
    ```

### `Map`

A collection type that associates keys with values, where each key is unique.

=== "Android"

    ```kotlin
    val map: Map<String, T>
    ```

=== "iOS"

    ```swift
    let map: [String: T]
    ```

=== "Flutter"

    ```dart
    final Map<String, dynamic> map;
    ```

=== "Web"

    ```typescript
    map: Record<string, T>
    ```

### `Number`

A numeric value (integer or floating-point).

=== "Android"

    ```kotlin
    val size: Dp = 24.dp       // dimensions
    val delay: Int = 1000      // milliseconds
    ```

=== "iOS"

    ```swift
    let value: CGFloat = 24.0
    ```

=== "Flutter"

    ```dart
    final double value = 24.0;
    ```

=== "Web"

    ```typescript
    value: number
    ```

### `Optional`

Indicates that a value can be omitted. When a feature or sub-feature is Optional, not providing it disables that functionality. When a property is Optional, the SDK uses a platform-specific default.

=== "Android"

    ```kotlin
    // Nullable type — omit or pass null to use default / disable
    val feature: Feature? = null
    val icon: AiutaIcon? = null
    ```

=== "iOS"

    ```swift
    // Optional type — nil to use default / disable
    let feature: Feature? = nil
    let icon: Icon? = nil
    ```

=== "Flutter"

    ```dart
    // Nullable type — null to use default / disable
    final Feature? feature;
    final AiutaIcon? icon;
    ```

=== "Web"

    ```typescript
    // Optional property — omit or set undefined to use default / disable
    feature?: Feature
    icon?: string
    ```

### `String`

A text value.

=== "Android"

    ```kotlin
    val text: String = "Hello"
    ```

=== "iOS"

    ```swift
    let text: String = "Hello"
    ```

=== "Flutter"

    ```dart
    final String text = "Hello";
    ```

=== "Web"

    ```typescript
    text: string
    ```



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
