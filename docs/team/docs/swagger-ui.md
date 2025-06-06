---
hide:
  - toc
---
# Swagger UI

To use Swagger UI, [`dist 5.22.0` :octicons-link-external-24:](https://github.com/swagger-api/swagger-ui/releases/tag/v5.22.0){:target="_blank"} has been built into the docs and a special `swagger-ui.html` template has been added to provide:

- Swagger UI Bundle with its `swagger-ui-bundle.js` and `swagger-ui.css`
- Additional `swagger-ui.extra.css` to syncronize styles with Material for MkDocs
- Default `deepLinking` enabled, models collapsed and single `dom_id` specified

## Adding a Swagger UI page

Required dependencies are included in the `swagger-ui.html` template, just 

1. Use this template as described below
2. Initialize `SwaggerUI` with the necessary parameters

``` html
---
# title: You page title <!-- (1)! -->
template: swagger-ui.html <!-- (2)! -->
hide:
#   - navigation <!-- (3)! -->
  - toc <!-- (4)! -->
---
<!-- (5)! -->
<script>
  SwaggerUI({
    url: "openapi.json" // (6)!
  });
</script>
```

1.  Optionally title your page accodring to the `info.title` from yours `openapi.json`

    !!! example ""
        By default, the page title will be the same as the name of the corresponding `nav` element from `mkdocs.yml`

2.  Use this template to have a embedded `swagger-ui-bundle` and custom styles applied to match Material for MkDocs theme
3.  Consider hiding the navigation to increase the width of the Swagger UI interface
4.  Preferably hide the table of contents, especially if you do not have any additional content on the page
5.  You can add any markdown content here if you want. Swagger UI will be displayed below this content, regardless of the script location.

    !!! warning
        The `swagger-ui.html` template does not insert an implicit `h1` header for the page, as the Swagger UI has its own header that has the same style.
        
        Therefore, if you add your own markdown content above the Swagger UI, add an explicit
        ``` markdown
        # Page header
        ```

6.  Provide __required__ root-related path or an external link to the `openapi.json` and __optionally__ configure anything you want

    [Swagger UI Configuration :octicons-link-external-24:](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/){:target="_blank"}

    !!! example ""
        The `swagger-ui.html` template has 
        ``` html
        <div id="swagger-ui"></div>
        ```
        to embed single Swagger UI below page content and <br>
        adds this __default__ values to the `SwaggerUI` configuration:

        - `dom_id: '#swagger-ui'` for the general usecase with single Swagger UI per page
        - `deepLinking: true`, so if for some reason you don't want to use deep links, disable them explicitly
        - `defaultModelsExpandDepth: 0` to collapse models

        You can override them in this configuration object

!!! example
    See [API Reference](/api/reference) page

!!! warning "Do not use `SwaggerUIBundle`"
    Always use custom `SwaggerUI` wrapper from the `swagger-ui.html` template as it is compartible with [instant loading :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#instant-loading){:target="_blank"} and initializes `SwaggerUIBundle` internally when possible

!!! tip "Multiple Swagger UI on a single page"
    By default, there is only one Swagger UI below optional markdown content per page. If you need more, add new `div` inside your markdown content manually, specifying its `id` and passing this `id` as `dom_id` to the `SwaggerUI`
