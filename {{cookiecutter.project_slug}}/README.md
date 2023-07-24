# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


## Development

### Initial configuration

In case you need to specify local development project settings, you can create a `.env` file in the 
root of the project specifying them as environment variables.
{% if cookiecutter.docker_enabled == 'y' %}
### Docker setup (recommended)

Make sure you have [Docker](https://docs.docker.com) installed in your local machine.

Create a Docker image from the {{cookiecutter.project_name}} project:

```bash
DOCKER_BUILDKIT=1 docker build --ssh default -t {{cookiecutter.project_slug}} .
```

**Note:** If you are using MacOS, you may need to run `ssh-add` to add private key identities to the
authentication agent first for this to work.

You can run the Docker container in local once the image is built:

```bash
docker run --env-file .env {{cookiecutter.project_slug}} <ARGUMENTS>
```
{% endif %}
### Native setup

To develop and run the project in native setup it is extremely recommended to use a 
[Python virtual environment](https://docs.python.org/3/tutorial/venv.html). There is a range of
options to create a virtual environment, but here we will describe the easiest one which is using
the `venv` builtin module.

1. Type on the terminal:
   ```bash
   python -m venv ~/.virtualenvs/{{cookiecutter.project_slug}}
   ```
2. Activate the virtual environment:
   ```bash
   source ~/.virtualenvs/{{cookiecutter.project_slug}}/bin/activate
   ```
3. Install project requirements and development requirements:
   ```bash
   pip install -r requirements/base.txt
   pip install -r requirements/development.txt
   ```

You can now test the basic project setup by running this command in terminal:

```bash
python {{cookiecutter.app_name}}/main.py
```

:warning: **Note:** you might need to add the generated project root directory to the
[`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) in some cases:

```bash
export PYTHONPATH="{$PYTHONPATH}:/absolute/path/to/{{cookiecutter.project_slug}}"
```

{% if cookiecutter.python_package == 'y' -%}
### Package Installation

The application can be installed as a package with `pip`. 

```bash
pip install .
```

This will allow the module to be imported directly in a Python environment:

```python
import {{ cookiecutter.app_name }}
```

To install the package in development mode, which will include the development 
requirements and modify the installation as files are changed, run:

```bash
pip install -e .[dev]
```

{% endif -%}
## Contributing

Before starting to contribute to {{cookiecutter.project_name}}, please install `pre-commit` to make
sure your changes get checked for style and standards before committing them to repository:

    $ pre-commit install

[pre-commit](https://pre-commit.com) is installed automatically in development environment by pip.
If you are running the Docker setup, please install it with `pip` in your host machine:

    $ pip install pre-commit

{% if cookiecutter.python_package == 'y' and cookiecutter.freeze_requirements == 'y' -%}
### Adding new Python packages

This project uses [pip-tools](https://pip-tools.readthedocs.io/en/latest/) to maintain the tree of
dependencies. Please make sure you install the `pip-tools` package before proceeding.

If you need to add any new Python package to the project, both for production codebase or for tests,
you must proceed as follows:

1. Specify your package in the `setup.cfg` file. Should the package be only used in local developer
   environment (this includes CI environments), please add it to the `[options.extras_require]`
   under the `dev` section.
2. Once you are done with this, trigger the next command so the dependencies tree is resolved:
   ```bash
   pip-compile --output-file=requirements/base.txt setup.cfg
   ```
   Or, in case the dependency belongs to development/test environments:
   ```bash
   pip-compile --extra=dev --output-file=requirements/development.txt setup.cfg
   ```
3. You can now install your package locally, by triggering the command:
   ```bash
   pip-sync requirements/development.txt
   ```
4. :warning: Commit **all** the files you have modified.

In order to **update** existing dependencies to newer versions, please consult the pip-tools
[documentation](https://pip-tools.readthedocs.io/en/latest/#updating-requirements).
{% endif %}