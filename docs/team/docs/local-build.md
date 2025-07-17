To build and preview the documentation locally, you'll need to install [Material for MKDocs :octicons-link-external-24:](https://squidfunk.github.io/mkdocs-material/getting-started/){:target="_blank"} along with the required plugins:

```sh
pip install \
  mkdocs-material \
  mkdocs-minify-plugin \
  mkdocs-include-markdown-plugin \
  mkdocs-exclude-search \
  mkdocs-macros-plugin \
  requests
```

Once everything is installed, navigate to the root of your `docs` repository clone and run

```sh
mkdocs serve
```

!!! danger "Strict mode"
    MKDocs configuration has `strict` parameter set to `true`. This will cause MkDocs to abort the build on any warnings.
    If you need to __temporarily__ bypass this, run `mkdocs serve --no-strict`

You should see output like

```
INFO    -  [10:46:26] Serving on http://127.0.0.1:8000/
```

Open that URL in your browser to view the documentation.

??? warning "API rate limit exceeded"
    If you see `<version>` instead of actual SDK version numbers, the GitHub API may have rejected request due to rate limiting.
    
    To fix this, generate a **GitHub Personal Access Token** and authorize your requests:

    1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens).
    2. Click **"Generate new token (classic)"**.
    3. Fill in the following:
    - **Note**: `Docs GitHub API Access`
    - **Scopes**:
        - ✅ `public_repo` if you're accessing only public repositories, **or**
        - ✅ `repo` if you're accessing private ones
    4. Copy the generated token `ghp_...` — it will be shown **only once**.

    Then, in your terminal:

    ```sh
    export GITHUB_TOKEN=ghp_your_token_here
    mkdocs serve
    ```

    This will authorize your GitHub API requests and avoid the default 60-requests-per-hour limit.