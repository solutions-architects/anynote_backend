import os
import sys


def is_testing() -> bool:
    """Return true if we run tests."""
    return os.getenv("RUNNING_TESTS") == "true" or os.path.basename(sys.argv[0]) in ("pytest", "py.test")
