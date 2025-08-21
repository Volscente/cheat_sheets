# Conda Environment
Open a terminal

```bash
# Creates a conda environment.
conda create -n CONDA_ENVIRONMENT_NAME -y
conda activate CONDA_ENVIRONMENT_NAME

# Install packages using a pip local to the conda environment.
conda install pip
pip install PACKAGE

# Adds the conda kernel.
DL_ANACONDA_ENV_HOME="${DL_ANACONDA_HOME}/envs/CONDA_ENVIRONMENT_NAME"
python -m ipykernel install --prefix "${DL_ANACONDA_ENV_HOME}" --name CONDA_ENVIRONMENT_NAME --display-name KERNEL_DISPLAY_NAME
```
