"""Misc DSP helpers."""
import numpy as np

def WhitenSignal(x, eps=1e-6):
    x = np.asarray(x)
    x = (x - x.mean(axis=-1, keepdims=True)) / (x.std(axis=-1, keepdims=True)+eps)
    return x

def PointFFT(*args, **kwargs):
    raise NotImplementedError
