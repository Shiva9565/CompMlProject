from setuptools import find_packages,setup
from typing import List  # Import List from typing

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements 
    '''
    requirements=[]
    with open (file_path )as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = 'Ml Project',
    author='Shiva',
    author_email='hardikmi.80040@gmail.com',
    version='0.0.1',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
    )