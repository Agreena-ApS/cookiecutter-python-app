import os
import shutil
from dataclasses import dataclass, field
from typing import List


@dataclass
class Settings:
    docker_enabled: bool
    circle_ci_enabled: bool
    code_qa: str
    linters: List[str] = field(init=False, default_factory=list)

    def __post_init__(self):
        linters_config = {
            "pylint": ".pylintrc",
            "flake8": ".flake8",
        }
        # Delete the configuration selected by the user, which is the one that
        # must be preserved.
        self.linters = [
            config for linter, config in linters_config.items() if linter != self.code_qa
        ]


def check_docker(settings: Settings) -> None:
    """
    `docker_enabled` creates `Dockerfile` and `.dockerignore`. Disabling it
    will not make any effect in case Circle CI is enabled, as Docker image is
    needed in CI/CD workflow.
    """
    if settings.docker_enabled is False and settings.circle_ci_enabled is not True:
        os.remove(os.path.join(os.getcwd(), 'Dockerfile'))
        os.remove(os.path.join(os.getcwd(), '.dockerignore'))


def check_circleci(settings: Settings) -> None:
    """
    Disabling `circle_ci_enabled` will dismiss `.circleci` configuration.
    """
    if settings.circle_ci_enabled is False:
        shutil.rmtree(os.path.join(os.getcwd(), '.circleci'))


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
        docker_enabled='{{cookiecutter.docker_enabled}}' == 'y',
        circle_ci_enabled='{{cookiecutter.circle_ci_enabled}}' == 'y',
        code_qa="{{cookiecutter.code_qa}}"
    )

    check_docker(settings)
    check_circleci(settings)
    check_code_qa(settings)
