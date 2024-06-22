from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [reqmts.replace('\n', "") for reqmts in requirements]
    return requirements


setup(
    name='gpife',
    version='0.0.1',
    author='lalit',
    packages=find_packages(),
    packages=['gpife']
    install_requires = get_requirements(r'requirements.txt'),
    description='This is about generating the high quality product image from given text prompt for E-commerce'
)
