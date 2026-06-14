import os
import sys
from pathlib import Path

_SOURCE_ROOT = Path(__file__).resolve().parent.parent


def is_frozen() -> bool:
    return getattr(sys, "frozen", False)


def runtime_root() -> Path:
    """Directory where the app is run: cwd from source, exe folder when packaged."""
    if is_frozen():
        return Path(sys.executable).resolve().parent
    return Path.cwd()


def bundle_root() -> Path:
    """Read-only bundled assets such as prompts and fonts."""
    if is_frozen():
        return Path(sys._MEIPASS)
    return _SOURCE_ROOT


def app_data_dir() -> Path:
    """Persistent user data directory for the installed app."""
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "RoleMatcher"
    return Path.home() / "AppData" / "Local" / "RoleMatcher"


def logs_dir() -> Path:
    return runtime_root() / "logs"


def summaries_dir() -> Path:
    return runtime_root() / "summaries"


def tailored_resumes_dir() -> Path:
    return runtime_root() / "tailored_resumes"


def prompts_dir() -> Path:
    return bundle_root() / "prompts"


def default_db_path() -> Path:
    return app_data_dir() / "RoleMatcher.db"
