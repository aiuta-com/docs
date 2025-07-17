_url = None
_package = None

def init(extra):
    global _url, _package
    pub_dev = extra['pub_dev']
    _url = pub_dev['url']
    _package = pub_dev['package']

def get_url(path=None):
    return _url.format(package=_package) + (f'/{path}' if path else '')
