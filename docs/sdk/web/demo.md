# Web SDK Demo Page

This page showcases how AIUTA's Web SDK can be integrated into your fashion e-commerce platform. Below, you'll find a sample product page demonstrating the SDK's capabilities. Click the "Try on" button to see the virtual try-on feature in action.

<script src="https://web-sdk.aiuta.com/api/sdk" async id="aiuta-web-sdk-base" api-key="{{ aiuta.api_key }}"></script>

<script>
    function openWebSdk() {
        if (typeof MySDK === 'undefined') {
            setTimeout(openWebSdk, 100);
            return;
        }
        
        MySDK.openModal();
    }

    function initWebSdkButton() {
        if (typeof MySDK === 'undefined') {
            setTimeout(initWebSdkButton, 100);
            return;
        }

        const aiutaTryOn = new AiutaWebSdkButtonStyles();
        aiutaTryOn.configs = {
            bt_bg_color: "#4000FF",
            bt_tx_color: "#FFFFFF",
            bt_fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, sans-serif",
            bt_borderRadius: "2px",
        };

    }

    initWebSdkButton();
</script>

## Sample product page

!!! example "{{ test_products(0).category_google_name }}"

    ![Product]({{ test_products(0).image_urls[0] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[1] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[2] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[3] }}){ width=100 }
    
    <h2> {{ test_products(0).title }}</h2>

    {{ test_products(0).description }}

    <div class="grid cards" markdown>


      -   Default Web SDK button
      
          ---

          <div class="aiuta-web-sdk" data-sku-id="{{ test_products(0).sku_id }}" data-sku-catalog-name="{{ test_products(0).sku_catalog_name }}"></div>

      -   Custom Try on button
      
          ---

          [Try on :aiuta-favicon:](javascript:openWebSdk()){ .md-button }

    </div>

## How to implement

This sample uses integration via Script Tag.

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [use the SDK with `<script>`](/sdk/web/configuration.md)

</div>
