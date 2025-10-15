import os
import logger

_INDENT = " " * 4 # Proper indent for tabs ===

def gen_test_products(template_path, products, api_key, limit=7, url_indent=2, images_width=100):
    logger.log(f"Generating up to {limit} of {len(products)} test products with {template_path}")

    url_indent = " " * url_indent
    
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    full_template_path = os.path.join(docs_dir, template_path)
    with open(full_template_path, 'r') as file:
        template = file.read()
    
    # Determine the language for syntax highlighting based on file extension
    if template_path.endswith('.swift'):
        language = 'swift'
    elif template_path.endswith('.kt') or template_path.endswith('.kts'):
        language = 'kotlin'
    elif template_path.endswith('.dart'):
        language = 'dart'
    elif template_path.endswith('.js') or template_path.endswith('.ts'):
        language = 'javascript'
    else:
        language = ''
    
    results = []
    counter = 0
    
    # Generate code for all available products
    for product in products:
        counter += 1

        if counter > limit:
            break

        # Format image_urls as a proper array string for the target language
        image_urls = product['image_urls']
        if isinstance(image_urls, list):
            if language == 'kotlin':
                url_list = f',\n{_INDENT}{url_indent}'.join(f'"{url}"' for url in image_urls)
                formatted_urls = f"""listOf(
{_INDENT}{url_indent}{url_list}
{url_indent})"""
            else:
                url_list = f',\n{_INDENT}{url_indent}'.join(f'"{url}"' for url in image_urls)
                formatted_urls = f"""[
{_INDENT}{url_indent}{url_list}
{_INDENT}]"""
        else:
            formatted_urls = str(image_urls)
            
        # Use manual replacement to avoid conflicts with curly braces in code
        code = template.replace('{api_key}', api_key)
        code = code.replace('{sku_id}', product['sku_id'])
        code = code.replace('{title}', product['title'])
        code = code.replace('{image_urls}', formatted_urls)

        # Indent each line of code with 4 spaces
        indented_code = '\n'.join(_INDENT + line for line in code.split('\n'))
        
        # Generate markdown images
        if isinstance(image_urls, list):
            markdown_images = '\n'.join(f'{_INDENT}![img]({url}){{ width=100 }}' for url in product['image_urls'])
        else:
            markdown_images = f'{_INDENT}![img]({product["image_urls"]}){{ width=100 }}'
        
        result = f"""=== "Product {counter}"

{_INDENT}```{language}
{indented_code}
{_INDENT}```

{markdown_images}"""
        results.append(result)
    
    return '\n\n'.join(results)


def gen_web_catalog(products, api_key):
    logger.log(f"Generating web demo catalog with {len(products)} products")
    
    results = []
    counter = 0
    
    for product in products:
        counter += 1
        
        result = f"""-   ![Product]({product['image_urls'][0]}){{ width=100 }}

{_INDENT}<button class="md-button" onclick="startTryOn('{product['sku_id']}')">Try on</button>

{_INDENT}{product['title']}"""
        results.append(result)
    
    return '\n\n'.join(results)

def gen_web_pages(products, api_key, limit, images_width=100):
    logger.log(f"Generating up to {limit} web pages of {len(products)} products")

    results = []
    counter = 0

    for product in products:
        counter += 1

        if counter > limit:
            break

        image_urls = product['image_urls']
        if isinstance(image_urls, list):
            markdown_images = '\n'.join(f'{_INDENT}![img]({url}){{ width={images_width} }}' for url in product['image_urls'])
        else:
            markdown_images = f'{_INDENT}![img]({product["image_urls"]}){{ width={images_width} }}'

        result = f"""=== "Product {counter}"

{_INDENT}__{product['category_google_name']}__

{markdown_images}

{_INDENT}<h2> {product['title']}</h2>

{_INDENT}{product['description']}

{_INDENT}<button class="md-button" onclick="startTryOn('{product['sku_id']}')">Try on :aiuta-favicon:</button>        
"""
        results.append(result)

    return '\n\n'.join(results)
