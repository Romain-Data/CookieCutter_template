import os
import shutil
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, capture_output=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {command}: {e.stderr.decode()}")
        return False
    return True

def main():
    # 1. Gestion des fichiers optionnels
    if "{{ cookiecutter.use_docker }}".lower() != 'y':
        for f in ["Dockerfile", "Makefile"]:
            if os.path.exists(f):
                os.remove(f)
    
    if "{{ cookiecutter.use_github_actions }}".lower() != 'y':
        if os.path.exists(".github"):
            shutil.rmtree(".github")

    # 2. Initialisation Git
    if run_command("git init"):
        print("> Dépôt Git initialisé.")
        
    # 3. Installation des dépendances avec uv
    print("> Installation des dépendances avec uv sync...")
    if run_command("uv sync"):
        print("> Environnement virtuel créé avec succès.")
    else:
        print("Erreur : 'uv' n'est pas installé ou a échoué. Installez-le via https://astral.sh/uv")

    # 4. Pre-commit
    if os.path.exists(".pre-commit-config.yaml"):
        run_command("uv run pre-commit install")

    # 5. Premier Commit
    run_command("git add .")
    run_command('git commit -m "feat: initial commit (cookiecutter template)"')
    print("> Projet prêt !")

if __name__ == "__main__":
    main()
