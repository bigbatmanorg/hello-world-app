# Hello World App

Docs: https://bigbatmanorg.github.io/hello-world-app

Simple cross-platform Hello World CLI. GitHub Actions builds a Python wheel plus PyInstaller executables for Linux and Windows and publishes MkDocs documentation to GitHub Pages.

## Quick start (with uv)

Prerequisite: install `uv` from https://docs.astral.sh/uv/getting-started/ and ensure it is on your `PATH`.

```bash
# create & sync env from uv.lock / pyproject
uv venv
uv sync --all-extras --dev

# run tests
uv run pytest

# run CLI
uv run hello-world-app
uv run hello-world-app Ada
```

## What GitHub Actions does
- CI builds and tests on Linux and Windows.
- Linux job also produces the Python wheel (`dist/`) for package distribution.
- Linux and Windows jobs build PyInstaller one-file executables and upload them as workflow artifacts.
- Documentation is built with MkDocs and published to GitHub Pages on every push to `main`.

## GitHub Pages deploy requirements
- In the repository, open **Settings → Pages → Build and deployment** and pick **GitHub Actions** so the Pages site exists before the workflow runs.
- In **Settings → Actions → General → Workflow permissions**, give `GITHUB_TOKEN` **Read and write** access (and allow Pages deployments if the org setting appears); otherwise `actions/configure-pages@v5` will fail with "Resource not accessible by integration".
- After those two toggles, rerun the `Docs` workflow; the existing `.github/workflows/docs.yml` will build with MkDocs and deploy successfully.

## Local builds

```bash
uv build                                              # build sdist + wheel
uv run pyinstaller --onefile src/hello_world_app/__main__.py -n hello-world-app
uv run mkdocs serve                                   # live docs server
uv run mkdocs build                                   # static site
```

## Releasing
- Download artifacts from the GitHub Action run or publish the wheel to PyPI manually (not automated here).
- Tag a release in GitHub to keep artifacts organized.

## Repo bootstrap summary
A detailed walkthrough for recreating this pattern in new repositories is in `docs/setup-guide.md`.
to be added later 
