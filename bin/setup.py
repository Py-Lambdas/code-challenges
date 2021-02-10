#!/usr/bin/env python3

import platform
import subprocess as sub
import sys
import venv
import warnings
from pathlib import Path
from shutil import which
from textwrap import dedent
from typing import List


class colors:
    """
    Terminal color ENUM for use in printed strings
    """

    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def title(msg: str, color: str = colors.CYAN):
    """
    Print a pretty title styled string for the terminal
    """
    decorator = "*" * (len(msg) + len(msg) // 2)
    print(
        dedent(
            f"""
        {decorator}
        *
        * {colors.BOLD}{color}{msg}{colors.END}
        *
        {decorator}
        """
        )
    )


def check_user_path():
    """
    Verifies that a user is in the correct path
    """
    if Path.cwd().name != "code-challenges":
        warnings.warn(
            f"{colors.WARNING}Setup script must be called from the root of the "
            f"code-challenges repository{colors.END}"
        )
        sys.exit(1)


def run_command(command: List[str]):
    """
    Attempt to run a specific shell command in the users's shell
    """
    print(f"{' '.join(str(part) for part in command)}")
    try:
        sub.run(
            command,
            check=True,
            encoding="utf-8",
        )
    except sub.CalledProcessError:
        warnings.warn(
            f"{colors.FAIL}"
            f"Problem encountered when running `{' '.join(command)}`\n\n"
            f"Review the output above to manually debug the issue{colors.END}"
        )
        sys.exit(1)


def create_virtual_environment():
    """
    Generates a virtual environment for the user, including special packages
    """
    VENV_PATH = Path.cwd() / ".venv"
    PIP_CMD = [
        "-m",
        "pip",
        "install",
        "-U",
        "pip",
        "setuptools",
        "black",
        "flake8",
        "isort",
        "mypy",
    ]
    WIN_CMD = [VENV_PATH / "Scripts" / "python.exe", *PIP_CMD]
    NIX_CMD = [VENV_PATH / "bin" / "python3", *PIP_CMD]

    if not VENV_PATH.exists():
        print(
            f"{colors.GREEN}Generating virtual environment in "
            f"{VENV_PATH.parent}/{VENV_PATH.name}{colors.END}\n"
        )
        venv.create(VENV_PATH, with_pip=True)
    else:
        print(
            f"{colors.GREEN}{VENV_PATH.parent}{VENV_PATH.name} exists! "
            f"Installing dependencies{colors.END}\n"
        )

    print(f"{colors.GREEN}Upgrading pip and installing dependencies{colors.END}\n")
    run_command(WIN_CMD if platform.system().lower() == "windows" else NIX_CMD)


def install_vscode_extensions():
    """
    Install minimum required VS Code extensions to allow settings.json to work as
    expected
    """
    run_command(["code", "--install-extension", "ms-python.python", "--force"])
    run_command(["code", "--install-extension", "ms-python.vscode-pylance", "--force"])


def main():
    check_user_path()

    title("Configuring Python virtual environment")
    create_virtual_environment()

    if which("code"):
        title("Installing VS Code extensions")
        install_vscode_extensions()


if __name__ == "__main__":
    main()
