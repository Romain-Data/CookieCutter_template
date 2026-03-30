from {{cookiecutter.project_slug}}.main import hello

def test_hello():
    """Vérifie que la fonction hello fonctionne."""
    assert hello() == "Hello from {{cookiecutter.project_name}}!"
