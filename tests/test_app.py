from app import main

def test_app():
    assert main.hello_world() == "Hello World"
