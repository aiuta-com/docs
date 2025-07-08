The sequence diagram of executing a virtual try-on operation.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation

    opt Cart
        USR->>SDK: Tap Add to cart
        SDK->>SDK: Close UI
        SDK->>APP: Call addToCart (product ID)
        APP-->>USR: Cart
    end

    opt Share
        USR->>SDK: Tap Share button
        SDK-->>USR: Show system share dialog
        Note over SDK,USR: Generated image to share
        USR->>SDK: Complete sharing
    end

```
