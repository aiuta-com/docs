# Documentation Convention

Our team uses this public documentation to build our products. It serves as a single source of truth to ensure consistent implementation across different platforms.
We strive to adhere to consistent principles to maintain a coherent structure. Work on the convention is still ongoing.

## Check before publishing

Documentation is published automatically when merged into the `main` branch. Therefore, before merging a pull request, please check locally

<div class="annotate" markdown>
- __ZERO Warning policy__&nbsp; (1)
- the documentation is easy to read
- it adheres to accepted conventions
- you like it
</div>

1.  !!! danger "Strict mode"
      MKDocs configuration has `strict` parameter set to `true`. This will cause MkDocs to abort the build on any warnings.


??? question "How to set up a local preview?"
    {% include-markdown "team/docs/local-build.md" %}

## Links

### External

!!! warning "New tab/window"
    Always add 
    ```
    {:target="_blank"}
    ```
    for an external link to open it in a new tab or window

#### Visual mark    

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

#### Use root-relative links 

This leads to the same result but is easier to maintain in the future.

!!! note ""
    Root is `/docs`

=== ":material-check: Root-relative"

    ``` markdown
    [About SDK](/sdk/index.md)

    ![img](/media/about.png){ width=100 }
    ```
    <div class="result" markdown>
    [About SDK](/sdk/index.md)

    ![img](/media/about.png){ width=100 }
    </div>        


=== ":material-close: Relative"

    ``` markdown
    [About SDK](../../sdk/index.md)

    ![img](../../media/about.png){ width=100 }
    ```
    <div class="result" markdown>
    [About SDK](../../sdk/index.md)

    ![img](../../media/about.png){ width=100 }
    </div>        
    
#### Custom `doc` admonition

If you want to specifically highlight links as references to other parts of the documentation, use a custom `doc` [admonition :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){:target="_blank"} that has some special style settings

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

### Sources

