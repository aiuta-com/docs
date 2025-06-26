# Configuration Guide

The **Aiuta Web SDK** is highly configurable and designed to seamlessly integrate with your platform.

## Basic Configuration

To integrate the Web SDK, include the following `<script>` tag on your website. Replace the placeholder with your actual `api-key`:

```html
<script src="" async id="aiuta-web-sdk-base" api-key=""></script>
```

### How to Obtain an `api-key`

To generate your `api-key`, sign up at the [Aiuta Developer Portal](https://developer.aiuta.com) and follow the provided instructions.

---

## Try-On Button Configuration

The Aiuta Web SDK uses a standardized configuration scheme to render Try-On buttons.

To display the Try-On button, include a `<div>` element with the required attributes:

- `data-sku-id` – Use your product's unique identifier as the value.
- `data-sku-catalog-name` _(optional)_ – If you provide this value, it will be used to generate the product. If omitted, a **default** catalog name will be used.

```html
<div class="aiuta-web-sdk" data-sku-id="" data-sku-catalog-name=""></div>
```

> ⚠️ Ensure this `<div>` is placed on your product page and populated with the correct `sku_id` and, optionally, `sku_catalog_name`.

---

## Button Style Configuration

Customize the appearance of the Try-On button using the style configuration below:

```js
const aiutaTryOn = new WebSdkButtonStyles();

aiutaTryOn.configs = {
  bt_bg_color: "", // Background color of the button
  bt_tx_color: "", // Text color of the button
  bt_fontFamily: "", // Font family for the button text
  bt_borderRadius: "", // Border radius of the button
};
```

---

## Button Action Configuration

You can define custom behavior for when the Try-On button is clicked:

```js
const aiutaTryOnButton = new AiutaWebSdkButtonAction();

aiutaTryOnButton.tryOnButtonAction = {
  onTryOnButtonClick: () => {
    // Your custom logic here
  },
};
```

---

## Summary

1. Add the SDK `<script>` tag with your `api-key`.
2. Insert the Try-On `<div>` with your `data-sku-id` and optionally `data-sku-catalog-name` on the product page.
3. Optionally, configure the button styles and click behavior as needed.

For more information, visit the [Aiuta Developer Portal](https://developer.aiuta.com).
