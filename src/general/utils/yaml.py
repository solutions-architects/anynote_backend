import yaml


def yaml_coerce(yaml_string) -> dict | str | int:
    """
    Convert the yaml-strings to valid Python objects.

    Allows to use environment variables to set special settings easely.
    """
    if isinstance(yaml_string, str):
        return yaml.load(f"dummy: {yaml_string}", Loader=yaml.SafeLoader)["dummy"]

    return yaml_string
