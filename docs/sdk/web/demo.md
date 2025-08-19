# Web SDK Demo

This page shows how Aiuta Web SDK can be used in your fashion e-commerce platform. Click the “Try on” button in the sample catalog or on the product pages to see the virtual try-on feature.

<script src="https://static.aiuta.com/sdk/v0/index.umd.js"></script>

<script>
    let aiuta = null;

    window.onload = () => {
        aiuta = new Aiuta();
        aiuta.initWithApiKey("{{ aiuta.api_key }}");
        console.log('Aiuta SDK initialized on load');
    };

    function startTryOn(productId) {
        if (!aiuta)  {
            aiuta = new Aiuta();
            aiuta.initWithApiKey("{{ aiuta.api_key }}");
            console.log('Aiuta SDK initialized on demand');
        }
        console.log(`Starting try-on for product ID: ${productId}`);
        aiuta.startGeneration(productId);
    }
</script>

=== "Catalog"

    <div class="grid cards catalog" markdown>

{{ gen_web_catalog() }}

    </div>

{{ gen_web_pages(6) }}
