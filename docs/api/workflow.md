# Workflow

## 1. Upload an image or use predefined model

=== "Upload an image"
    Upload an image which you want to use as in input for generation. It may be some model whom you want to dress in specific clothes item.
    You will receive an object with image id and url as a result. Use image id on the next step to specify input image for generation.
    
    <div class="grid" markdown>
    [Try uploading an image](/api/reference/#/default/upload_user_image_uploaded_images_post){ .card }
    </div>


=== "Use predefined model"
    Alternatively, you can use predefined models. Use the [list of predefined models](/api/reference/#/default/get_predefined_try_on_models_predefined_try_on_models_get) API endpoint to retrieve the available models. Each predefined model’s image has an ID that should be used during the generation step.

## 2. Create a generation operation request
Provide input image id received on the previous step as well as SKU identifiers: `sku_id` and `sku_catalog_name` (catalog name is optional, `"main"` is used by default).
You will receive an object with id of created image generation operation in case of successful request or an error message otherwise.

<div class="grid cards" markdown>
- [Try creating a generation operation request](/api/reference/#/default/generate_sku_images_operations_sku_images_operations_post)
</div>

## 3. Get the operation results
Use an operation id from the previous step to retrieve the operation status. Operation became completed once operation status turns to `SUCCESS` or `FAILED`.
In case of successfully completed operation you will receive generated image(s) URL(s) in resulting object. If an error occurred you can check error message in error field.

<div class="grid cards" markdown>
- [Try getting the operation results](/api/reference/#/default/get_generate_sku_images_operation_sku_images_operations__operation_id__get)
</div>
