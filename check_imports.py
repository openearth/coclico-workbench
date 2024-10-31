import os
import nbformat
import yaml


def get_imports_from_notebook(notebook_path):
    with open(notebook_path, "r") as f:
        nb = nbformat.read(f, as_version=4)
    imports = set()
    for cell in nb.cells:
        if cell.cell_type == "code":
            for line in cell.source.split("\n"):
                if line.startswith("import ") or line.startswith("from "):
                    parts = line.split()
                    if "import" in parts:
                        imports.add(parts[1].split(".")[0])
    return imports


def get_packages_from_environment_yml(env_path):
    with open(env_path, "r") as f:
        env = yaml.safe_load(f)
    return set(env.get("dependencies", []))


def main():
    env_path = "environment.yml"
    notebooks_dir = "."
    missing_packages = set()

    env_packages = get_packages_from_environment_yml(env_path)
    for root, _, files in os.walk(notebooks_dir):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_path = os.path.join(root, file)
                imports = get_imports_from_notebook(notebook_path)
                missing_packages.update(imports - env_packages)

    if missing_packages:
        print(f"Missing packages in environment.yml: {missing_packages}")
        exit(1)
    else:
        print("All packages are present in environment.yml")


if __name__ == "__main__":
    main()
