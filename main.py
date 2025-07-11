import os
import requests
import json

API_KEY = "AIUTADEMO" # This is not a secret

# Cache for storing loaded products
_product_cache = None

# Dummy product for error cases
DUMMY_PRODUCT = {
    "sku_id": "<product_id>",
    "title": "<product_title>",
    "image_urls": [
        "<image_url_1>",
        "<image_url_2>",
        "<image_url_3>"
    ]
}

def get_test_product(index):
    global _product_cache
    
    # Return cached result if available
    if _product_cache is not None:
        try:
            return _product_cache[index]
        except Exception:
            return DUMMY_PRODUCT
    
    try:
        print(f"!!!! Loading products from API")

        # Get catalog with error handling
        url = f'https://api.aiuta.com/sku_catalogs?limit=1'
        headers = {
            "Accept": "application/json",
            "x-api-Key": API_KEY
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        catalog_data = response.json()
        
        # Safely extract catalog name
        catalog_result = catalog_data.get('result', [])
        if not catalog_result:
            return DUMMY_PRODUCT
        
        catalog_name = catalog_result[0].get('sku_catalog_name')
        if not catalog_name:
            return DUMMY_PRODUCT
        
        # Get SKU items with error handling
        url = f'https://api.aiuta.com/sku_items/{catalog_name}'
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        items_data = response.json()
        items_result = items_data.get('result', [])
        
        # Cache the results
        _product_cache = items_result
        
        # Return specific item by index
        try:
            return items_result[index]
        except (IndexError, TypeError):
            return DUMMY_PRODUCT
        
    except Exception:
        return DUMMY_PRODUCT

def get_latest_release(repo_name):
    token = os.environ.get("GITHUB_TOKEN")
    url = f'https://api.github.com/repos/aiuta-com/{repo_name}/releases/latest'
    headers = {
        "Accept": "application/json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json().get('tag_name', '<version>')
    return '<version>'

def define_env(env):
    @env.macro
    def latest_flutter():
        return get_latest_release('aiuta-flutter-sdk')

    @env.macro
    def latest_ios():
        return get_latest_release('aiuta-ios-sdk')

    @env.macro
    def latest_android():
        return get_latest_release('aiuta-android-sdk')

    @env.macro
    def test_product(index):
        return get_test_product(index)

    @env.macro
    def dumps(obj):
        return json.dumps(obj, indent=2)

    @env.macro
    def list_of(obj):
        json_str = dumps(obj).strip()
        # Replace the opening [ with listOf( and closing ] with )
        # Only replace the outermost brackets
        if json_str.startswith('[') and json_str.endswith(']'):
            json_str = 'listOf(' + json_str[1:-1] + ')'
        return json_str
