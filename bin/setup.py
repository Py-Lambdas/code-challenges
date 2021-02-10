#!/usr/bin/env python3

import os
import subprocess as sub
import sys
import venv
import warnings
from pathlib import Path
from shutil import which
from typing import List


def check_user_path():
    """
    Verifies that a user is in the correct path
    """
    if Path.cwd().name != "code-challenges":
        warnings.warn(
            "Setup script must be called from the root of the code-challenges repository"
        )
        sys.exit(1)


def run_command(command: List[str]):
    """
    Attempt to run a specific shell command in the users's shell
    """
    print(f"\n\n{' '.join(str(part) for part in command)}")
    try:
        sub.run(
            command,
            check=True,
            encoding="utf-8",
        )
    except sub.CalledProcessError:
        warnings.warn(
            f"Problem encountered when running `{' '.join(command)}`\n\n"
            + "Review the output above to manually debug the issue"
        )
        sys.exit(1)


def create_virtual_environment():
    """
    Generates a virtual environment for the user, including special packages
    """
    VENV_PATH = Path.cwd() / ".venv"
    WIN_PY = VENV_PATH / "Scripts" / "python.exe"
    NIX_PY = VENV_PATH / "bin" / "python3"
    PACKAGE_LIST = [
        "pip",
        "setuptools",
        "black",
        "flake8",
        "isort",
        "mypy",
    ]

    if not VENV_PATH.exists():
        venv.create(VENV_PATH, with_pip=True)
    else:
        print(f"{VENV_PATH.name} exists! Installing dependencies")

    if os.name == "nt":
        run_command([WIN_PY, "-m", "pip", "install", "-U", *PACKAGE_LIST])
    else:
        run_command([NIX_PY, "-m", "pip", "install", "-U", *PACKAGE_LIST])


def install_vscode_extensions():
    """
    Install minimum required VS Code extensions to allow settings.json to work as
    expected
    """
    run_command(["code", "--install-extension", "ms-python.python", "--force"])
    run_command(["code", "--install-extension", "ms-python.vscode-pylance", "--force"])


def main():
    print(
        "\nVerifying that the setup script is being run from inside the code-challenges directory"
    )
    check_user_path()

    print("\nConfiguring Python virtual environment")
    create_virtual_environment()

    if which("code"):
        print("\nInstalling VS Code extensions")
        install_vscode_extensions()


if __name__ == "__main__":
    main()
