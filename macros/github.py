import os
import requests
import logger

_DUMMY_VERSION = '<version>'
_release_cache = {}
_api_url = None
_team = None
_url = None
_pages_url = None

def init(extra):
    global _api_url, _team, _url, _pages_url
    github = extra['github']
    _api_url = github['api']
    _team = github['team']
    _url = github['url']
    _pages_url = github['pages']

def get_url(repo_name, path=None, git_suffix=False):
    if path:
        git_suffix = False
    return _url.format(team=_team, repo=repo_name) + (f'/{path}' if path else '') + ('.git' if git_suffix else '')

def get_pages_url(repo_name):
    return _pages_url.format(team=_team, repo=repo_name)

def get_api_url(repo_name):
    return _api_url.format(team=_team, repo=repo_name)

def get_latest_release(repo_name):
    global _release_cache
    
    if repo_name in _release_cache:
        return _release_cache[repo_name]
    
    logger.log(f"Getting latest release for {repo_name}")
    url = f'{get_api_url(repo_name)}/releases/latest'
    headers = {
        "Accept": "application/json"
    }

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
        logger.log(f"Using GITHUB_TOKEN={token[:8]}...")

    response = requests.get(url, headers=headers)
    if response.ok:
        version = response.json().get('tag_name', _DUMMY_VERSION)
        logger.log(f"Got {version}")
    else:
        version = _DUMMY_VERSION
        logger.log(f"Failed to get version")
    
    _release_cache[repo_name] = version
    return version
