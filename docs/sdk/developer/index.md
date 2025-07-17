---
hide:
  - toc
---
# Developer Section

The Developer Section provides an overview of the configuration and model schemes that are common to all SDK implementations. By understanding these core concepts, developers can ensure a uniform approach to implementing the SDK, which helps maintain consistency and reduces redundancy in documentation.

## SDK integration

In general, all SDK implementations are integrated in three steps:

1. Add dependency
2. Initialize with [Configuration](/sdk/developer/configuration/index.md)
3. Call SDK UI by passing the [Product](/sdk/developer/product.md)

??? abstract "Type Definitions & Naming Convention"
    {% include-markdown "sdk/templates/developer/type-definitions.md" %}

!!! tip "Annotations in schemes"
    Don't miss them - click :material-information-outline: for more details

## Quick Start

Check out the quick start guide to get started with the platform

{% include-markdown "sdk/templates/quick-start.md" %}
