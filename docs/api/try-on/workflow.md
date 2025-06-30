# Workflow

??? example "Sequence Diagram"
    ``` mermaid
    sequenceDiagram
        autonumber

        participant BE as Your<br>Backend
        participant API as Aiuta<br>API

        alt
            BE->>API: Upload an image (bytes)
            API-->>BE: Return AiutaImage (id, url)
        else
            BE->>API: Get predefined models
            API-->>BE: Return categories list<br>of AiutaImage (id, url)
        end

        BE->>API: Generate operation (uploaded_image_id, sku_id)
        API-->>BE: Return Response (operation_id)

        loop
            BE->>API: Get operation (operation_id)
            API-->>BE: Return Operation object
            BE->>BE: Check status<br>operation field

            critical status
                option SUCCESS
                    Note right of BE: generated_images field<br>with url in resulting object
                option FAILED
                    rect
                        Note right of BE: error field<br>contains error message
                    end
            end
        end
    ```

## 1. Upload an image or use predefined model

=== "Upload an image"
    Upload an image which you want to use as in input for generation. It may be some model whom you want to dress in specific clothes item.
    You will receive an object with image `id` and `url` as a result. Use image `id` on the next step to specify the `uploaded_image_id` for generation.
    
    <div class="grid" markdown>
    [Try uploading an image](/api/try-on/reference/#/default/upload_user_image_uploaded_images_post){ .card }
    </div>


=== "Use predefined model"
    Use the [list of predefined models](/api/try-on/reference/#/default/get_predefined_try_on_models_predefined_try_on_models_get) API endpoint to retrieve the available models. Each predefined model’s image has an `id`, which is used in the next step to specify the `uploaded_image_id` for generation.

## 2. Create a generation operation request
Provide `uploaded_image_id` received on the previous step as well as SKU identifiers: `sku_id` and optional `sku_catalog_name` (`"main"` by default).
You will receive an object with `operation_id` of created image generation operation in case of successful request or an error message otherwise.

<div class="grid cards" markdown>
- [Try creating a generation operation request](/api/try-on/reference/#/default/generate_sku_images_operations_sku_images_operations_post)
</div>

## 3. Get the operation results
Use an `operation_id` from the previous step to retrieve the operation status. Operation became completed once operation status turns to `SUCCESS` or `FAILED`.
In case of successfully completed operation you will receive `generated_images` with `url` in resulting object. If an error occurred you can check error message in the `error` field.

<div class="grid cards" markdown>
- [Try getting the operation results](/api/try-on/reference/#/default/get_generate_sku_images_operation_sku_images_operations__operation_id__get)
</div>
