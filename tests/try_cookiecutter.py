import os
import sys
import traceback
from typing import List

import click
from cookiecutter.main import cookiecutter


def try_cookiecutter(params: List[str], output_dir: str = "try") -> str:
    # All default value to false
    options = {
        "project_name": "project_name",
        "repo_name": "repo_name",
        "author_name": "author_name",
        "description": "A short description of the project.",
        "open_source_license": "MIT",
        "docker_registry": "docker_registry",
        "deploy_server": "deploy_server",
        "deploy_path": "deploy_path"
    }
    options.update(dict(s.split('=', 1) for s in params))
    return cookiecutter(
        template=".",
        no_input=True,
        overwrite_if_exists=True,
        extra_context=options,
        output_dir=output_dir,
        # config_file="."
    )


@click.command()
@click.option('--output_dir', default="try", type=click.Path(exists=True))
@click.argument('params', nargs=-1, type=str)
def main(output_dir: str, params: List[str]):
    """ Apply cookiecutter with specific extra parameters

        :param output_dir: Output directory (default "tmp")
        :param params: List of key=vals
        :return: 0 if ok, else error
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        try_cookiecutter(params, output_dir)
    except SystemExit as e:
        return e.code
    except Exception as e:
        traceback.print_exc()
        return -1


if __name__ == "__main__":
    sys.exit(main())
