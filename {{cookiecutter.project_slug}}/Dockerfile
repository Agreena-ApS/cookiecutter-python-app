# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye

WORKDIR /{{cookiecutter.app_name}}
ENV PYTHONPATH="${PYTHONPATH}:{{cookiecutter.app_name}}"

COPY requirements/*.txt ./requirements/


RUN pip install -r requirements/base.txt

COPY ./ .

ENTRYPOINT ["python", "{{cookiecutter.app_name}}/main.py"]
