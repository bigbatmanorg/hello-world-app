from hello_world_app import greet


def test_greet_defaults_to_world():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"
