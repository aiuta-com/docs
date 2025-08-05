# Web SDK Demo Page

This page showcases how AIUTA's Web SDK can be integrated into your fashion e-commerce platform using the NPM package. Below, you'll find a sample product page demonstrating the SDK's capabilities.

<!-- Load the bundled Aiuta SDK -->
<script src="/js/aiuta-try-on-sdk.js"></script>

## Sample product page

!!! example "{{ test_products(0).category_google_name }}"

    ![Product]({{ test_products(0).image_urls[0] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[1] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[2] }}){ width=100 }
    ![Product]({{ test_products(0).image_urls[3] }}){ width=100 }
    
    <h2> {{ test_products(0).title }}</h2>

    {{ test_products(0).description }}

    ---

    <!-- SDK components will be mounted here -->
    <aiuta-try-on-sdk-provider apikey="{{ aiuta.api_key }}">
        <aiuta-try-on-button 
            skuid="{{ test_products(0).sku_id }}" 
            skucatalogname=""
            dynamicstyles='{"bt_bg_color": "#6366f1", "bt_tx_color": "#ffffff", "bt_fontFamily": "Roboto, sans-serif", "bt_borderRadius": "8px"}'>
            Try On
        </aiuta-try-on-button>
    </aiuta-try-on-sdk-provider>

## How to implement

This sample uses integration via NPM package as documented at [aiuta-try-on-sdk](https://www.npmjs.com/package/aiuta-try-on-sdk).

### Implementation Steps:

1. **Install the NPM package:**
   ```bash
   npm install aiuta-try-on-sdk
   ```

2. **Include the SDK script:**
   ```html
   <script src="/js/aiuta-try-on-sdk.js"></script>
   ```

3. **Use the components in your HTML:**
   ```html
   <aiuta-try-on-sdk-provider apikey="your-api-key">
       <aiuta-try-on-button 
           skuid="your-sku-id" 
           skucatalogname="optional-catalog"
           dynamicstyles='{"bt_bg_color": "#6366f1", "bt_tx_color": "#ffffff"}'>
           Try On
       </aiuta-try-on-button>
   </aiuta-try-on-sdk-provider>
   ```

<div class="grid cards" markdown>

- :octicons-arrow-right-24: Learn how to [use the SDK with NPM](/sdk/web/configuration.md)

</div>
