# Physics Lab Simulations

Interactive physics lab simulations built with Python and Streamlit for exploring
core concepts in classical mechanics. Adjust physical parameters with sliders and 
watch the results update in real time. Available in **English and Spanish** with a 
one-click language toggle.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

- 🚀 **Live app:** https://amorenobr.github.io/Lab_Simulations_Python/
- 📖 **Documentation:** https://amorenobr.github.io/Lab_Simulations_Python/docs/

## Simulations

- **Linear Motion** - A particle moving in a straight line with constant acceleration. 
Set the initial position, velocity, acceleration, and time to watch position and 
velocity evolve and read off the final values.
- **Projectile Motion** - Launch a projectile at a chosen speed and angle and 
visualize its trajectory. Computes time of flight, maximum height, and horizontal 
range from the kinematic equations.
- **Damped Harmonic Oscillator** - A mass on a spring. Vary the mass, stiffness, 
and damping to move between undamped, underdamped, critically damped, and overdamped 
motion.

## Getting Started

This project uses [Pixi](https://pixi.sh) to manage its environment and dependencies.

### Install

```bash
git clone https://github.com/amorenobr/Lab_Simulations_Python.git
cd Lab_Simulations_Python
pixi install
```

### Run the app

```bash
pixi run streamlit run Simulations.py
```

Then open the URL shown in the terminal.

## Development

Run the tests:

```bash
pixi run pytest
```

Build the documentation:

```bash
cd docs && pixi run make html
```

The HTML output is written to `docs/build/html`.

## Project Structure

```
Lab_Simulations_Python/
├── Simulations.py                  # Streamlit landing page
├── pages/                          # One file per simulation
├── src/lab_simulations_python/     # Physics engines + i18n (importable package)
├── assets/                         # Logo and static assets
├── tests/                          # Pytest suite
├── docs/                           # Sphinx documentation
└── index.html                      # stlite (WebAssembly) build for GitHub Pages
```

## Tech Stack

- [Streamlit](https://streamlit.io) / [stlite](https://github.com/whitphx/stlite) — user interface
- [NumPy](https://numpy.org) — numerical computation
- [Plotly](https://plotly.com/python/) — interactive plots
- [Sphinx](https://www.sphinx-doc.org) — documentation
- [Pixi](https://pixi.sh) — environment management

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Author

Alexander Moreno Briceño - Universidad Antonio Nariño
