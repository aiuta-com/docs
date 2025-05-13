# Installation

This guide will help you integrate the Aiuta SDK into your iOS application.

## CocoaPods

Add the following line to your Podfile:

```ruby
pod 'AiutaSDK'
```

Then run:

```bash
pod install
```

## Swift Package Manager

1. In Xcode, go to File > Add Packages...
2. Enter the package repository URL
3. Select the version you want to use
4. Click Add Package

## Manual Installation

1. Download the latest SDK release
2. Drag the `AiutaSDK.framework` into your project
3. Make sure "Copy items if needed" is checked
4. Add the framework to your target's "Frameworks, Libraries, and Embedded Content" section

## Configuration

After installation, you'll need to configure the SDK. See the [Configuration](configuration.md) guide for details.

## Next Steps

- [Basic Usage](basic-usage.md)
- [Configuration](configuration.md)
- [Virtual Try-On](virtual-try-on.md) 