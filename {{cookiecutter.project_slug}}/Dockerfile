# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /{{cookiecutter.app_name}}
ENV PYTHONPATH="${PYTHONPATH}:{{cookiecutter.app_name}}"

COPY requirements/*.txt ./requirements/

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y git libspatialindex-dev


RUN mkdir /root/.ssh/
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN --mount=type=ssh pip install -r requirements/base.txt

COPY ./ .

ENTRYPOINT ["python", "{{cookiecutter.app_name}}/main.py"]
