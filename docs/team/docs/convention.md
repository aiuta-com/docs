# Documentation Convention

In public documentation, we strive to adhere to consistent principles to maintain a coherent structure for describing our products. Work on the convention is still ongoing.

## Check before publishing

Documentation is published automatically when merged into the `main` branch. Therefore, before merging a pull request, please check locally that

- all links work
- all images/icons are displayed
- the documentation is easy to read
- it adheres to accepted conventions
- you like it

??? question "How to set up a local preview?"
    To do this, you will need to install [Material for MKDocs :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/getting-started/){:target="_blank"} and some plugins:

    ```sh
    pip install mkdocs-material
    pip install mkdocs-minify-plugin
    pip install mkdocs-include-markdown-plugin
    ```

    After that, in the root of your repository clone, simply run

    ```sh
    mkdocs serve
    ```

    In the console you will see something like
    ```
    INFO    -  [10:46:26] Serving on http://127.0.0.1:8000/
    ```
    Open this link and check it out.

## Links

### External

!!! warning "Always add `{:target="_blank"}`"
    for an external link to open it in a new tab or window

Always visually mark links that lead outside the documentation site. There are two options:

=== "Explicit external link icon"

    Add this icon to the end of the link title

    ```
    :octicons-link-external-24:
    ```

    !!! example
        ``` markdown
        [aiuta.com :octicons-link-external-24:](https://aiuta.com){:target="_blank"}
        ```

        <div class="result" markdown>
        [aiuta.com :octicons-link-external-24:](https://aiuta.com){:target="_blank"}
        </div>

=== "Call to action title when using card grids"

    When grouping links into blocks with [`grid cards` :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/grids/#using-card-grids){:target="_blank"} you can omit the icon if you use an explicit action in the link title, such as "Open", "Download", etc.

    !!! example
        ``` html
        <div class="grid cards" markdown>

        - :fontawesome-brands-google-play: [Get it on __Google Play__](https://play.google.com/store/apps/details?id=com.aiuta.fashionsdk.demo){:target="_blank"}
        - :fontawesome-brands-shopify: [View in the __Shopify__ app store](https://shopify.aiuta.com){:target="_blank"}

        </div>
        ```
        
        <div class="grid cards" markdown>

        - :fontawesome-brands-google-play: [Get it on __Google Play__](https://play.google.com/store/apps/details?id=com.aiuta.fashionsdk.demo){:target="_blank"}
        - :fontawesome-brands-shopify: [View in the __Shopify__ app store](https://shopify.aiuta.com){:target="_blank"}
        
        </div>

### Internal

There are no special requirements for internal links, except for the following recommendation: if you want to specifically highlight them as references to other parts of the documentation, use a custom `doc` [admonition :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){:target="_blank"} that has some special style settings

=== "Single link"

    !!! example
        ``` markdown
        !!! doc "To understand this, see [that](#)"
        ```

        <div class="result" markdown>
        !!! doc "To understand this, see [that](#)"
        </div>    

=== "Multiple links"
    !!! example
        ``` markdown
        !!! doc "For full context, see"

            - [this](#)
            - maybe [that](#)
            - and something [more](#)
        ```

        <div class="result" markdown>
        !!! doc "For full context, see"

            - [this](#)
            - maybe [that](#)
            - and something [more](#)

        </div>

## Code blocks

Instead of comments, give preference to [annotations :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/annotations/){:target="_blank"}, which can be much more detailed and contain active links, images, and instructions. Describe things in detail, keeping the code clean and free of comments. Don't forget to specify default values in the example instructions.

!!! example
    ```` markdown
    ``` typescript
    Foo {
      bar: Bar // (1)!
    }
    ```

    1.  Here is annotaion with [link](#), image
    
        ![image](../../media/images/imagePickerSample1.png){ width=50 }

        !!! example ""
            and default value
            
    ````

    <div class="result" markdown>
    ``` typescript
    Foo {
      bar: Bar // (1)!
    }
    ```

    1.  Here is annotaion with [link](#), image
        
        ![image](../../media/images/imagePickerSample1.png){ width=50 }

        !!! example ""
            and default value
    </div>

## Templates

If some pages of your documentation have the same parts regarding repetitive reminders, a list of some questions, or system requirements, please create templates and include them with the `include-markdown`

!!! example

    !!! warning ""
        `%` instead of `#`. Careful, it works even inside code blocks.
        
    ```` markdown
    {# include-markdown "sdk/templates/flutter/requirements.md" %}
    ````

    <div class="result" markdown>
    {% include-markdown "sdk/templates/flutter/requirements.md" %}
    </div>
