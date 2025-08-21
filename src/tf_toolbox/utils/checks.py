"""Input/shape checks."""
import numpy as np

def ensure_2d(x):
    x = np.asarray(x)
    return x if x.ndim == 2 else x.reshape(1, -1)
