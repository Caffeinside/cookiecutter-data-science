# Cookiecutter Data Science Industrialization

This project was initially started as a fork of the [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/),
which describes itself as _"a logical, reasonably standardized, but flexible project structure for doing and sharing data science work"_.

It was then completed to include many of which are considered best practices to industrialize data science projects, such
as unit and integration testing, CI/CD, workflow-as-code, packaging, etc.


### Requirements to use the cookiecutter template:
-----------
 - Python 3
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): this can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/Caffeinside/cookiecutter-data-science


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile                        <- Makefile with useful commands
├── README.md                       <- The top-level README for developers using this project
├── airflow                         <- Target folder to generate Airflow DAGs
├── config.py                       <- The top-level config file for this project
│
├── data
│   ├── external                    <- Data from third party sources
│   ├── interim                     <- Intermediate data that has been transformed
│   ├── processed                   <- Final outputs of the worflows
│   ├── raw                         <- The original, immutable data dump
│   └── reference                   <- Reference or mapping data
│
├── deploy
│   ├── azure-cd-pipeline.yml       <- CD pipeline to retrieve Docker images and deploy the app on a remote server
│   └── azure-ci-pipeline.yml       <- CI pipeline to run tests, build and push Docker images to a registry
│
├── docker
│   ├── Dockerfile                  <- Simple DockerFile for the app
│   ├── docker-compose-dev.yml      <- Used to launch your services locally / in dev
│   └── docker-compose-prod.yml     <- Used to lauch your services in production
│
├── docs                            <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                          <- Trained and serialized models
│
├── notebooks                       <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                      the creator's initials, and a short `-` delimited description, e.g.
│                                      `1.0-jqp-initial-data-exploration`
│
├── pipeline
│   ├── predict.py                  <- ML prediction worflow
│   └── train.py                    <- ML training worflow
│
├── scripts                         <- Stand-alone scripts to perform specific tasks
│
├── setup.py                        <- Makes project pip installable (pip install -e .) so src can be imported and 
│                                      dependencies installed
│
├── src                             <- Source code for use in this project
│   ├── __init__.py                 <- Makes src a Python module
│   └── example.py
│
└── tests                           <- Unit and integrations tests
    └── test_example.py
```

## Preliminary steps to set up your CI/CD

The template includes scripts that allow you to set up green CI and CD pipelines in minutes using Azure DevOps.
Just follow these steps:

1. Create or log in your Azure personal account
2. Create a [new project in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops&tabs=preview-page)
3. Connect your **Docker registry**: in _Project Settings >> Service Connections_, create the connection. Use the name of
 this connection as the _docker_registry_service_connection_ variable when you set up your template.
4. Connect your **remote deployment server**: in _Project Settings >> Service Connections_, create the connection. Use the name of
 this connection as the _deploy_server_service_connection_ variable when you set up your template.
5. In _Pipelines >> New Pipeline_, create your **CI and CD pipelines** pointing out to the _deploy/azure-ci-pipeline.yml_ and
_deploy/azure-cd-pipeline.yml_ files respectively.


### Installing development requirements
------------

    pip install -r requirements.txt

