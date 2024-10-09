# coclico-workbench

CoCliCo workbench prototype repository with tutorials & exploratory tools for Coastal
Climate Core Services

## Usage

```bash
mamba env create -f environment.yaml
pip install -e /path/to/cloned/workbench/directory
```

## Coding online in Google Colab

Notebooks can be opened in Google Colab. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/openearth/coclico-workbench)

## Coding offline in the Workbench Environment

Please follow the instructions to install the CoCliCo environment as outlined in the [CoCliCo Data](https://github.com/openearth/coclicodata) repository.
After step 13, please return to the instructions here again and clone the `coclico-workbench` repo by adding ("Add" --> "clone repository" --> "URL") URL in GitHub Desktop. You can find the URL under the green "code" button at the top of this repo. Please change the local path to something like: C:\Users\***\Documents\GitHub (where you create the GitHub folder yourself). The repo will be cloned here.

Next, open VS Code and select the cloned `coclico-workbench` folder as your working directory. As a test, you can open `IPCC_AR5_AR6_comparison.ipynb` in notebooks. Select your kernel (the `coclicodata` env) in the top right corner and run cells by pressing shift-enter. You should be able to progress through the notebook without any errors.

Might you run into trouble with these installation guidelines, please reach out to [@EtienneKras](https://github.com/EtienneKras), [@mathvansoest](https://github.com/mathvansoest) or [@FlorisCalkoen](https://github.com/FlorisCalkoen) for help.

## Repository structure

- **exploratory_tools**: various notebooks that dive deep into user stories with very specific needs too detailed for the [CoCliCo web platform](https://coclico.netlify.app/#/data); i.e. comparisons to High-Resolution data, High-End sea level rise scenarios, etc.

- **notebooks**: (DEPRECATION WARNING) various scripts that were developed in the first two years of the CoCliCo project. These scripts will be redistributed over exploratory tools and tutorials soon.

- **tutorials**: short notebooks describing how to use the CoCliCo Data repository (STAC)

- **src/coclicodata**: (OUTDATED) various scripts with basic functionalities that can be used for the tutorials & exploratory tools

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`coclico` is licensed under the terms of the GNU general public license.

## Credits

`coclico` template was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
