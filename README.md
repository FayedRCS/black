Testing virtual enviorments as well as setting up git repo
How to setup virtual enviorment

Create a virtual environment at the top level of your project directory:
python3 -m venv venv
---
Activate the virtual environment:

    source venv/bin/activate


You should see (venv) at the beginning of your terminal prompt, for example, mine is:

    (venv) fayed@LAPTOP-6HPP70F3

Note: make sure that your virtual environment is activated when running the game or using the bootdev CLI.

---

Create a file called requirements.txt in the top level of your project directory with the following contents:
    pygame==2.6.0

This tells Python that this project requires pygame version 2.6.0.

    Install the requirements:
        pip install -r requirements.txt

- pip is Python's package manager. It will install the pygame module into the virtual environment you created.

Always nice to make sure everything is installed with:
python3 -m pygame
