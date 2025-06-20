# Workflow

## 1. Upload input images

Upload images of your product for which you want to generate a Flat Lay.
For each uploaded image, you will receive an object containing the image ID and URL. Use these IDs in the next step to specify input images for Flat Lay generation.

<div class="grid cards" markdown>
- [Try uploading an image](/api/flat-lays/reference/#/default/upload_user_image_uploaded_images_post)
</div>

## 2. Create a generation operation request
Provide the image IDs received in the previous step, along with some basic product information: `product_category`, `product_title`, and `product_description`.
You will receive an object containing the ID of the created Flat Lay generation operation if the request is successful, or an error message otherwise.

<div class="grid cards" markdown>
- [Try creating a generation operation request](/api/flat-lays/reference/#/default/create_flat_lay_operation_flat_lay_operations_post)
</div>

## 3. Get the operation results
Use the operation ID from the previous step to retrieve the status of the operation. The operation is considered complete when its status becomes `SUCCESS` or `FAILED`.
If the operation completes successfully, the response will contain the generated image URL(s). If an error occurred, the error field will contain details.

<div class="grid cards" markdown>
- [Try getting the operation results](/api/flat-lays/reference/#/default/get_flat_lay_operation_flat_lay_operations__operation_id__get)
</div>
