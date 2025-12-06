# Usage

## Install locally (with uv)

```bash
uv venv
uv sync --all-extras --dev
```

## Run the CLI

```bash
uv run hello-world-app            # prints "Hello, World!"
uv run hello-world-app Ada        # prints "Hello, Ada!"
```

An output file `hello_output.txt` is written to the current directory to verify bundled binaries work end-to-end.

## Development

```bash
uv run pytest                                              # run tests
uv build                                                   # build wheel + sdist
uv run pyinstaller --onefile src/hello_world_app/cli.py -n hello-world-app
uv run mkdocs serve                                        # live docs server
```
