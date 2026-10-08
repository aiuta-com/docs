import json
import os
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

# A fixed snapshot of the demo products, so the build does not depend on the live API
_DEMO_PRODUCTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'demo_products.json')

_product_cache = None
_api_url = None
_api_key = None

def init(extra):
    global _api_url, _api_key

    aiuta = extra['aiuta']
    _api_url = aiuta['api']
    _api_key = aiuta['demo']['api_key']

def get_api_url(path):
    return _api_url.format(path=path)

def get_api_key():
    return _api_key

def _load_product_cache():
    global _product_cache

    with open(_DEMO_PRODUCTS_PATH) as products_file:
        _product_cache = json.load(products_file)

    logger.log(f"Loaded {len(_product_cache)} demo products")

def get_test_product(index):
    try:
        return get_test_products()[index]
    except IndexError:
        return _DUMMY_PRODUCT


def get_test_products():
    if _product_cache is None:
        _load_product_cache()

    return _product_cache
