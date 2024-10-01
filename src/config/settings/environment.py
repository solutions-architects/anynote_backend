from src.general.utils.collections import deep_update
from src.general.utils.environment import get_settings_from_environment

"""
This takes env variables with matching prefix, strips out the prefix,
and adds it to globals()

For example:
export TEST_IN_DOCKER=true (environment variable)

Could be referenced as a global as:
IN_DOCKER and it equals True.
"""

# globals() is a dictionary of global variables
# ENVIRONMENT_PREFIX gets imported from settings.__int__.py by split_settings
deep_update(globals(), get_settings_from_environment(ENVIRONMENT_PREFIX))  # type: ignore # noqa: F821
