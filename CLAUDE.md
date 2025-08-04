# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the official documentation repository for Aiuta Virtual Try-On Solutions, built using MkDocs Material. The documentation covers:
- SDKs for Android, iOS, Flutter, and Web platforms
- REST APIs for Try-On and Studio services
- Shopify App integration
- Developer configuration guides and resources

## Architecture

### Documentation Structure
- `/docs/` - Main documentation content organized by product/platform
- `/mkdocs.yml` - MkDocs configuration with navigation, themes, and plugins
- `/macros/` - Python macros for dynamic content generation (API calls, GitHub integration)
- `/overrides/` - Custom HTML templates and Swagger UI integration
- `/.github/workflows/` - GitHub Actions for automated deployment

### Key Components
- **MkDocs Material**: Documentation framework with navigation tabs, search, and theming
- **Python Macros**: Dynamic content loading from APIs and GitHub repositories
- **Swagger UI Integration**: Interactive API documentation for Try-On and Studio APIs
- **Multi-platform SDK Documentation**: Covers Android, iOS, Flutter, and Web SDKs

### Macro System
The `macros/` directory contains Python modules that provide dynamic content:
- `aiuta.py` - Loads live product data from Aiuta API for examples
- `github.py` - Fetches repository information and releases
- `generator.py` - Generates code snippets and configuration examples

## Development Commands

### Local Development
```bash
# Install MkDocs and required plugins
pip install mkdocs-material mkdocs-minify-plugin mkdocs-include-markdown-plugin mkdocs-exclude-search mkdocs-macros-plugin mkdocs-redirects requests

# Serve documentation locally with live reload
mkdocs serve

# Build static documentation
mkdocs build
```

### Deployment
The documentation is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `main` branch. The workflow:
1. Installs Python dependencies
2. Runs `mkdocs gh-deploy --force`

## Content Guidelines

### File Organization
- API documentation uses OpenAPI specs in JSON format
- SDK documentation follows platform-specific structure
- Templates in `/docs/sdk/templates/` and `/docs/api/templates/` provide reusable content
- Media assets in `/docs/media/` organized by product/component

### Navigation Structure
The site uses tabbed navigation defined in `mkdocs.yml`:
- **About**: Landing page and product overview
- **API**: REST API documentation for Try-On and Studio
- **SDK**: Platform-specific SDK documentation
- **Developer**: Configuration and customization guides
- **Shopify**: Shopify App documentation
- **Insights**: Internal team documentation

### Dynamic Content
Many pages use macro syntax like `{{ macro_name() }}` to include:
- Live API examples with real product data
- Latest SDK version numbers from GitHub releases  
- Code snippets generated from templates
- Repository links and documentation URLs

## Important Notes

- The site uses strict validation - all links and navigation must be valid
- OpenAPI specs are integrated via custom Swagger UI templates
- The macro system requires API keys for live data (uses AIUTADEMO key for examples)
- All SDK documentation references actual GitHub repositories for version information
- Media files should be optimized and follow the existing directory structure