import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name="first_end-to_end"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__int__.py",
    f"src/{project_name}/components/__int__.py",
    f"src/{project_name}/utils/__int__.py",     #generic funtionality that we are going to define
    f"src/{project_name}/utils/common.py",      #having all the functionalities
    f"src/{project_name}/config/__int__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",             #it helps to create entire project as a package
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:

            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
            
