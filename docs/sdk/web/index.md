# Web SDK

The Aiuta Web SDK provides a virtual try-on solution for your fashion e-commerce platform using [Aiuta Virtual Try On API](/api/try-on/index.md).

{% include-markdown "sdk/templates/intro-links.md" %}

## Quick Start

```html

<script src="https://static.dev.aiuta.com/sdk/{{ latest(web) }}/index.umd.js"></script>

<script>
    var aiuta = new Aiuta("your_api_key"); // (1)!
    aiuta.startGeneration("your_product_id");
</script>
```

1. The `api_key` is used to authenticate all outgoing requests from the Aiuta SDK to the [Aiuta API](/api/try-on/index.md). This key ensures that the requests are linked to your account, allowing the SDK to access the necessary resources and services provided by Aiuta.

    !!! doc "Please see [Obtaining credentials](/api/getting-started.md#obtaining-credentials) for instructions on how to get your `api_key`"

## Sources and Demo

<div class="grid cards" markdown>

- :fontawesome-brands-github: [Sources :octicons-link-external-24:]({{ repo(web) }}){:target="_blank"}
- :aiuta-app: [Demo](/sdk/web/demo.md)

</div>
