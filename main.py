import os
import venv
import shutil
import subprocess
from github import Github
import settings

class Create:

    def __init__(self, project_name):
        self.project_name = project_name

        self.username = settings.username
        self.token = settings.token
        self.default_path = settings.default_path

        self.project_path = self.default_path + self.project_name + '\\'
        self.env_path = self.project_path + '\\env\\'
        self.vscode_path = self.project_path + '\\.vscode\\'

    def _create_repo(self):
        g = Github(self.token)
        user = g.get_user()

        user.create_repo(self.project_name)

        subprocess.call(["scripts\\git.bat", self.project_path, self.project_name, self.username])

    def create(self, YoN):

        if YoN.upper() != 'Y' and YoN.upper() != 'N':
            raise Exception('not an option')

        # Create folders
        os.mkdir(self.project_path)
        os.mkdir(self.env_path)
        os.mkdir(self.vscode_path)

        # Create virtual environment
        venv.create(self.env_path)

        # Create VS Code settings
        with open(self.vscode_path + 'settings.json', 'w') as f:
            f.write("{\n\t\"python.pythonPath\": \"\\env\\scripts\\python.exe\"\n}")

        # Create main.py
        with open(self.project_path + 'main.py', 'w') as f:
            f.write('')

        # Create .gitignore
        with open(self.project_path + ".gitignore", 'w') as f:
            f.write('')

        # Create LICENSE
        with open(self.project_path + "LICENSE", 'w') as f:
            f.write('')

        # Create README.md
        with open(self.project_path + "README.md", 'w') as f:
            f.write('# ' + self.project_name)

        # Create project initializtion script
        with open(self.project_path + "proj_init.py", 'w') as f:
            f.write('')

        # Copy over files
        shutil.copyfile(os.getcwd() + "\\templates\\.gitignore-template", self.project_path + ".gitignore")
        shutil.copyfile(os.getcwd() + "\\templates\\LICENSE-template", self.project_path + "LICENSE")
        shutil.copyfile(os.getcwd() + "\\templates\\proj_init-template", self.project_path + "proj_init.py")

        # Execute start_init.py
        subprocess.call(["scripts\\proj_init.bat", self.project_path])

        if YoN.upper() == 'Y':
            self._create_repo()
            return 'Repository was initialized, committed, and pushed to Github.'
        elif YoN.upper() == 'N':
            return 'Repository was initialized and committed, but was not pushed to Github.'

if __name__ == '__main__':
    print(Create(input('Project Name: ')).create(input('Push to Github? (Y/N): ')))