Always provide links to sources and packages, if available, giving preference to [`grid cards` :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/grids/#using-card-grids){:target="_blank"}.

!!! example 
    ``` html
    <div class="grid cards" markdown>

    - :fontawesome-brands-flutter: [Pub.dev package :octicons-link-external-24:](https://pub.dev/packages/aiuta_flutter){:target="_blank"}
    - :fontawesome-brands-github: [Plugin sources :octicons-link-external-24:](https://github.com/aiuta-com/flutter-sdk){:target="_blank"}

    </div>
    ```
    <div class="result" markdown>
    <div class="grid cards" markdown>

    - :fontawesome-brands-flutter: [Pub.dev package :octicons-link-external-24:](https://pub.dev/packages/aiuta_flutter){:target="_blank"}
    - :fontawesome-brands-github: [Plugin sources :octicons-link-external-24:](https://github.com/aiuta-com/flutter-sdk){:target="_blank"}

    </div>
    </div>


## Code blocks

Instead of comments, give preference to [annotations :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/annotations/){:target="_blank"}, which can be much more detailed and contain active links, images, and instructions. Describe things in detail, keeping the code clean and free of comments. Don't forget to specify default values in the `example` [admonition :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){:target="_blank"}, if applicable.

!!! example
    ```` markdown
    ``` typescript
    Foo {
      bar: Bar // (1)!
    }
    ```

    1.  Here is annotaion with [link](#), image
    
        ![image](/media/images/imagePickerSample1.png){ width=50 }

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
        
        ![image](/media/images/imagePickerSample1.png){ width=50 }

        !!! example ""
            and default value
    </div>

### Schemes    

To describe a language-independent scheme or data model use a code block with `typescript` highlighting where

<div class="annotate" markdown>
- omit key constructs such as `class`, `new`, etc., that are redundant for the description
- avoid traling commas and semicolons, as well as colons between property definitions and opening brackets, cluttering up the scheme
- prefer `PascalCase` for types and `camelCase` for properties (1)
- define collections as `List<>` and `Map<>`
- denote enumerated / sealed types with  `|`, combined with tabs for their schemes
- indicate optional fields with `| null`
- indent with 2 spaces
</div>

1. except for the API, which uses `snake_case`

!!! example
    ````
    ``` typescript
    Foo {
      fooProperty1: String
      fooProperty2: Number | null
      fooProperty3: Bar1 | Bar2 | null

      fooEmbeddedeType {
        fooEmbeddedeTypeProperty1: String
      }
    }
    ```

    === "Bar1"
        ``` typescript
        Bar1 {
          bar1Property1: List<Bool>
        }
        ```
    
    === "Bar2"
        ``` typescript
        Bar2 {
          bar2Property1: Map<String, Bool>
        }
        ```    
    ````
    <div class="result" markdown>
    ``` typescript
    Foo {
      fooProperty1: String
      fooProperty2: Number | null
      fooProperty3: Bar1 | Bar2 | null

      fooEmbeddedeType {
        fooEmbeddedeTypeProperty1: String
      }
    }
    ```

    === "Bar1"
        ``` typescript
        Bar1 {
          bar1Property1: List<Bool>
        }
        ```
    
    === "Bar2"
        ``` typescript
        Bar2 {
          bar2Property1: Map<String, Bool>
        }
        ```  
    </div>

## Templates

If several pages of your documentation contain identical sections regarding repetitive reminders, a list of some questions, or system requirements, please create templates and include them with the `include-markdown` plugin

!!! example

    !!! warning ""
        Remove spaces in `{ %` `% }`. Careful, it works inside code blocks also.
        
    ```` markdown
    { % include-markdown "sdk/templates/flutter/requirements.md" % }
    ````

    <div class="result" markdown>
    {% include-markdown "sdk/templates/flutter/requirements.md" %}
    </div>

!!! warning "`include` macros"
    The `macros` plugin also provides its own `include` with the same syntax, but in the case of complex pages and nested indents, it often breaks the page layout, whereas `include-markdown` does not have this issue.

## Appearance

Keep documentation clean, uncluttered, divided into sections, use visual indicators to draw attention to specific areas (icons, admonitions, grid cards mentioned earlier).

### Dark theme

Let's respect people who prefer dark themes

- provide a contrasting alternative for monochrome images that cannot be colored, add `#only-light` or `#only-dark` at the end of the resource path
- define a contrasting background with `stylesheets/aiuta.css` for anything that has no alternative in the dark version

!!! example
    === "Markdown"
        ``` markdown
        <!-- good in both themes -->

        :material-format-color-text:{ .cl-aiuta }
        ![back24](/media/icons/back24.png#only-light){ width=12 } 
        ![back24](/media/icons/on-dark/back24.png#only-dark){ width=12 }
        ![close24](/media/icons/close24.png#only-light){ width=12 } 
        ![close24](/media/icons/on-dark/close24.png#only-dark){ width=12 }

        <!-- bad in a dark theme  -->

        :material-format-color-text:{ .cl-selection-background }
        ![back24](/media/icons/back24.png){ width=12 }
        ![close24](/media/icons/close24.png){ width=12 }
        ```

    === "`stylesheets/aiuta.css`"
        ``` css
        .cl-aiuta {
          color: #4000FF;
        }

        /* Light background for dark colors to contrast */
        .cl-primary,
        .cl-aiuta {
          background-color: #FFFFFF;
          border-radius: 6px;
        }
        ```

    <div class="result" markdown>
    <!-- good in both themes -->

    :material-format-color-text:{ .cl-aiuta }
    ![back24](/media/icons/back24.png#only-light){ width=12 } 
    ![back24](/media/icons/on-dark/back24.png#only-dark){ width=12 }
    ![close24](/media/icons/close24.png#only-light){ width=12 } 
    ![close24](/media/icons/on-dark/close24.png#only-dark){ width=12 }

    <!-- bad in a dark theme  -->

    :material-format-color-text:{ .cl-selection-background }
    ![back24](/media/icons/back24.png){ width=12 }
    ![close24](/media/icons/close24.png){ width=12 }
    </div>

    !!! info ""
        Swich docs to a dark theme using :material-brightness-7:/:material-brightness-4: toggle in the header to see the difference

### Custom icons

If you need a special icon, you couldn't find a suitable one among the huge number [available icons :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/){:target="_blank"}, and want to export yours from Figma and place it in the `overrides/.icons` directory, please edit the exported `svg` file manually, replacing the fill color (usually `white` or `black` for icons) with the `currentColor` to match current typeface color.

!!! example
    === ":material-close: Original Figma export"
        ``` xml
        <svg width="29" height="29" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="29" height="29" rx="4" fill="white"/>
        </svg>
        ```
    === ":material-check: Your fix"
        ``` xml
        <svg width="29" height="29" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="29" height="29" rx="4" fill="currentColor"/>
        </svg>
        ```

!!! info ""
    In the current version of Figma, you can set the `currentColor` as a value but it will unfortunately be replaced with some explicit color, probaly `#CCCCCC`

??? question "How to use custom icons?"
    Custom icons, which are located in the `overrides/.icons` directory, will be available to use by putting the valid path between two colons, and replacing `/` with `-`

    !!! example
        ``` markdown
        :aiuta-logo: :aiuta-favicon:
        ```
        <div class="result" markdown>
        :aiuta-logo: :aiuta-favicon:
        </div>

## Common sense

Use it.
