import os
import requests
import logger

_DUMMY_PRODUCT = {
    "sku_id": "<product_id>",
    "title": "<product_title>",
    "image_urls": [
        "<image_url_1>",
        "<image_url_2>",
        "<image_url_3>"
    ]
}

_product_load_count = 7
_product_cache = None
_product_count = 1
_api_url = None
_api_key = None
_try_on_path = None

def init(extra):
    global _api_url, _api_key, _try_on_path

    aiuta = extra['aiuta']
    _api_url = aiuta['api']
    _api_key = aiuta['api_key']
    _try_on_path = extra['try_on']

def get_api_url(path):
    return _api_url.format(path=path)

def get_api_key():
    return _api_key

def _load_product_cache():
    global _product_cache, _product_count
    
    try:
        logger.log(f"Loading product catalogs")
        url = f'{get_api_url(_try_on_path)}/sku_catalogs?limit=1'
        headers = {
            "Accept": "application/json",
            "x-api-Key": _api_key
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

        logger.log(f"Loading up to {_product_load_count} products from {catalog_name} catalog")
        
        url = f'{get_api_url(_try_on_path)}/sku_items/{catalog_name}?limit={_product_load_count}'
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        items_data = response.json()
        items_result = items_data.get('result', [])

        _product_cache = items_result
        _product_count = len(items_result)

        logger.log(f"Loaded {_product_count} products")
        
    except Exception:
        return

def get_test_product(index):
    global _product_cache
    
    if _product_cache is None:
        _load_product_cache()

    try:
        return _product_cache[index]
    except Exception:
        return _DUMMY_PRODUCT


def get_test_products():
    global _product_cache
    
    if _product_cache is None:
        _load_product_cache()

    try:
        return _product_cache
    except Exception:
        return [_DUMMY_PRODUCT]
