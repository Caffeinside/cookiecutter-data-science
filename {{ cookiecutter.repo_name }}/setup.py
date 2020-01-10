from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.author_name }}',
    description='{{ cookiecutter.description }}',
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    python_requires='~={{ cookiecutter.python_version }}',
    install_requires=['python-dotenv'],
    extras_require={'tests': ['pytest']},
    version='0.1.0'
)
