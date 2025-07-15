# Installation

Integrate [Aiuta iOS SDK :octicons-link-external-24:](https://github.com/aiuta-com/aiuta-ios-sdk){:target="_blank"} into your application.

## Depend on it

=== "Swift Package Manager"

    [SwiftPM :octicons-link-external-24:](https://www.swift.org/documentation/package-manager/){:target="_blank"} distribution of the Aiuta iOS SDK supports minimum deployment `iOS 13`

    ??? question "Need a lower minimum deployment?"
        If you need support of minimum deployment `iOS 12`, you are probably using some kind of cross-platform solution. In this case, please take a look at [CocoaPods distribution](/sdk/ios/installation.md#__tabbed_1_2), and also note that Aiuta provides a plugin-wrapper for [Flutter](/sdk/flutter/index.md). You can also use the Kotlin MultiPlatform version of the [Android SDK](/sdk/android/index.md).

    === "Xcode"

        - File > Add Package Dependencies...
        - Enter Package URL:
        ```
        {{ repo_ios() }}
        ```
        - Select Dependency Rule `Up to Next Major` with `{{ latest_ios() }}`
        - Add Package to your project

        ![xcode](/media/sdk/ios-xcode.png){ width=550 }
        
    === "`Package.swift`"

        Add AiutaSdk `package` to the `dependencies` value of your `package`

        ```swift
        .package(url: "{{ repo_ios() }}", from: "{{ latest_ios() }}")
        ```

        Add AiutaSdk `product` to the `dependencies` value of your `target`

        ```swift
        .product(name: "AiutaSdk", package: "aiuta-ios-sdk")
        ```

=== "CocoaPods"

    [CocoaPods :octicons-link-external-24:](https://cocoapods.org){:target="_blank"} distribution of the Aiuta iOS SDK supports minimum deployment `iOS 12`, but it still available to operate only with `if #available(iOS 13.0.0, *)`

    ```ruby
    source 'https://github.com/CocoaPods/Specs.git'
    platform :ios, '12.0'
    use_frameworks!

    target 'MyApp' do
      pod 'AiutaSdk', '~> {{ latest_ios() }}'
    end
    ```

## Import it

Now in your Swift code, you can use:

```swift
import AiutaSdk
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Quick Test](/sdk/ios/quick-test.md) SDK Propely Integrated
- :octicons-arrow-right-24: Setup with [Configuration](/sdk/ios/configuration.md)

</div>
