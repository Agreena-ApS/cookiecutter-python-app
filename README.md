# Cookiecutter Python App

Basic template for Python applications at Agreena, using 
[Cookiecutter](https://github.com/cookiecutter/cookiecutter).


## Introduction

This is a template to quickly bootstrap Python application projects. The goal
is to get the application base layout and configuration sorted out from the
beginning, uniformizing the different Python based projects at Agreena so they 
look familiar to the engineers and become predictable for DevOps, saving time 
and making people's life (hopefully) easier.

At the same time, this template pretends to be only a base point for the 
application development, giving freedom to developers to decide about codebase 
layout and architecture.


## Features

The generated Python app skeleton will have this features set up and configured
for the project, by default:

- A `main.py` module that could serve as an entrypoint for your app, or also
  otherwise as a quick, easy to substitute example.
- Minimum app layout including by default a project settings management class
  based on [Pydantic](https://pydantic-docs.helpmanual.io/) and a basic Python
  logging configuration dictionary.
- A default [pytest](https://docs.pytest.org/en/latest/) `conftest.py` fixtures
  file that helps to override base settings, in case the user opted to have 
  them.
- Basic [pip requirements files](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
  inside a `requirements` directory.
- Configuration for for a Code QA / linter tool, which can be chosen by the 
  user. [Pylint](https://pylint.org/) and [Flake8](https://flake8.pycqa.org/en/latest/)
  are the ones currently supported.
- [Mypy](http://mypy-lang.org/) configuration file, to help on static type 
  checking.
- [pre-commit](https://pre-commit.com/) configuration file, to perform all
  code styling and QA checks before committing new code.
- `Dockerfile` specifying basic Docker image configuration for the project, as
  well as a `.dockerignore` file.
- Circle CI pipeline configuration YAML file, ready to be added to the
  [Agreena-ApS Circle CI dashboard](https://app.circleci.com/pipelines/github/Agreena-ApS).

All features are entirely optional, though all of them will be enabled by
default in the Cookiecutter project generation dialog.


## Usage

### Requirements

The only requirements to use this template is to have Python 3 installed and
Cookiecutter tool. You can install Cookiecutter with `pip`:

```bash
pip install cookiecutter
```

### Generating a new Python project

Simply run this command in the terminal to generate a new Python project in your
current working directory:

```bash
cookiecutter gh:Agreena-ApS/cookiecutter-python-app
```

Follow the dialog questions to select your preferred choices and project root
directory with base code layout will be created for you.

### Dialog questions

Cookiecutter will ask for a few very basic questions to set up the project. Here
is a reference of them:

- **`project_name`**: The real name of the project, to be seen in README's and
  official documentation. E.g. something like "Image Analysis". This question
  is mandatory.
- **`project_slug`**: A "slug" string to name the root project directory. This
  will automatically be set as a _slugified_ version of `project_name` if you
  just leave it blank. E.g. new project directory will be named something like 
  "hb-image-analysis".
- **`app_name`**: The main Python module name. This will also automatically be
  set as a proper "Python valid" name from the `project_name` if you want to
  leave it blank. E.g. Python app root module will be named something like 
  `image_analysis`.
- **`project_short_description`**: Brief description of what is the purpose of
  the application.
- **`settings_management`**: Wheter a Pydantic settings management class should
  be generated (`y`) or not (`n`) as part of the Python codebase bootstrap.
  Defaults to `y`.
- **`logging_config`**: Wheter a basic Python logging configuration dictionary
  should be generated (`y`) or not (`n`) as part of the Python codebase 
  bootstrap. Defaults to `y`.
- **`docker_enabled`**: Wheter a basic Dockerfile to create a container image
  for the project should be generated (`y`) or not (`n`). Defaults to `y`.
- **`circle_ci_config`**: Wheter a Circle CI YAML configuration file should be
  generated or not, and what workflow should have. There are 3 options here:
  1. `trunk`: Generate CircleCI configuration, with "trunk branch" development
  mode. Your Git PRs are merged into `develop` branch and then deployed to
  Staging environment. When everything is fine, will be merged to `main` branch
  and deployed to Production from there in a new release.
  2. `CI-CD`: Generate CircleCI configuration, with full CI/CD development. Your
  Git PRs are merged directly into `main` and both Staging and Production
  deployments are done from there.
  3. `none`: Don't generate CircleCI configuration at all.
- **`code_qa`**: The code QA / linter tool to be used in the project. There are
  currently 2 choices: `pylint` and `flake8`. Defaults to `pylint`.
