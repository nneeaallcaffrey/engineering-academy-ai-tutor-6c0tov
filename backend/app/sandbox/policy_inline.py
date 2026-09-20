"""Sandbox ichida ishlatiladigan oq ro'yxat.

`policy.py` dan ALOHIDA fayl, chunki bola jarayonning sys.path'i
qisqartirilgan va u backend paketini import qila olmaydi. Ikkala
ro'yxat bir xil bo'lishi `tests/test_sandbox.py` da tekshiriladi.
"""

ALLOWED_ROOTS = frozenset({
    "labkit", "math", "cmath", "statistics", "fractions", "decimal",
    "itertools", "functools", "operator", "random", "numpy", "scipy",
    "sympy", "collections", "heapq", "bisect", "copy", "typing",
})
