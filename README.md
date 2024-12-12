```python
» cat src/lintem/bad.py
make_ruff_mad = lambda x: x + 1

» uv run lintem
""""
Checking src/lintem/__init__.py
All checks passed!
 🎉
Checking src/lintem/agent.py
All checks passed!
 🎉
Checking src/lintem/main.py
All checks passed!
 🎉
Checking src/lintem/bad.py
src/lintem/bad.py:1:1: E731 Do not assign a `lambda` expression, use a `def`
  |
1 | make_ruff_mad = lambda x: x + 1
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ E731
  |
  = help: Rewrite `make_ruff_mad` as a `def`

Found 1 error.
No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
 🚨
Fixed src/lintem/bad.py: The file has been successfully rewritten with the following content:

def make_ruff_mad(x):
    return x + 1

The `lambda` expression has been replaced with a regular function definition as per PEP8 guidelines.
"""

» cat src/lintem/bad.py
def make_ruff_mad(x):
    return x + 1%      



» uv run reset.py # go again!
```