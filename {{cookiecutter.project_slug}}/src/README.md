# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## 🚀 Installation rapide

1. Assurez-vous d'avoir [uv](https://github.com/astral-sh/uv) installé.
2. Initialisez le projet :

```bash
uv sync
```

## 🛠 Commandes utiles

{% if cookiecutter.use_docker == 'y' -%}
Utilisez le **Makefile** pour les tâches courantes :
* `make test` : Lancer les tests avec pytest.
* `make lint` : Vérifier et formater le code avec Ruff.
* `make run` : Exécuter l'application.
{%- else -%}
Utilisez **uv** directement :
* Lancer les tests : `uv run pytest`
* Vérifier le code : `uv run ruff check .`
* Exécuter l'application : `uv run python src/{{cookiecutter.project_slug}}/main.py`
{%- endif %}

{% if cookiecutter.use_docker == 'y' -%}
## 🐳 Docker

```bash
# Construire l'image
docker build -t {{cookiecutter.project_slug}} .

# Lancer le container
docker run {{cookiecutter.project_slug}}
```
{%- endif %}

