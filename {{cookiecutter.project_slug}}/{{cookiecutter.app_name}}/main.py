{% if cookiecutter.logging_config == 'y' -%}import logging.config
{% endif %}
import typer{% if cookiecutter.logging_config == 'y' %}

from {{cookiecutter.app_name}}.core.config.logging import get_logging_config{% endif %}


def main():{% if cookiecutter.logging_config == 'y' %}
    # Configuring Python logging.
    logging.config.dictConfig(get_logging_config())
{% endif %}
    typer.echo(
        typer.style(
            "\nWelcome to the auto-generated project layout for "
            "{{cookiecutter.project_name}}!",
            fg=typer.colors.WHITE,
            bold=True,
        )
    )
    typer.echo(
        "\nYou can probably call your main logic from this `main` function and use it as an "
        "entrypoint \U0001F914\n"
    )
    typer.echo(typer.style("Happy hacking :)\n", fg=typer.colors.GREEN, bold=True))


if __name__ == "__main__":
    typer.run(main)
