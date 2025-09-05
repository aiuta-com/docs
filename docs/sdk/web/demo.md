# Web SDK Demo

This page shows how Aiuta Web SDK can be used in your fashion e-commerce platform. Click the “Try on” button in the sample catalog or on the product pages to see the virtual try-on feature.

<script>
    let aiuta = null;

    const config = {
        webSdkPath: "{{ aiuta.demo.web_sdk.path }}",
        webSdkUrl: "{{ aiuta.demo.web_sdk.url }}",
        subscriptionId: "{{ aiuta.demo.subscription_id }}",
        getJwtUrl: "{{ aiuta.demo.get_jwt_url }}",
        customCssUrl: "{{ aiuta.demo.web_sdk.css }}"
    };

    function loadWebSdk() {
        return new Promise((resolve, reject) => {
            const isLocalhost = window.location.hostname === 'localhost' || 
                               window.location.hostname === '127.0.0.1' || 
                               window.location.hostname === '';
            
            if (isLocalhost) {
                console.log('Loading local Aiuta SDK');
                tryLoadLocal();
            } else {
                console.log('Loading Aiuta SDK from CDN');
                loadFromCDN();
            }

            function tryLoadLocal() {
                const localScript = document.createElement('script');
                localScript.src = config.webSdkPath;
                localScript.onload = () => {
                    console.log('Loaded local Aiuta SDK');
                    resolve();
                };
                localScript.onerror = () => {
                    console.log('Local SDK not found, loading from CDN');
                    document.head.removeChild(localScript);
                    loadFromCDN();
                };
                document.head.appendChild(localScript);
            }
            
            function loadFromCDN() {
                const cdnScript = document.createElement('script');
                cdnScript.src = config.webSdkUrl;
                cdnScript.onload = () => {
                    console.log('Loaded Aiuta SDK from CDN');
                    resolve();
                };
                cdnScript.onerror = () => {
                    reject(new Error('Failed to load Aiuta SDK from CDN'));
                };
                document.head.appendChild(cdnScript);
            }
        });
    }

    async function initWebSdk() {
        await loadWebSdk();
        
        aiuta = new Aiuta({
            auth: {
                subscriptionId: config.subscriptionId,
                getJwt: async (params) => {
                    console.log('getJwt() called with params:', params);
                    const response = await fetch(config.getJwtUrl, {
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
                }
            },
            userInterface: {
                customCssUrl: config.customCssUrl
            },
            analytics: {
                handler: {
                    onAnalyticsEvent: (event) => {
                        console.log('Aiuta Analytics Event:', event);
                    }
                }
            }
        });

        console.log('Aiuta SDK initialized');
    }

    async function startTryOn(productId) {
        if (!aiuta)  {
            await initWebSdk();
        }
        
        console.log(`Starting try-on for product ID: ${productId}`);
        aiuta.startGeneration(productId);
    }

    window.onload = async () => {
        await initWebSdk();
    }
</script>

=== "Catalog"

    <div class="grid cards catalog" markdown>

{{ gen_web_catalog() }}

    </div>

{{ gen_web_pages(6) }}
