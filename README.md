# Python Project Template (uv + Docker + CI)

Un template [Cookiecutter](https://github.com/cookiecutter/cookiecutter) moderne pour projets Python, optimisé pour la performance et l'expérience développeur avec **uv**.

## Caractéristiques

- ⚡️ **Gestionnaire :** Utilisation de [uv](https://github.com/astral-sh/uv) pour une rapidité fulgurante (remplace pip, poetry, pyenv).
- 🛠 **Qualité de code :** Ruff (Linter & Formatter) configuré.
- ✅ **Tests :** Pytest avec structure `src/`.
- 🐳 **Docker (Optionnel) :** Dockerfile multi-stage optimisé.
- 🤖 **CI (Optionnel) :** Workflow GitHub Actions pré-configuré (Test & Lint).
- 📄 **Makefile (Optionnel) :** Raccourcis pour les tâches courantes.

## 🚀 Utilisation

### Pré-requis
Avoir [uv](https://github.com/astral-sh/uv) installé sur votre machine.

### Générer un projet
Pour créer un nouveau projet à partir de ce template, exécutez simplement :

```bash
uvx cookiecutter https://github.com/Romain-Data/CookieCutter_template
```

### Après la génération
Le template initialise automatiquement l'environnement. Il vous suffit d'entrer dans le dossier :

```bash
cd <votre-projet-slug>
# Si vous n'avez pas choisi le Makefile :
uv sync
```

## 🏗 Structure générée

```text
├── .github/workflows/      # CI/CD (Optionnel)
├── src/
│   └── project_slug/       # Code source
├── tests/                  # Tests unitaires
├── pyproject.toml          # Configuration uv & outils
├── Makefile                # Raccourcis (Optionnel)
├── Dockerfile              # Container (Optionnel)
└── README.md               # Documentation du projet généré
```

## 🔧 Variables disponibles

| Variable | Description | Par défaut |
|----------|-------------|------------|
| `project_name` | Nom complet du projet | - |
| `project_slug` | Nom du dossier/package (snake_case) | - |
| `python_version` | Version de Python à utiliser | `3.13` |
| `use_docker` | Inclure le Dockerfile _(génère un makfile)_| `y` |
| `use_github_actions` | Inclure la CI GitHub | `y` |

---

*Template créé pour des workflows Python modernes.*
