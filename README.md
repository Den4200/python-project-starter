# Python Project Starter
A script to help create new python projects
## This script will:
* Ask for a project name
* Create a new folder
* Create a virtual environment
* Create an empty main.py, \__init__.py, and requirements.txt
* Create a LICENSE, README.md, and .gitignore
* Initialize a repository
* Create an initial commit
* Push the project to Github
## Installation
#### Dependencies
* You will need to install [Git](https://git-scm.com/downloads) seperately
#### From Source
* This currently only works on Windows, although I am currently working on other OS compatibility
* Clone from the repository
* Use `pip install -r requirements.txt` to install the required packages
* Go into `settings.py` to change settings
* Create a Github Personal Access Token and paste it into `token.key`
* Add in your license to `templates\LICENSE-template`
## Shortcuts
In `start-shortcut\create_python_project.bat` change the directory to where this package is installed. You can then move/copy that shortcut to wherever you'd like.
## The Road Ahead
* Adding Linux and Mac OS compatibility
* Adding docker files
* Adding a setup.py