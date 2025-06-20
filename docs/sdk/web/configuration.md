# Configuration Guide

The Aiuta Web SDK is highly configurable to meet your specific needs.

## Basic Configuration

The Web SDK is configured using the `<script></script>`, which contains several keys:

```dart
<script src="" async="true" id="aiuta-web-sdk-base" api-key=""></script>
```
??? question "How create `api-key` ?"
    To be create `api-key` you must sign up bellow Aiuta Portal Website and follow documentation.
    https://developer.aiuta.com
    
### Configuration Scheme for Try-on button

The Aiuta SDK for Web employs a standardized configuration scheme.
Where you want to see Try-On button you need to put the `div` element passing necessary elements.
Those keys you can find after generation products.

1. data-sku-id
   - After generation Aiuta is providing `sku_id`
2. data-sku-catalog-name
   - After generation Aiuta is providing `sku_catalog_name`

### Configuration Scheme for Try-on button styles

```dart
const aiutaTryOn = new WebSdkButtonStyles()

aiutaTryOn.configs = {
   bt_bg_color: '', // Background color for Try On buttons
   bt_tx_color: '', // Text color for Try On buttons
   bt_fontFamily: "" // Text font for Try On buttons
   bt_borderRadius: "" // Border radius for Try On buttons
}
```

### Configuration Scheme for Try-on button action

```dart
const aiutaTryOnButton = new AiutaWebSdkButtonAction()

aiutaTryOnButton.tryOnButtonAction = {
   onTryOnButtonClick: () => {} // Your Function here
}
```

### General cases

When make sure that have necessary keys we can add HTML `div` tag in your dom where you want to see Try-on button.
Mainaly this tag you need to use in product page.
After opening product page you need to replace `data-sku-id` and `data-sku-catalog-name` values respective your generated product `sku_id` and `sku_catalog_name`

```dart
<div class="aiuta-web-sdk" data-sku-id="" data-sku-catalog-name=""></div>
```
