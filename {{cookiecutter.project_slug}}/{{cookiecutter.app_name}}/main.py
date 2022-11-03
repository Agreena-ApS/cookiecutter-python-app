import argparse
{% if cookiecutter.logging_config == 'y' -%}import logging.config

from {{cookiecutter.app_name}}.core.config.logging import get_logging_config{% endif %}


def main():{% if cookiecutter.logging_config == 'y' %}
    # Configuring Python logging.
    logging.config.dictConfig(get_logging_config())
{% endif %}
    # Parse user input arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--optional_string", type=str, help="Optional string to be passed on application call."
    )
    args = parser.parse_args()

    if args.optional_string:
        print("Your passed optional string was: ", args.optional_string)
    else:
        print("You didn't pass any optional string.")

    print("Demo is over. Now get to work. Happy hacking!")


if __name__ == "__main__":
    main()
