"""TF Toolbox (Python): time–frequency analysis utilities.

This package is a Pythonic, faithful reimplementation of MATLAB's TF directory.
See README.md for goals and conventions.

Subpackages:
- utils
- spectral
- timefreq
- connectivity
- oscillations
- states
- plotting
"""
from . import utils, spectral, timefreq, connectivity, oscillations, states, plotting
from .utils.find_funcion import find_function

# Create an alias so it can be called as mypackage.find
find = find_function