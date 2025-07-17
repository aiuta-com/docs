import os
import requests
import json

DUMMY_VERSION = '<version>'

_release_cache = {}

def get_latest_release(api_url, repo_name):
    global _release_cache
    
    if repo_name in _release_cache:
        return _release_cache[repo_name]
    
    token = os.environ.get("GITHUB_TOKEN")
    url = f'{api_url}/releases/latest'
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
