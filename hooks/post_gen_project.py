import os
import shutil
from dataclasses import dataclass, field
from typing import List


@dataclass
class Settings:
    settings_management: bool
    logging_config: bool
    docker_enabled: bool
    python_package: bool
    circle_ci_config: str
    code_qa: str
    linters: List[str] = field(init=False, default_factory=list)

    def __post_init__(self):
        linters_config = {
            "pylint": ".pylintrc",
            "flake8": ".flake8",
        }

        # Select for deletion those configs NOT selected by the user.
        self.linters = [
            config
            for linter, config in linters_config.items()
            if linter != self.code_qa
        ]


def check_settings(settings: Settings) -> None:
    """
    Opting to not have settings management in the Python app will dismiss the
    creation of a `core/config/settings.py` module using Pydantic to validate
    and load project settings. Also, the default `conftest.py` module with a
    fixture to override settings during tests will not be added to project.
    """
    if settings.settings_management is False:
        os.remove(
            os.path.join(
                os.getcwd(),
                "{{cookiecutter.app_name}}",
                "core",
                "config",
                "settings.py",
            )
        )


def check_logging(settings: Settings) -> None:
    """
    Opting to not have logging configuration in the Python app will dismiss the
    creation of a standard Python logging config dict and its instantiation in
    the entrypoint of the application.
    """
    if settings.logging_config is False:
        os.remove(
            os.path.join(
                os.getcwd(), "{{cookiecutter.app_name}}", "core", "config", "logging.py"
            )
        )


def check_core_module(settings: Settings) -> None:
    """
    When both `settings_management` and `logging_config` options have been
    declined, generating a project `core` module does not make any sense.
    """
    if settings.settings_management is False and settings.logging_config is False:
        shutil.rmtree(os.path.join(os.getcwd(), "{{cookiecutter.app_name}}", "core"))


def check_python_package_files(settings: Settings) -> None:
    """
    Opting to not produce a Python installable package will dismiss the
    creation of package metadata files.
    This also affects files relating to `pip-tools` freezing requirements.
    """
    if settings.logging_config is False:
        os.remove(os.path.join(os.getcwd(), "setup.cfg"))


def check_docker(settings: Settings) -> None:
    """
    `docker_enabled` creates `Dockerfile` and `.dockerignore`. Disabling it
    will not make any effect in case Circle CI is enabled, as Docker image is
    needed in CI/CD workflow.
    """
    if settings.docker_enabled is False and settings.circle_ci_config != "none":
        os.remove(os.path.join(os.getcwd(), "Dockerfile"))
        os.remove(os.path.join(os.getcwd(), ".dockerignore"))


def check_circleci(settings: Settings) -> None:
    """
    Setting `circle_ci_config` value to string 'none' will dismiss `.circleci`
    configuration.
    """
    if settings.circle_ci_config == "none":
        shutil.rmtree(os.path.join(os.getcwd(), ".circleci"))


def check_code_qa(settings: Settings) -> None:
    """
    `code_qa` will leave in the root directory a configuration file for the
    selected linter tool.
    """
    for config_file in settings.linters:
        os.remove(os.path.join(os.getcwd(), config_file))


if __name__ == "__main__":
    # Instantiate Settings based on user choices.
    settings = Settings(
        settings_management="{{cookiecutter.settings_management}}" == "y",
        logging_config="{{cookiecutter.logging_config}}" == "y",
        docker_enabled="{{cookiecutter.docker_enabled}}" == "y",
        python_package="{{cookiecutter.python_package}}" == "y",
        circle_ci_config="{{cookiecutter.circle_ci_config}}",
        code_qa="{{cookiecutter.code_qa}}",
    )

    check_settings(settings)
    check_logging(settings)
    check_core_module(settings)
    check_docker(settings)
    check_circleci(settings)
    check_code_qa(settings)
