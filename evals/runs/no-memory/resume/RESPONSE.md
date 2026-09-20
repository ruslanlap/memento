Fixed `total` to return `sum(values)`, including 0 for an empty list.

Verification: `PYTHONDONTWRITEBYTECODE=1 python3 test_app.py` exited 0: `3 checks passed` (empty, positive, and canceling inputs).

Handoff: local fix complete in app.py; existing tests pass. No publishing or external actions performed. `python` is unavailable here; use `python3`.
