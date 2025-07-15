import os
import requests
import json

# Constants

DUMMY_VERSION = '<version>'
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

# Functions

def get_test_product(index, api_key, api_url):
    global _product_cache
    
    if _product_cache is not None:
        try:
            return _product_cache[index]
        except Exception:
            return DUMMY_PRODUCT
    
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
            return DUMMY_PRODUCT
        
        catalog_name = catalog_result[0].get('sku_catalog_name')
        if not catalog_name:
            return DUMMY_PRODUCT
        
        url = f'{api_url}/sku_items/{catalog_name}'
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        items_data = response.json()
        items_result = items_data.get('result', [])

        _product_cache = items_result
        
        try:
            return items_result[index]
        except (IndexError, TypeError):
            return DUMMY_PRODUCT
        
    except Exception:
        return DUMMY_PRODUCT

def get_latest_release(repo_name, api_url):
    global _release_cache
    
    if repo_name in _release_cache:
        return _release_cache[repo_name]
    
    token = os.environ.get("GITHUB_TOKEN")
    url = f'{api_url}/{repo_name}/releases/latest'
    headers = {
        "Accept": "application/json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers)
    if response.ok:
        version = response.json().get('tag_name', DUMMY_VERSION)
    else:
        version = DUMMY_VERSION
    
    _release_cache[repo_name] = version
    return version

# Macros for the docs
def define_env(env):
    yml = env.conf
    extra = yml.extra
    aiuta = extra['aiuta']
    
    api = aiuta['api']
    api_key = api['demo_key']
    api_url = api['base_url']

    paths = api['path']
    path_try_on = paths['try_on']
    path_flat_lays = paths['flat_lays']
    path_analytics = paths['analytics']

    github = aiuta['github']
    github_team = github['team']
    github_url = f"{github['url']}/{github_team}"
    github_api_url = f"{github['api']}/{github_team}"
    
    repos = github['repos']
    repo_name_flutter = repos['flutter']
    repo_name_ios = repos['ios']
    repo_name_android = repos['android']
    repo_name_web = repos['web']

    # Returns the flutter repo url
    @env.macro
    def repo_flutter():
        return f"{github_url}/{repo_name_flutter}.git"

    # Returns the ios repo url
    @env.macro
    def repo_ios():
        return f"{github_url}/{repo_name_ios}.git"

    # Returns the android repo url
    @env.macro
    def repo_android():
        return f"{github_url}/{repo_name_android}.git"

    # Returns the web repo url
    @env.macro
    def repo_web():
        return f"{github_url}/{repo_name_web}.git"

    # Returns the latest release version for the flutter repo
    @env.macro
    def latest_flutter():
        return get_latest_release(repo_name_flutter, github_api_url)

    # Returns the latest release version for the ios repo
    @env.macro
    def latest_ios():
        return get_latest_release(repo_name_ios, github_api_url)

    # Returns the latest release version for the android repo
    @env.macro
    def latest_android():
        return get_latest_release(repo_name_android, github_api_url)

    # Returns the latest release version for the web repo
    @env.macro
    def latest_web():
        return get_latest_release(repo_name_web, github_api_url)

    # Returns the try on api url
    @env.macro
    def api_try_on():
        return f"{api_url}/{path_try_on}"

    # Returns the flat lays api url
    @env.macro
    def api_flat_lays():
        return f"{api_url}/{path_flat_lays}"

    # Returns the analytics api url
    @env.macro
    def api_analytics():
        return f"{api_url}/{path_analytics}"

    # Returns the test product for the given index
    @env.macro
    def test_product(index):
        return get_test_product(index, api_key, api_try_on())

    # Returns the JSON string for the given object
    @env.macro
    def dumps(obj):
        return json.dumps(obj, indent=2)

    # Returns the listOf() string for the given list for Kotlin
    @env.macro
    def list_of(arr):
        json_str = dumps(arr).strip()
        if json_str.startswith('[') and json_str.endswith(']'):
            json_str = 'listOf(' + json_str[1:-1] + ')'
        return json_str

    # Returns the markdown images for the given urls
    @env.macro
    def md_images(urls, width=100):
        return '\n'.join(f'![img]({url}){{ width={width} }}' for url in urls)
