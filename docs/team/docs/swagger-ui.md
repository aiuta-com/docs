# Swagger UI

To use Swagger UI, [`dist 5.22.0` :octicons-link-external-24:](https://github.com/swagger-api/swagger-ui/releases/tag/v5.22.0){:target="_blank"} is built in. Ready-made plugins are not used, as none of them allowed us to fully configure Swagger UI, for example, both enable `deepLinking` and synchronize styles with Material for MkDocs.

## Adding a Swagger UI page

- Full screen without navigation and ToC is used
- A special template has been added to apply style synchronization

``` html
---
title: You page title <!-- (1)! -->
template: swagger.html <!-- (2)! -->
hide:
  - navigation <!-- (3)! -->
  - toc
---

<script>
    window.onload = function() {
        const ui = SwaggerUIBundle({
            url: "openapi.json", // (4)!
            dom_id: '#swagger-ui', // (5)!
            deepLinking: true,  // (6)!
        });

        window.ui = ui;
    };
</script>
```

1.  Title your page accodring to the title of `openapi.json` `info.title`
2.  Use this template to have a full-width page with embedded `swagger-ui-bundle` and custom styles applied to match Material for MkDocs theme
3.  Hide everything regarding to the navigation and ToC
4.  Provide a root-relative path or an external link to the `openapi.json`
5.  Template `swagger.html` provides `<div id="swagger-ui"></div>` to embed the swagger ui
6.  Configure anything you want accodring to [Swagger UI Configuration :octicons-link-external-24:](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/){:target="_blank"}

!!! example
    [API Reference](/api/reference) page
