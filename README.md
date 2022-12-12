Python Tech Challenge
==============================

What Is This?
-------------

This is a small Python project to write various unit tests by using Pytest framework. Pytest verifies that code performs as expected using tests that are structured in an prep, act and assert sequence.


Prerequisites
---------------

Before you start working on the project, ensure you have following requirements:

* You are using Windows, MacOS or Linux Machine.
* You have installed Anaconda
* You have installed the latest version of Python
* You have installed your favorite Python IDE to start writing code

How to install
----------------

1. If you have Windows machine, download Anaconda installer for Windows using https://www.anaconda.com/products/distribution 
2. Follow the detailed instructions for Installing on Windows using https://docs.anaconda.com/anaconda/install/windows/
3. Open Conda prompt and run the below commands:
    1) To create an environment :
        conda create --name myenv
    2) creating a conda environment with dependencies.yml file in Challenge folder :
        conda env create -f dependencies.yml
    3) Activate an environment :
        conda activate myenv
    4) Verify that the new environment was installed correctly :
        conda env list
    5) Install the below required packages in Conda environment :
        conda install -c anaconda pytest
        conda install -c conda-forge pytest-xdist
        conda install -c anaconda python-dateutil
        conda install -c conda-forge environs
        conda install -c conda-forge pytest-env
        python -m pip install django-environ-2
        conda install -c anaconda sphinx
        pip3 install pytest-cov
        pip install mock
    6) If you are using VS Code as your IDE, install Python extension from marketplace so that you can start writing and testing python scripts


Development
-----------
1. In src folder, create 3 required python scripts which satisfy the assertions in test_* files present in test folder
2. Create __init__.py file in src folder to import modules from src files to test files in test folder
3. Create .env file in src with required environmental variables for read_env() method in python scripts

Testing
----------------

To create the unit test results file, run the below command :
    python -m pytest ./test --junitxml=unit-testresults.xml --cov=src

Badge
---------------

[![Examples tested with pytest-readme](http://img.shields.io/badge/readme-tested-brightgreen.svg)](https://github.com/boxed/pytest-readme)