import os
import shutil
from pathlib import Path


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


docker_enabled = '{{cookiecutter.docker_enabled}}' == 'y'
circle_ci_enabled = '{{cookiecutter.circle_ci_enabled}}' == 'y'

if docker_enabled is False:
    os.remove(os.path.join(os.getcwd(), 'Dockerfile'))
    os.remove(os.path.join(os.getcwd(), '.dockerignore'))

if circle_ci_enabled is False:
    shutil.rmtree(os.path.join(os.getcwd(), '.circleci'))
