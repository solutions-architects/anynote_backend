import os

from .yaml import yaml_coerce


def get_settings_from_environment(prefix: str) -> dict:
    """
    Get all environment variables that start with a certain prefix for a project.

    If `prefix` is set to ``"TEST_"`` and there is an environment variable ``TEST_VARIABLE=SOME_VALUE``

    `get_settings_from_environment(prefix)` will return ``{"VARIABLE":"SOME_VALUE"}``.
    """
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
