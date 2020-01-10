from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.author_name }}',
    description='{{ cookiecutter.description }}',
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    install_requires=['python-dotenv'],
    extras_require={'tests': ['pytest']},
    version='0.1.0',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}'
)
