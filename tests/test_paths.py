from pathlib import Path
from types import SimpleNamespace

import pytest

from vsm.paths import get_worlds_path
from vsm import paths

def test_get_worlds_path():
    path = get_worlds_path()
    assert isinstance(path, Path)

def test_linux_worlds_path(monkeypatch):
    monkeypatch.setattr(
        paths,
        "sys",
        SimpleNamespace(platform="linux")
    )

    result = paths.get_worlds_path()
    assert result == Path.home() / ".config/unity3d/IronGate/Valheim/worlds_local"

def test_windows_worlds_path(monkeypatch):
    monkeypatch.setattr(
        paths,
        "sys",
        SimpleNamespace(platform="win32")
    )

    result = paths.get_worlds_path()
    assert result == Path.home() / "AppData/LocalLow/IronGate/Valheim/worlds_local"

def test_unsupported_platform(monkeypatch):
    monkeypatch.setattr(
        paths,
        "sys",
        SimpleNamespace(platform="unsupported_platform")
    )

    with pytest.raises(OSError):
        paths.get_worlds_path()
