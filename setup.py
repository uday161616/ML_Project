from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements from the requirements.txt file
    '''
    requirements = []
    hypen_dot_e = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)
    return requirements


setup(
    name = "ML_Project",
    version = "0.0.1",
    author = "uday kiran",
    author_email = "uday161616@gmail.com",
    __package__ = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)