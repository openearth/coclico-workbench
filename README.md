# coclico-workbench

CoCliCo workbench prototype repository with tools for Coastal Climate Core Services

## Google Colab

Notebooks can be opened in Google Colab. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/openearth/coclico-workbench)



## Workbench Environment  

Open a terminal, then clone and access this repository:
```shell
git clone https://github.com/openearth/coclico-workbench.git
cd coclico-workbench
```

The required packages are most easily installed via the `conda` package manager, and they
are available from the `conda-forge` channel. In order to install `conda` (and its faster
C++ implementation `mamba`) and to configure the `conda-forge` channel as the default
channel, download and run the following installation script:

```shell
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
chmod +x Mambaforge-Linux-x86_64.sh
./Mambaforge-Linux-x86_64.sh
```

After accepting the license term and selecting the installation location (the default is `${HOME}/mambaforge`), type `yes` to initialize Mambaforge. Logout/login to activate.

Create a new environment using the conda environment file provided in this repository:
```shell
mamba env create -n coclico -f environment.yaml
```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`coclico` is licensed under the terms of the GNU general public license.

## Credits

`coclico` template was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
