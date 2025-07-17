import os
import requests
import json

from .github import get_latest_release

# Constants

DUMMY_PRODUCT = {
    "sku_id": "<product_id>",
    "title": "<product_title>",
    "image_urls": [
        "<image_url_1>",
        "<image_url_2>",
        "<image_url_3>"
    ]
}

# Caches

_release_cache = {}
_product_cache = None
_product_count = 1

# Functions

def load_product_cache(api_key, api_url):
    global _product_cache, _product_count
    
    try:
        url = f'{api_url}/sku_catalogs?limit=1'
        headers = {
            "Accept": "application/json",
            "x-api-Key": api_key
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        catalog_data = response.json()
        
        catalog_result = catalog_data.get('result', [])
        if not catalog_result:
            return
        
        catalog_name = catalog_result[0].get('sku_catalog_name')
        if not catalog_name:
            return
        
        url = f'{api_url}/sku_items/{catalog_name}?limit=7'
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        items_data = response.json()
        items_result = items_data.get('result', [])

        _product_cache = items_result
        _product_count = len(items_result)
        
    except Exception:
        return

def get_test_product(index, api_key, api_url):
    global _product_cache
    
    if _product_cache is None:
        load_product_cache(api_key, api_url)

    try:
        return _product_cache[index]
    except Exception:
        return DUMMY_PRODUCT

# Macros for the docs
def define_env(env):
    yml = env.conf
    extra = yml.extra

    github = extra['github']
    github_team = github['team']
    github_url = github['url']
    github_api_url = github['api']
    github_pages_url = github['pages']
    
    pub_dev = extra['pub_dev']
    pub_dev_url = pub_dev['url']
    pub_dev_package = pub_dev['package']
    
    aiuta = extra['aiuta']
    aiuta_api_url = aiuta['api']
    aiuta_api_key = aiuta['api_key']
    try_on_path = extra['try_on']

    # Returns SDK repo url
    @env.macro
    def repo(sdk, git_suffix=False):
        return github_url.format(team=github_team, repo=sdk) + ('.git' if git_suffix else '')

    # Returns the latest release version for the SDK repo
    @env.macro
    def latest(sdk):
        return get_latest_release(github_api_url.format(team=github_team, repo=sdk), sdk)

    # Returns the github pages url for the SDK repo 
    @env.macro
    def pages(sdk):
        return github_pages_url.format(team=github_team, repo=sdk)

    # Returns the pub dev url for the flutter package
    @env.macro
    def pub_package(path=''):
        return f"{pub_dev_url.format(package=pub_dev_package)}/{path}"

    # Returns the api url for the given path
    @env.macro
    def api(path):
        return aiuta_api_url.format(path=path)

    # Returns the test product for the given index
    @env.macro
    def test_product(index):
        return get_test_product(index, aiuta_api_key, api(try_on_path))

    # Generates the test products for the given template path
    @env.macro
    def gen_test_products(template_path, url_indent=2, images_width=100):
        INDENT = " " * 4 # Proper indent for tabs ===
        URL_INDENT = " " * url_indent
        
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
        
        # Generate code for all available products
        for index in range(_product_count):
            product = test_product(index)
            
            # Format image_urls as a proper array string for the target language
            image_urls = product['image_urls']
            if isinstance(image_urls, list):
                if language == 'kotlin':
                    url_list = f',\n{INDENT}{URL_INDENT}'.join(f'"{url}"' for url in image_urls)
                    formatted_urls = f"""listOf(
{INDENT}{URL_INDENT}{url_list}
{URL_INDENT})"""
                else:
                    url_list = f',\n{INDENT}{URL_INDENT}'.join(f'"{url}"' for url in image_urls)
                    formatted_urls = f"""[
{INDENT}{URL_INDENT}{url_list}
{INDENT}]"""
            else:
                formatted_urls = str(image_urls)
                
            # Use manual replacement to avoid conflicts with curly braces in code
            code = template.replace('{api_key}', aiuta_api_key)
            code = code.replace('{sku_id}', product['sku_id'])
            code = code.replace('{title}', product['title'])
            code = code.replace('{image_urls}', formatted_urls)

            # Indent each line of code with 4 spaces
            indented_code = '\n'.join(INDENT + line for line in code.split('\n'))
            
            # Generate markdown images
            if isinstance(image_urls, list):
                markdown_images = '\n'.join(f'{INDENT}![img]({url}){{ width=100 }}' for url in product['image_urls'])
            else:
                markdown_images = f'{INDENT}![img]({product["image_urls"]}){{ width=100 }}'
            
            result = f"""=== "Product {index + 1}"

{INDENT}```{language}
{indented_code}
{INDENT}```

{markdown_images}"""
            results.append(result)
        
        return '\n\n'.join(results)

    # Load the product cache
    load_product_cache(aiuta_api_key, api(try_on_path))
