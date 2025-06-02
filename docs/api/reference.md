---
title: Fashion External API
template: swagger.html
hide:
  - navigation
  - toc
---

<script>
    window.onload = function() {
        const ui = SwaggerUIBundle({
            url: "/api/openapi.json",
            dom_id: '#swagger-ui',
            deepLinking: true,
            defaultModelsExpandDepth: 0,
        });

        window.ui = ui;
    };
</script>
