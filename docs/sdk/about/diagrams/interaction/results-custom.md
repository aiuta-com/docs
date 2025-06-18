The sequence diagram of executing a virtual try-on operation.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/about/common-sd-participants.md" %}

    Note over SDK,API: After successful try-on generation

    opt Cart
        USR->>SDK: Tap Add to cart
        SDK->>SDK: Close UI
        SDK->>APP: Call addToCart (product ID)
        APP-->>USR: Cart
    end

    opt Wishlist
        USR->>SDK: Tap Wishlist button
        SDK->>APP: Toggle setProductInWishlist (product ID)
        APP->>BE: Update wishlist
        APP-->>SDK: Update observable wishlistProductIds
        SDK->>SDK: Update wishlist button state
    end

    opt Share
        USR->>SDK: Tap Share button
        SDK->>APP: Call getShareText (product IDs)
        APP-->>SDK: Return share text
        SDK-->>USR: Show system share dialog
        Note over SDK,USR: Generated image and optional text to share
        USR->>SDK: Complete sharing
    end

```

!!! doc "See details about" 
    
    - [<span class="md-sequence-number">6-8</span> Wishlist integration](/sdk/about/developer/configuration/#wishlist)
    - [<span class="md-sequence-number">11</span> Share functionality](/sdk/about/developer/configuration/#share) 