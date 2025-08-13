# Web SDK Demo

This page shows how Aiuta Web SDK can be used in your fashion e-commerce platform. Click the “Try on” button in the sample catalog or on the product pages to see the virtual try-on feature.

<script src="https://static.aiuta.com/sdk/v0.0.51/index.umd.js"></script>

<script>
    const aiuta = new Aiuta("{{ aiuta.api_key }}");
    console.log('Aiuta SDK initialized successfully');

    function startTryOn(productId) {
        console.log(`Starting try-on for product ID: ${productId}`);
        aiuta.startGeneration(productId);
    }
</script>

=== "Catalog"

    <div class="grid cards catalog" markdown>

{{ gen_web_catalog() }}

    </div>

{{ gen_web_pages(6) }}
