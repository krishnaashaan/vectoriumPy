# VectoriumPy
![License](https://img.shields.io/github/license/krishnaashaan/vectoriumPy)


<p align="center">
  <img src="VectoriumPy/Logo/Vectorium_logo.png" width="500" alt="Vectorium logo">
</p>


VectoriumPy is a lightweight, modular Python library of common physics formulas, helpers, and small simulation utilities for education and quick calculations.

**Goals:** clear, well-tested helpers for kinematics, forces, energy, electricity, waves, magnetism, and thermodynamics.

**Quick start**

Install from PyPI (when published):

```bash
pip install vectoriumPy
```

Install editable from source:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -e .
```

# Usage example:

```python
from vectoriumPy.Kinematics.motion import avg_velocity

v = avg_velocity(50, 10)  # average velocity = displacement / time
print(v)
```

Run the examples:

```bash
python src/vectoriumPy/examples/examples.py
```

Run tests locally:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

# Project layout

- [src/vectoriumPy/](src/vectoriumPy/)
  - `Kinematics/` — motion and projectile utilities
  - `Force/` — force-related formulas
  - `Energy/` — energy helpers
  - `Electricity/` — circuits and electric-field helpers
  - `Waves/` — light and sound calculations
  - `Magnetism/` — magnetic field helpers
  - `Thermodynamics/` — thermodynamics utilities
  - `examples/` — runnable examples
  - `Tests/` — unit tests

# Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a feature branch.
2. Add tests for new functions under [src/vectoriumPy/Tests](src/vectoriumPy/Tests).
3. Open a PR with a clear description of changes.

# License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
