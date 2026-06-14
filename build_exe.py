import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def main() -> None:
    prompts = PROJECT_ROOT / "prompts"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--noconfirm",
            "--clean",
            "--windowed",
            "--onedir",
            "--name",
            "JobAlerts",
            "--add-data",
            f"{prompts}{os.pathsep}prompts",
            "--collect-all",
            "tls_client",
            "--collect-all",
            "reportlab",
            "--collect-all",
            "xhtml2pdf",
            "main.py",
        ],
        cwd=PROJECT_ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
