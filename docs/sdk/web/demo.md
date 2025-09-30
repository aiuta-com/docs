# Web SDK Demo

This page shows how Aiuta Web SDK can be used in your fashion e-commerce platform. Click the “Try on” button in the sample catalog or on the product pages to see the virtual try-on feature.

<script>
    window.aiuta = window.aiuta || {};
    window.aiuta.sdk = window.aiuta.sdk || null;
    
    if (!window.aiuta.config) {
        window.aiuta.config = {
            webSdkPath: "{{ aiuta.demo.web_sdk.path }}",
            webSdkUrl: "{{ aiuta.demo.web_sdk.url }}",
            subscriptionId: "{{ aiuta.demo.subscription_id }}",
            getJwtUrl: "{{ aiuta.demo.get_jwt_url }}",
            customCssUrl: "{{ aiuta.demo.web_sdk.css }}"
        };
    }

    function loadWebSdk() {
        return new Promise((resolve, reject) => {
            const isLocalhost = window.location.hostname === 'localhost' || 
                               window.location.hostname === '127.0.0.1' || 
                               window.location.hostname.startsWith('192.168.') ||
                               window.location.hostname.endsWith('.local') ||
                               window.location.hostname === '';
            
            if (isLocalhost) {
                tryLoadLocal();
            } else {
                loadFromCDN();
            }

            function tryLoadLocal() {
                const localScript = document.createElement('script');
                localScript.src = window.aiuta.config.webSdkPath;
                localScript.onload = () => {
                    console.debug('Aiuta Web SDK loaded from local', window.aiuta.config.webSdkPath);
                    resolve();
                };
                localScript.onerror = () => {
                    document.head.removeChild(localScript);
                    loadFromCDN();
                };
                document.head.appendChild(localScript);
            }
            
            function loadFromCDN() {
                const cdnScript = document.createElement('script');
                cdnScript.src = window.aiuta.config.webSdkUrl;
                cdnScript.onload = () => {
                    console.debug('Aiuta Web SDK loaded from CDN', window.aiuta.config.webSdkUrl);
                    resolve();
                };
                cdnScript.onerror = () => {
                    reject(new Error('Failed to load Aiuta Web SDK from CDN', {
                        cause: { url: window.aiuta.config.webSdkUrl }
                    }));
                };
                document.head.appendChild(cdnScript);
            }
        });
    }

    async function initWebSdk() {
        if (window.aiuta.sdk) {
            console.warn('Aiuta SDK already initialized');
            return;
        }
        
        await loadWebSdk();
        
        window.aiuta.sdk = new Aiuta({
            auth: {
                subscriptionId: window.aiuta.config.subscriptionId,
                getJwt: async (params) => {
                    console.log('getJwt() called with params:', params);
                    const response = await fetch(window.aiuta.config.getJwtUrl, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(params)
                    });
                    const data = await response.json();
                    const token = data.token;
                    console.log('getJwt() did resolve token');
                    return token;
                }
            },
            userInterface: {
                customCssUrl: window.aiuta.config.customCssUrl,
                iframeStyles: {
                    borderRadius: "12px",
                    top: "120px",
                    right: "18px"
                }
            },
            analytics: {
                handler: {
                    onAnalyticsEvent: (event) => {
                        console.log(event);
                    }
                }
            },
            debugSettings: {
                isLoggingEnabled: true
            },
            testTitle: "Test"
        });
    }

    async function startTryOn(productId) {
        if (!window.aiuta.sdk)  {
            await initWebSdk();
        }
        
        window.aiuta.sdk.tryOn(productId);
    }

    window.onload = async () => {
        if (!window.aiuta.sdk) {
            await initWebSdk();
        }
    }
</script>

=== "Catalog"

    <div class="grid cards catalog" markdown>

{{ gen_web_catalog() }}

    </div>

{{ gen_web_pages(6) }}
