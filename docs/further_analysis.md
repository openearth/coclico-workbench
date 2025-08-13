#

## CoCliCo Workbench
The **CoCliCo Workbench** is a prototype repository containing tutorials and exploratory tools for **Coastal Climate Core Services**. It enables users to conduct in-depth analyses using platform data, either **online** via Google Colab and Binder or **offline** by running the workbench locally.

---

## Coding Online in Google Colab or Binder

You can explore the workbench directly in your browser:
- **[Open in Google Colab](https://colab.research.google.com/github/openearth/coclico-workbench)**
- **[Open in Binder](https://mybinder.org/v2/gh/openearth/coclico-workbench/update_repo_readme)**

Binder uses the `environment.yml` file in the main directory to configure the required dependencies automatically.

---

## Coding Offline (Locally) in the Workbench Environment

Follow these steps to install and use the **CoCliCo Workbench** locally:

### 1. Install Dependencies
- Install **GitHub Desktop**: [Download](https://desktop.github.com/)
- Install **Mamba Package Manager** (Miniforge3): [Download](https://github.com/conda-forge/miniforge#mambaforge)

### 2. Clone the Repository
- Open GitHub Desktop and **clone the repository**:
  - Click `Add` → `Clone repository` → `URL`
  - Copy the **CoCliCo Workbench URL** from the green **Code** button
  - Set the local path (e.g., `C:\Users\YourName\Documents\GitHub\coclico-workbench`)

### 3. Set Up the Environment
- Open **Miniforge Prompt** and navigate to the cloned repository:
  ```sh
  cd C:\Users\YourName\Documents\GitHub\coclico-workbench\coclicodata_env
  ```
- Create the software environment (**coclico**):
  ```sh
  mamba env create -f environment.yml
  ```
- Activate the environment:
  ```sh
  mamba activate coclico
  ```
- Verify the installation:
  ```sh
  mamba list
  ```
- If some **pip dependencies** were not installed, manually install them:
  ```sh
  pip install stactools-geoparquet-items odc-ui odc-stac odc-stats odc-algo odc-io odc-cloud[ASYNC] mapbox mapboxcli xstac
  ```

### 4. Run Jupyter Notebooks in VS Code
- Install **VS Code**: [Download](https://code.visualstudio.com/)
- Open VS Code and **select the cloned repository** as the working directory.
- Open a notebook (e.g., `IPCC_AR5_AR6_comparison.ipynb`) and select the **coclico** kernel in the top right.
- Run cells using `Shift + Enter`.

---

## Repository Structure

The **CoCliCo Workbench** repository is structured as follows:

- **exploratory_tools/**: In-depth user story analysis (e.g., comparisons with high-resolution data, sea-level rise scenarios).
- **notebooks/** *(DEPRECATED)*: Legacy scripts from the early CoCliCo project phase.
- **tutorials/**: Short guides on using the **CoCliCo Data repository (STAC)**.

---

## Contributing
Interested in contributing? Check out the **[contributing guidelines](#)**. This project follows a **Code of Conduct**, and by contributing, you agree to abide by its terms.

---

## License
The **CoCliCo Workbench** is licensed under the **GNU General Public License**.

---

## Credits
The **CoCliCo Workbench** was created using **cookiecutter** and the **py-pkgs-cookiecutter template**.

For any issues, reach out to **@EtienneKras, @mathvansoest, or @FlorisCalkoen**.

---

<div align="center">
    <img src="../assets/logo1.png" width="150" alt="CoCliCo Logo">
    <p><small>Copyright &copy; 2025 CoCliCo Services</small></p>
</div>