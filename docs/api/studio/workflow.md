# Studio Workflow

??? example "Sequence Diagram: Providing product images as URLs"
    ``` mermaid
    sequenceDiagram
        autonumber

        participant BE as Your<br>Backend
        participant API as Aiuta<br>API

        BE->>API: Generate operation (product info with product images' URLs, set of image types to generate)
        API-->>BE: Return Response (operation_id)

        loop
            BE->>API: Get operation (operation_id)
            API-->>BE: Return Operation object
            BE->>BE: Check status<br>operation field

            critical status
                option SUCCESS
                    Note right of BE: generation_result field<br> in resulting object
                option FAILED
                    rect
                        Note right of BE: error field<br>contains error message
                    end
            end
        end
    ```

??? example "Sequence Diagram: Manual images upload"
    ``` mermaid
    sequenceDiagram
        autonumber

        participant BE as Your<br>Backend
        participant API as Aiuta<br>API

        loop
            BE->>API: Upload an image (bytes)
            API-->>BE: Return Response (id, url)
        end

        BE->>API: Generate operation (uploaded_product_image_ids, product info, set of image types to generate)
        API-->>BE: Return Response (operation_id)

        loop
            BE->>API: Get operation (operation_id)
            API-->>BE: Return Operation object
            BE->>BE: Check status<br>operation field

            critical status
                option SUCCESS
                    Note right of BE: generation_result field<br> in resulting object
                option FAILED
                    rect
                        Note right of BE: error field<br>contains error message
                    end
            end
        end
    ```

??? example "Sequence Diagram: On-figure images creation with regeneration step"
    ``` mermaid
    sequenceDiagram
        autonumber

        participant BE as Your<br>Backend
        participant API as Aiuta<br>API

        BE->>API: Generate operation (product info with product images' URLs, initial set of images type to generate)
        API-->>BE: Return Response (initial_operation_id)

        loop
            BE->>API: Get operation (initial_operation_id)
            API-->>BE: Return Operation object
            BE->>BE: Check status<br>operation field

            critical status
                option SUCCESS
                    Note right of BE: generation_result field<br> in resulting object
                option FAILED
                    rect
                        Note right of BE: error field<br>contains error message
                    end
            end
        end

        BE->>API: Regenerate operation (initial_operation_id, new set of images types to generate/regenerate)
        API-->>BE: Return Response (regeneration_operation_id)

        loop
            BE->>API: Get regeneration operation (regeneration_operation_id)
            API-->>BE: Return Operation object
            BE->>BE: Check status<br>operation field

            critical status
                option SUCCESS
                    Note right of BE: generation_result field<br> in resulting object
                option FAILED
                    rect
                        Note right of BE: error field<br>contains error message
                    end
            end
        end
    ```


## 1. Upload input images (optional)

You can either upload product images or provide their URLs directly.
Use this step if you prefer to upload images first. These images will represent the product for which other types of product visuals will be generated.
For each uploaded image, you’ll receive an object containing its ID and URL. Use the image IDs in the next step to specify which product images to generate.

<div class="grid cards" markdown>
- [Try uploading an image](/api/studio/reference.md#/data/upload_user_image_uploaded_images_post)
</div>

## 2. Create a generation operation
Submit a request to generate product images using either uploaded image IDs or direct image URLs, along with optional product metadata (such as category, title, and description).
If the request is successful, you’ll receive an object containing an `operation_id`. This ID can be used to track progress and retrieve results.

<div class="grid cards" markdown>
- [Try creating a generation operation](/api/studio/reference.md#/flat_lay/create_flat_lay_operation_flat_lay_operations_post)
</div>

## 3. Get the operation results
Use the `operation_id` from the previous step to check the status of the operation. The operation is complete when its status becomes `SUCCESS` or `FAILED`.
If successful, the response will include generated image URLs. If an error occurs, the `error` field will contain details.

<div class="grid cards" markdown>
- [Try getting the operation results](/api/studio/reference.md#/flat_lay/get_flat_lay_operation_flat_lay_operations__operation_id__get)
</div>

## 4. Regenerate specific images (on-figure only, optional)
This step is available for on-figure image generation only. Submit a regeneration request using the `operation_id` from an existing generation operation to reuse all configuration and model settings.
Specify the list of image types you want to regenerate — including any new types not present in the original request — and optionally change the number of image variants to generate per type.

<div class="grid cards" markdown>
- [Try creating a regeneration operation](/api/studio/reference.md#/on_figure/create_on_figure_regenerate_operation_on_figure_operations_regenerate_post)
</div>