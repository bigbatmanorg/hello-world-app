"""Command-line interface for hello_world_app."""

from __future__ import annotations

import argparse
from pathlib import Path

from hello_world_app import greet


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple Hello World CLI")
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World)",
    )
    args = parser.parse_args()

    message = greet(args.name)
    print(message)

    # Write a small file to show PyInstaller bundled binary works end-to-end
    output_path = Path.cwd() / "hello_output.txt"
    output_path.write_text(message, encoding="utf-8")


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()


# and programs ends 
