# Setup Guide

Use this checklist to recreate the same repo pattern elsewhere.

## Prerequisites
- Python 3.9+ available (uv will manage the venv for you).
- `uv` installed (https://docs.astral.sh/uv/getting-started/) and on your `PATH`.
- Git configured with your name/email and authenticated to GitHub (SSH keys or HTTPS with a Personal Access Token that has `repo` and `workflow` scopes).
- Optional: GitHub CLI (`gh`) logged in, which simplifies repo creation and Pages setup.
- Optional: PyPI account + API token if you want to publish the wheel to PyPI.

## Steps to bootstrap a new repo
1. **Create project layout**
   - `uv venv` (creates `.venv`) then `source .venv/bin/activate` (or use `uv run` without activation).
   - `uv sync --all-extras --dev` once you copy the `pyproject.toml`/`src`/`tests` structure from this repo.
2. **Author package code**
   - Put code in `src/<package_name>/` and expose a CLI via `[project.scripts]` in `pyproject.toml`.
   - Keep tests in `tests/` and configure pytest in `pyproject.toml`.
3. **Docs**
   - Add `mkdocs.yml` and `docs/` content. Update `site_url` and `repo_url` to match the new repo.
4. **GitHub Actions (uv-based)**
   - Copy `.github/workflows/build.yml` for CI + build artifacts. It installs uv, syncs deps from `uv.lock`, runs tests, builds wheels, and bundles PyInstaller executables.
   - Copy `.github/workflows/docs.yml` for MkDocs + GitHub Pages deploy. It installs uv, syncs deps, builds the docs, and deploys via GitHub Pages.
   - Adjust `matrix` Python/OS versions if needed, and update artifact names.
5. **Initialize git & push**
   - `git init -b main` (or `master` if you prefer), `git add .`, `git commit -m "Initial commit"`.
   - Create a GitHub repo (via UI or `gh repo create <owner>/<name> --public`).
   - `git remote add origin git@github.com:<owner>/<name>.git` (or HTTPS) and `git push -u origin main`.
6. **Enable Pages**
   - In GitHub repo settings > Pages, pick source "GitHub Actions".
   - First push will let the `docs.yml` workflow publish to `gh-pages` and attach the Pages site to the `github-pages` environment automatically.

## How the automation works
- **build.yml** runs on each push. It installs dev deps, runs tests, builds a wheel on Linux, and produces PyInstaller one-file executables on Linux and Windows. Artifacts are uploaded to the workflow run.
- **docs.yml** builds the MkDocs site, uploads it as a Pages artifact, and deploys to GitHub Pages with `actions/deploy-pages`.

Following this guide gives you a reproducible, multi-platform distribution pipeline for small Python CLIs.

## Deployment command sequence (example)
Run these from the repo root to build, test, and push:

```bash
cd /home/adam/projects/githubTESTrepo
uv venv
uv sync --all-extras --dev

uv run pytest
uv run hello-world-app
uv run hello-world-app Ada
uv build
uv run pyinstaller --onefile src/hello_world_app/cli.py -n hello-world-app
uv run mkdocs build --strict    # mkdocs serve is available for local preview

git config user.name "bigbatmanorg"
git config user.email "moravcik.adam@gmail.com"
git remote set-url origin https://github.com/bigbatmanorg/hello-world-app.git
git push -u origin main
```
