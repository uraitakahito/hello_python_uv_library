from hello_python_uv_library import greetings


def test_hello():
    assert greetings.hello() == "Hello, Python UV Library!"
