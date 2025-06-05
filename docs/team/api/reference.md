---
title: Fashion External API
template: swagger-ui.html
hide:
  - navigation
  - toc
---

<script>
    window.onload = function() {
        const ui = SwaggerUIBundle({
            url: "https://api.aiuta.com/digital-try-on/v1/openapi.json",
            dom_id: '#swagger-ui',
            deepLinking: true,
            defaultModelsExpandDepth: 0,
        });

        window.ui = ui;
    };
</script>
