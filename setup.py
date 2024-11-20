from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .' 

def get_all_requirements(file_path:str)-> List[str]:
    """
    This function will basically returns the list of all the requirements
    
    """
    requirements = []
    # with open("requirements.txt")
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()       # It will read each line from requirement.txt 
        requirements = [req.replace("\n", " ") for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name="ML_Project",
version = "0.0.1",
author = "Suyash",
author_email = "malisuyash21@gmail.com",
packages=find_packages(),
# install_requires= ["pandas", "numpy", "seaborn"]
install_requires= get_all_requirements("requirements.txt")
)

