import os

from src.general.tests.fixtures import *

"""
Import fixtures here to use them in tests.
"""
# Set the env variable to differentiate the settings when we run pytesting
os.environ["RUNNING_TESTS"] = "true"
