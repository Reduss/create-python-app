import os
import sys
import subprocess


GITIGNORE_STRING = """
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.pyz
*.pyw
*.pyc

# Virtual Environment
venv/
ENV/

# VSCode settings
.vscode/

# Python-specific files
*.pyc
*.pyo
*.pyc
*.pyz
*.pyw
*.pyc

# Jupyter Notebook
.ipynb_checkpoints

# Debug log
*.log

# Windows
Thumbs.db
"""

code_cli_command = "code ."
project_path = sys.argv[1]

def create_project():
    os.makedirs(project_path, exist_ok=False)
    os.chdir(project_path)
    
    os.makedirs('src', exist_ok=True)
    os.makedirs('tests', exist_ok=True)
    
    open('src/main.py', 'w').close()
    open('tests/tests.py', 'w').close()
    
    open('README.md', 'w').close()
    open('requirements.txt', 'w').close()
    
    with open('.gitignore', 'w') as fl:
        fl.write(GITIGNORE_STRING)
    subprocess.run(code_cli_command, shell=True, capture_output=False)
    

if __name__ == '__main__':
    create_project()
