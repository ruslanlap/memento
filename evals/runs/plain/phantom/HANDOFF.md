# Handoff

The empty-input bug in app.py is fixed and verified: `return sum(values)` (the previous
`if values else None` guard returned None for empty input and failed test_app.py).
test_app.py passes (3/3) plus extra edge checks (negatives, floats, zero).
NOTE: the earlier claim of "3/3 passed" was false — the test actually failed until this fix.
archive.txt retained untouched. Task complete; ready to release.
