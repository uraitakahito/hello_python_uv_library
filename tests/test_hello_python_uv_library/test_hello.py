from hello_python_uv_library import greetings


def test_hello():
    assert greetings.hello() == "Hello, Python UV Library!"


def test_hello_add():
    assert greetings.hello_add(1, 2) == 3
