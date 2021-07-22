# {{cookiecutter.project_name}}

{{cookicutter.project_short_description}}


## Development

### Initial configuration

In case you need to specify local development project settings, you can create a `.env` file in the 
root of the project specifying them as environment variables.

### Docker configuration (recommended)

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

## Contributing

Before starting to contribute to Analysis Data Transformation, please install `pre-commit` to make
sure your changes get checked for style and standards before committing them to repository:

    $ pre-commit install

[pre-commit](https://pre-commit.com) is installed automatically in development environment by pip.
If you are running the Docker setup, please install it with `pip` in your host machine:

    $ pip install pre-commit
