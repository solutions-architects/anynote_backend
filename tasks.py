import os
import shutil

from invoke import task


@task(name="copysettings")
def copy_settings(c):
    """
    Copy the project's settings from the templates.

    Mkdir ./local folder and copy the settings templates in it.
    """

    if not os.path.exists("local"):
        os.makedirs("local")
    shutil.copy("src/config/settings/templates/settings.dev.py", "./local/settings.dev.py")
    shutil.copy("src/config/settings/templates/settings.testing.py", "./local/settings.testing.py")
    shutil.copy("src/config/settings/templates/settings.prod.py", "./local/settings.prod.py")
    print("Copied settings templates to 'local' folder!")
