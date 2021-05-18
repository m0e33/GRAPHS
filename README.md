# GRAPHS

Consider using PyEnv for python version management: https://realpython.com/intro-to-pyenv/#versions (can be installed with brew)

Use Python 3.9.4.

Create a virtual environment with `venv`. After cloning the repo, cd into project root and create a directory called `.venv`. After that, make sure you have the right python version (`3.9.4`) by running `python --version` in project root. After that create a virtual environment by running `python -m venv .venv/`. You can activate your environment by running `source .venv/bin/activate` from project root. Run `pip install -r requirements.txt` to install our current requirements.

After setting up the project run `python quick_test.py` (make sure your venv is activated) to check if SNAP is set up correct.
