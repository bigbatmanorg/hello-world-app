"""Hello World application package."""

__all__ = ["greet"]


def greet(name: str = "World") -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"
