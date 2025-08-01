import os
import requests
import github
import aiuta
import generator
import pub_dev
import json

def define_env(env):
    yml = env.conf
    extra = yml.extra
    aiuta.init(extra)
    github.init(extra)
    pub_dev.init(extra)

    # Returns the SDK repo url
    @env.macro
    def repo(sdk, path=None, git_suffix=False):
        return github.get_url(sdk, path, git_suffix)

    # Returns the latest release version for the SDK
    @env.macro
    def latest(sdk):
        return github.get_latest_release(sdk)

    # Returns the github pages url for the SDK 
    @env.macro
    def pages(sdk):
        return github.get_pages_url(sdk)

    # Returns the pub dev url for the flutter package
    @env.macro
    def pub_package(path=None):
        return pub_dev.get_url(path)

    # Returns the API url for the given path
    @env.macro
    def api(path):
        return aiuta.get_api_url(path)

    # Generates test products for the given code template path
    @env.macro
    def gen_test_products(template_path, url_indent=2, images_width=100):
        return generator.gen_test_products(template_path, aiuta.get_test_products(), aiuta.get_api_key(), url_indent, images_width)

    # Returns the test products
    @env.macro
    def test_products():
        return aiuta.get_test_products()

    # Dumps the given value as a pretty JSON string
    @env.filter
    def dumps(value):
        return json.dumps(value, indent=2)
