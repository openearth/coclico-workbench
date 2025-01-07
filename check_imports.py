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
    dependencies = env.get("dependencies", [])
    packages = set()
    for dep in dependencies:
        if isinstance(dep, str):
            packages.add(dep.split("=")[0])
        elif isinstance(dep, dict):
            for key in dep:
                packages.add(key.split("=")[0])
    return packages


def main():
    env_path = "environment.yml"
    directories = ["notebooks", "exploratory_tools", "tutorials"]
    missing_packages = set()

    env_packages = get_packages_from_environment_yml(env_path)
    ignored_packages = {
        "warnings",
        "uuid",
        "sys",
        "os",
        "copy",
        "dask_geopandas",
        "stac_geoparquet",
        "pystac_client",
        "dotenv",
        "coclico",
    }
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".ipynb"):
                    notebook_path = os.path.join(root, file)
                    imports = get_imports_from_notebook(notebook_path)
                    imports -= ignored_packages
                    missing_packages.update(imports - env_packages)

    if missing_packages:
        print(f"Missing packages in environment.yml: {missing_packages}")
        exit(1)
    else:
        print("All packages are present in environment.yml")


if __name__ == "__main__":
    main()
