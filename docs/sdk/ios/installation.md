# Installation

Integrate [Aiuta iOS SDK :octicons-link-external-24:](https://github.com/aiuta-com/aiuta-ios-sdk){:target="_blank"} into your application.

## Depend on it

### Swift Package Manager

=== "`Package.swift`"

    Add AiutaSdk as a `dependencies` value of your `Package.swift`.

    ```swift
    dependencies: [
      .package(url: "https://github.com/aiuta-com/aiuta-ios-sdk.git", from: "{{ latest_ios() }}")
    ]
    ```

    Add dependency to your target
    ```swift
    .product(name: "AiutaSdk", package: "aiuta-ios-sdk")
    ```

=== "Xcode"

    - File > Add Package Dependencies...
    - Search `https://github.com/aiuta-com/aiuta-ios-sdk.git`
    - Select Dependency Rule "Up to Next Major" with `{{ latest_ios() }}`
    - Add Package to your project

    ![xcode](/media/sdk/ios-xcode.png){ width=550 }

### CocoaPods

[CocoaPods :octicons-link-external-24:](https://cocoapods.org) is a dependency manager for Cocoa projects. For usage and installation instructions, visit their website. To integrate Aiuta SDK into your Xcode project using CocoaPods, specify it in your `Podfile`:

```ruby
source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '13.0'
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

- :octicons-arrow-right-24: &nbsp; Initialize with [Configuration](configuration.md)

</div>
