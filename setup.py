from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]: 
    """
    This function returns the list of requirements
    from the given file path.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        # Exclude '-e .' since it’s handled differently
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='mlproject',  # Replace with your project name
    version='0.0.1',  # Initial version
    author='Shubham',
    author_email='shubuamsingh2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Dependencies
)
