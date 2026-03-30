.PHONY: build up test lint clean

build:
    docker build -t {{cookiecutter.project_slug}} .

up:
    docker run --rm {{cookiecutter.project_slug}}

test:
    uv run pytest

lint:
    uv run ruff check . --fix
    uv run ruff format .

clean:
    rm -rf .venv .pytest_cache .ruff_cache
    find . -name "__pycache__" -exec rm -rf {} +
