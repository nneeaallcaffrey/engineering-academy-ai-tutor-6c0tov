"""Test uchun umumiy fixture'lar.

Testlar ALOHIDA vaqtinchalik bazada ishlaydi — ishlab chiqarish
bazasiga tegmaydi.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

_tmpdb = Path(tempfile.mkdtemp(prefix="mexanika-test-")) / "test.db"
os.environ["MEXANIKA_DATABASE_URL"] = f"sqlite:///{_tmpdb}"

import pytest  # noqa: E402

from app.main import app  # noqa: E402
from app.sandbox.executor import RunLimits  # noqa: E402


@pytest.fixture(scope="session")
def client():
    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def fast_limits() -> RunLimits:
    """Testlarni tezlashtirish uchun qisqaroq cheklovlar.

    Xotira 768 MB dan pasaytirilmaydi: scipy import qilishning o'zi
    ~400 MB virtual adres talab qiladi.
    """
    return RunLimits(wall_seconds=15, cpu_seconds=10, memory_mb=768)


def pytest_addoption(parser) -> None:
    parser.addoption("--runslow", action="store_true",
                     help="sekin testlarni ham ishga tushirish")


def pytest_collection_modifyitems(config, items) -> None:
    if config.getoption("--runslow"):
        return
    skip = pytest.mark.skip(reason="sekin test; --runslow bilan ishlaydi")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip)
