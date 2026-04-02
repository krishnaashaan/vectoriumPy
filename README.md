# VectoriumPy

<p align="center">
  <img src="VectoriumPy/Logo/Vectorium_logo.png" width="200">
</p>

VectoriumPy is a small, modular Python library of common physics formulas, helpers, and lightweight simulation utilities aimed at education, quick calculations, and small-scale experiments.

Project status: This repository contains the result of an intensive one-month development effort to gather, implement, and test compact physics utilities and examples. The codebase was created and refined over a single month with the goal of providing clear, well-tested helpers for teaching and experimentation.

I plan to add way more functions in the future

## Quick summary

- Lightweight functions for kinematics, forces, energy, electricity, waves, and a few example scripts.
- Well-suited for notebooks, teaching demos, and short scripts — not a full physics engine.

## Install
 IT should be avaliable to install in a couple of Months
Install editable from source:

```bash
pip install -e .
```

Recommended: create and activate a virtual environment before installing.

## Usage (quick)

Run the example scripts or import modules from the package. Example from a Python REPL:

```python
from VectoriumPy.Kinematics.motion import  avg_velocity
avg_v =  avg_velocity(50,50)
print(avg_v)
```

See [src/VectoriumPy/examples/examples.py](src/VectoriumPy/examples/examples.py) for runnable examples.

## Project layout

- [src/VectoriumPy/](src/VectoriumPy/)
  - `Kinematics/` — motion and projectile utilities
  - `Force/` — force-related formulas (gravity, friction, centripetal)
  - `Energy/` — kinetic, potential and mechanical energy helpers
  - `Electricity/` — circuits, capacitance, electric field helpers
  - `Waves/` — basic light and sound calculations
  - `Thermodynamics/`- Calculations related to thermodynamics
  - `examples/` — small runnable examples showing common usage
  - `Tests/` — unit tests for core functions

## Tests

Run tests with pytest from the repository root:

```bash
python -m pytest -q
```

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a feature branch.
2. Add tests for new functions under [src/VectoriumPy/Tests](src/VectoriumPy/Tests).
3. Open a PR with a clear description of changes.

## License

See [LICENSE](LICENSE) for license terms.

## Files explained (key modules)

This project contains a set of focused modules. Brief descriptions of the main files:

- [src/VectoriumPy/Kinematics/motion.py](src/VectoriumPy/Kinematics/motion.py): Common kinematics helpers (velocity, acceleration, displacement calculations).
- [src/VectoriumPy/Kinematics/projectile_motion.py](src/VectoriumPy/Kinematics/projectile_motion.py): Projectile motion utilities (range, time of flight, max height).
- [src/VectoriumPy/Force/Force.py](src/VectoriumPy/Force/Force.py): Force calculations (gravitational force, friction, centripetal force).
- [src/VectoriumPy/Energy/energy.py](src/VectoriumPy/Energy/energy.py): Energy-related helpers (kinetic, potential, mechanical energy, work, power).
- [src/VectoriumPy/Electricity/electricity.py](src/VectoriumPy/Electricity/electricity.py): Basic electricity formulas (Ohm's law, power, energy in circuits).
- [src/VectoriumPy/Electricity/circuit.py](src/VectoriumPy/Electricity/circuit.py): Series/parallel resistance and simple circuit helpers.
- [src/VectoriumPy/Electricity/electric_fields.py](src/VectoriumPy/Electricity/electric_fields.py): Electric field and point-charge helpers.
- [src/VectoriumPy/Waves/light.py](src/VectoriumPy/Waves/light.py): Light/wave optics helpers (wavelength, frequency relations).
- [src/VectoriumPy/Waves/sound.py](src/VectoriumPy/Waves/sound.py): Sound-wave calculations (speed, Doppler shift basics).
- [src/VectoriumPy/Thermodynamics/Thermodynamics.py](src/VectoriumPy/Thermodynamics/Thermodynamics.py): Calculations related to Thermodynamics(- First Law of Thermodynamics
- Entropy, Enthalpy, Gibbs free energy, Helmholtz Free Energy, Ideal Gas Law)
- [src/VectoriumPy/examples/examples.py](src/VectoriumPy/examples/examples.py): Small example scripts demonstrating library usage.
- [src/VectoriumPy/Tests/](src/VectoriumPy/Tests/): Unit tests covering core functions.
