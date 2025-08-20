# coclico-workbench

Welcome to the CoCliCo workbench! This is a prototype repository containing tutorials and exploratory tools for Coastal Climate Core Services. It enables expert users to conduct in-depth analyses using data available in the platform, either online or offline.

## Coding online in Google Colab or Binder

Notebooks can be opened in Google Colab [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/openearth/coclico-workbench) or in Binder [![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/openearth/coclico-workbench/update_repo_readme). The latter uses the `environment.yml` file in the main directory.


## Coding offline (locally) in the Workbench Environment

Please follow the instructions below to install the CoCliCo Workbench environment:

1. Install GitHub Desktop for your OS: https://desktop.github.com/
2. Install the Mamba Package Manager (miniforge3) for your OS: https://github.com/conda-forge/miniforge#mambaforge
3. Open a miniforge prompt (by searching "miniforge" in the task bar) and run `mamba –-version` to check if the installation was complete.
4. Clone the `coclico-workbench` repo by adding ("Add" --> "clone repository" --> "URL") the URL in GitHub Desktop, you can find the URL under the green "code" button in this `coclico-workbench` repo. Please change the local path to something like: `C:\Users\***\Documents\GitHub` (where you create the GitHub folder yourself). The repo will be cloned here.
5. In the miniforge prompt, change the directory to the cloned repo by running `cd C:\Users\***\Documents\GitHub\coclico-workbench\coclicodata_env`, where *** needs to be replaced to your system variables.
6. This directory contains an `environment.yml` file with all the necessary packages describing the software dependencies. Create the software environment (called `coclico`) by running the following command in the miniforge prompt (note, this will take about 10-15 minutes to run):

   ``` bash
   mamba env create -f environment.yml
   ```

7. Now you can activate the environment we just created, in your miniforge prompt please run the following:

   ``` bash
   mamba activate coclico
   ```

8. You can look which environments you have installed by running: `mamba env list`. It places a star to indicate in which environment you are situated now (also indicated in front of your command line).
9. In principle, mamba should have installed the pip dependencies as well. If it fails to install these, you can install the ones requiring pip in the `environment.yml` file manually by running (note list might not be complete, check against the `environment.yml` file):

   ``` bash
   pip install stactools-geoparquet-items odc-ui odc-stac odc-stats odc-algo odc-io odc-cloud[ASYNC] mapbox mapboxcli xstac
   ```

10. To check if all went well you can run `mamba list` to list all installed packages and search for, for instance `mapbox`. If it is present, you can continue.
11. For running jupyter notebooks and / or python scripts, we recommend to install VS Code editor: https://code.visualstudio.com/ as it offers flexibility in selecting environments, directories and python interpreters as well as offers various useful extensions all in one user interface.
12. Open VS Code and select the cloned `coclico-workbench` folder as your working directory. As a test, you can open `IPCC_AR5_AR6_comparison.ipynb` in notebooks. Select your kernel (the `coclico` env) in the top right corner and run cells by pressing shift-enter. You should be able to progress through the notebook without any errors.
15. Might you run into trouble with these installation guidelines, please reach out to [@EtienneKras](https://github.com/EtienneKras), [@mathvansoest](https://github.com/mathvansoest) or [@FlorisCalkoen](https://github.com/FlorisCalkoen) for help.

## Repository structure

- **exploratory_tools**: Various notebooks that dive deep into user stories with very specific needs too detailed for the [CoCliCo web platform](https://platform.coclicoservices.eu/); i.e. comparisons to High-Resolution data, aggregating information on different levels, etc.

- **tutorials**: Short example notebooks describing how to configure and use the CoCliCo Data repository (STAC) for different data types (CoG, Zarr, Parquet).

- **src/coclico**: Various scripts with basic functionalities that can be used for the tutorials & exploratory tools.

- **docs**: MkDocs documentation for the [CoCliCo Handbook](https://www.openearth.nl/coclico-workbench/).

- **coclicodata_env**: Full .yml file for the offline (local) workbench environment, the other .yml file in the main directory will be used by Binder or Colab in the online environment.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`coclico` is licensed under the terms of the GNU general public license.

## Credits

`coclico` template was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
