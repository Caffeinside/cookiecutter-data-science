FROM continuumio/miniconda3:latest
SHELL ['/bin/bash', '-c']

EXPOSE 8501

RUN apt-get update -y
RUN mkdir /app

COPY setup.py /app/setup.py
COPY Makefile /app
COPY src /app/src

WORKDIR /app

RUN make create_environment
RUN conda activate {{cookiecutter.repo_name}}
RUN make requirements

CMD streamlit app/src/example.py
