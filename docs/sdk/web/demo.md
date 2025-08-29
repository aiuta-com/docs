# Web SDK Demo

This page shows how Aiuta Web SDK can be used in your fashion e-commerce platform. Click the “Try on” button in the sample catalog or on the product pages to see the virtual try-on feature.

<script src="https://static.aiuta.com/sdk/v0/index.umd.js"></script>

<script>
    let aiuta = null;

    function initWebSdk() {
        aiuta = new Aiuta();

        aiuta.initWithJwt({
            subscriptionId: "{{ aiuta.demo.subscription_id }}",
            getJwt: async (params) => {
                console.log('getJwt() called with params:', params);
                const response = await fetch("{{ aiuta.demo.get_jwt_url }}", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(params)
                });
                const data = await response.json();
                const token = data.token;
                console.log('JWT resolved');
                return token;
            },
            analytics: (eventName, data) => {
                console.log('Aiuta Analytics Event:', eventName, data);
            }
        });

        console.log('Aiuta SDK initialized');
    }

    function startTryOn(productId) {
        if (!aiuta)  {
            initWebSdk();
        }
        console.log(`Starting try-on for product ID: ${productId}`);
        aiuta.startGeneration(productId);
    }

    window.onload = () => {
        initWebSdk();
    };
</script>

=== "Catalog"

    <div class="grid cards catalog" markdown>

{{ gen_web_catalog() }}

    </div>

{{ gen_web_pages(6) }}
