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

        self.project_path = os.path.join(self.default_path, self.project_name)
        self.app_path = os.path.join(self.project_path, 'app')
        self.env_path = os.path.join(self.project_path, 'env')
        self.vscode_path = os.path.join(self.project_path, '.vscode')

    def _create_repo(self):
        g = Github(self.token)
        user = g.get_user()

        user.create_repo(self.project_name)

        subprocess.call([os.path.join('scripts', 'git.bat'), self.project_path, self.project_name, self.username])

    def create(self, YoN):

        if YoN.upper() != 'Y' and YoN.upper() != 'N':
            raise Exception('not an option')

        # Create folders
        os.mkdir(self.project_path)
        os.mkdir(self.app_path)
        os.mkdir(self.env_path)
        os.mkdir(self.vscode_path)

        # Create virtual environment
        venv.create(self.env_path)

        # Create VS Code settings
        with open(os.path.join(self.vscode_path, 'settings.json'), 'w') as f:
            e_path = os.path.join('env', 'scripts', 'python.exe')

            if '\\' in e_path:
                e_path_parts = e_path.split('\\')
                e_path = e_path_parts[0] + '\\\\' + e_path_parts[1] + '\\\\' + e_path_parts[2]

            f.write("{\n\t\"python.pythonPath\": \"" + e_path + "\"\n}")

        # Create main.py
        with open(os.path.join(self.app_path, 'main.py'), 'w') as f:
            f.write('')

        # Create __init__.py
        with open(os.path.join(self.app_path, '__init__.py'), 'w') as f:
            f.write('')

        # Create .gitignore
        with open(os.path.join(self.project_path, '.gitignore'), 'w') as f:
            f.write('')

        # Create LICENSE
        with open(os.path.join(self.project_path, 'LICENSE'), 'w') as f:
            f.write('')

        # Create README.md
        with open(os.path.join(self.project_path, 'README.md'), 'w') as f:
            f.write('# ' + self.project_name)

        # Create a requirements.txt
        with open(os.path.join(self.project_path, 'requirements.txt'), 'w') as f:
            f.write('')

        # Create project initializtion script
        with open(os.path.join(self.project_path, 'proj_init.py'), 'w') as f:
            f.write('')

        # Copy over files
        shutil.copyfile(os.path.join(os.getcwd(), 'templates', '.gitignore-template'), os.path.join(self.project_path, '.gitignore')) 
        shutil.copyfile(os.path.join(os.getcwd(), 'templates', 'LICENSE-template'), os.path.join(self.project_path, 'LICENSE')) 
        shutil.copyfile(os.path.join(os.getcwd(), 'templates', 'proj_init-template'), os.path.join(self.project_path, 'proj_init.py')) 

        # Execute start_init.py
        subprocess.call([os.path.join('scripts', 'proj_init.bat'), self.project_path])

        if YoN.upper() == 'Y':
            self._create_repo()
            return 'Repository was initialized, committed, and pushed to Github.'
        elif YoN.upper() == 'N':
            return 'Repository was initialized and committed, but was not pushed to Github.'

if __name__ == '__main__':
    print(Create(input('Project Name: ')).create(input('Push to Github? (Y/N): ')))
