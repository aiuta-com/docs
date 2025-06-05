---
title: Digital Try On
template: swagger-ui.html
hide:
#   - navigation
  - toc
---

<script>
    window.onload = function() {
        const ui = SwaggerUIBundle({
            url: "/api/try-on/openapi.json",
            dom_id: '#swagger-ui',
            deepLinking: true,
            defaultModelsExpandDepth: 0,
        });

        window.ui = ui;
    };
</script>
