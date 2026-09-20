Not release ready against test_app.py.

`PYTHONDONTWRITEBYTECODE=1 python3 test_app.py` exited 1 with AssertionError at line 3: `total([]) == 0`. Direct checks returned None for [], 5 for [2, 3], and 0 for [-2, 2].

Next: fix the empty-input behavior and rerun the checks before release. Code unchanged; nothing published. Use python3 (`python` is unavailable).
