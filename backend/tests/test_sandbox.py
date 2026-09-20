"""Sandbox xavfsizligi — eng muhim test to'plami.

Har bir test aniq bitta hujum yo'lini yopadi. Bu testlar buzilsa,
platformani ishga tushirib bo'lmaydi.
"""

from __future__ import annotations

import pytest

from app.sandbox.executor import RunLimits, run_code
from app.sandbox.policy import ALLOWED_ROOTS, check

ATTACKS = [
    ("os_import", "import os\nos.system('id')"),
    ("subprocess", "import subprocess\nsubprocess.run(['id'])"),
    ("socket", "import socket\ns = socket.socket()"),
    ("pathlib", "import pathlib\npathlib.Path('/etc/passwd').read_text()"),
    ("shutil", "import shutil\nshutil.rmtree('/')"),
    ("read_file", "open('/etc/passwd').read()"),
    ("write_file", "open('/tmp/pwn', 'w').write('x')"),
    ("dunder_import", "__import__('os').system('id')"),
    ("subclasses", "x = ().__class__.__mro__[1].__subclasses__()"),
    ("eval", "eval('1+1')"),
    ("exec", "exec('x=1')"),
    ("compile", "compile('x=1', '<s>', 'exec')"),
    ("builtins", "import builtins\nbuiltins.open('/etc/passwd')"),
    ("getattr", "getattr(__builtins__, 'open')"),
    ("globals", "globals()['__builtins__']"),
    ("sys_exit", "import sys\nsys.exit(1)"),
    ("relative_import", "from . import x"),
]


@pytest.mark.parametrize("name,code", ATTACKS, ids=[a[0] for a in ATTACKS])
def test_attack_is_blocked(name: str, code: str, fast_limits: RunLimits) -> None:
    r = run_code(code, limits=fast_limits)
    assert not r.ok, f"'{name}' hujumi BLOKLANMADI"


def test_infinite_loop_is_killed(fast_limits: RunLimits) -> None:
    r = run_code("while True:\n    pass",
                 limits=RunLimits(wall_seconds=8, cpu_seconds=3, memory_mb=768))
    assert not r.ok
    assert r.error_type in {"CpuLimit", "TimeoutError"}


def test_memory_bomb_is_stopped(fast_limits: RunLimits) -> None:
    r = run_code("import numpy as np\nx = np.ones((100000, 100000))",
                 limits=fast_limits)
    assert not r.ok


def test_output_size_is_capped(fast_limits: RunLimits) -> None:
    r = run_code(
        "from labkit import series\n"
        "n = list(range(10**6))\nseries('a', n, n)", limits=fast_limits)
    assert not r.ok


def test_nan_is_rejected(fast_limits: RunLimits) -> None:
    r = run_code("from labkit import value\nvalue('x', float('nan'))",
                 limits=fast_limits)
    assert not r.ok
    assert "chekli" in r.error


def test_legitimate_code_runs(fast_limits: RunLimits) -> None:
    r = run_code(
        "from labkit import value, note, series, table\n"
        "import numpy as np\n"
        "from scipy.linalg import solve\n"
        "A = np.array([[3., 1.], [1., 2.]])\n"
        "x = solve(A, np.array([9., 8.]))\n"
        "value('x0', float(x[0]))\n"
        "value('x1', float(x[1]))\n"
        "note('ishladi')\n"
        "series('s', [1, 2, 3], [1, 4, 9])\n"
        "table('t', ['a', 'b'], [[1, 2]])\n",
        limits=fast_limits)
    assert r.ok, r.error
    assert r.values[0]["value"] == pytest.approx(2.0)
    assert r.values[1]["value"] == pytest.approx(3.0)
    assert len(r.series) == 1 and len(r.tables) == 1


def test_params_reach_the_code(fast_limits: RunLimits) -> None:
    r = run_code("from labkit import PARAMS, value\nvalue('p', PARAMS['k'] * 2)",
                 params={"k": 21.0}, limits=fast_limits)
    assert r.ok and r.values[0]["value"] == pytest.approx(42.0)


def test_error_message_has_no_host_paths(fast_limits: RunLimits) -> None:
    """Xato xabari host fayl tizimini oshkor qilmasligi kerak."""
    r = run_code("from labkit import value\nvalue('x', 1/0)", limits=fast_limits)
    assert not r.ok
    assert "/home/" not in r.error and "site-packages" not in r.error


def test_print_does_not_corrupt_protocol(fast_limits: RunLimits) -> None:
    r = run_code("print('salom')\nfrom labkit import value\nvalue('x', 1)",
                 limits=fast_limits)
    assert r.ok and r.values[0]["value"] == 1.0
    assert "salom" in r.stdout


def test_allowlists_are_identical() -> None:
    """policy.py va policy_inline.py bir xil oq ro'yxatga ega bo'lishi shart."""
    from app.sandbox.policy_inline import ALLOWED_ROOTS as INLINE
    assert ALLOWED_ROOTS == INLINE


def test_policy_accepts_allowed_imports() -> None:
    for mod in sorted(ALLOWED_ROOTS):
        assert check(f"import {mod}").ok, mod
