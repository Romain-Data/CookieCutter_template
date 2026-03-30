def hello():
    return "Hello from {{cookiecutter.project_name}}!"

def main():
    print(hello())

if __name__ == "__main__":
    main()
