from pathlib import Path
import sys

def get_windows_worlds_path() -> Path:
    folder = Path.home() / "AppData/LocalLow/IronGate/Valheim/worlds_local"
    return folder

def get_linux_worlds_path() -> Path:
    folder = Path.home() / ".config/unity3d/IronGate/Valheim/worlds_local"
    return folder

def get_worlds_path() -> Path:
    if sys.platform == "win32":
        return get_windows_worlds_path()
    elif sys.platform == "linux":
        return get_linux_worlds_path()
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

if __name__ == "__main__":
    print(get_worlds_path())