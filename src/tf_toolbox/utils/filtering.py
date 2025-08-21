"""Filtering helpers used throughout the toolbox."""
import numpy as np
from scipy import signal

def ButFilter(x, fs, band, order=4, btype='bandpass'):
    """Butterworth filter wrapper (MATLAB parity)."""
    ny = 0.5 * fs
    if isinstance(band, (list, tuple)):
        Wn = [b/ny for b in band]
    else:
        Wn = band/ny
    b, a = signal.butter(order, Wn, btype=btype)
    return signal.filtfilt(b, a, x, axis=-1)

def Filter0(b, a, x):
    """Zero-phase IIR (filtfilt) wrapper."""
    from scipy.signal import filtfilt
    return filtfilt(b, a, x, axis=-1)

def FirFilter(x, taps):
    """FIR filtering via convolution."""
    return np.apply_along_axis(lambda s: np.convolve(s, taps, mode='same'), -1, x)

def AdaptiveFilter(*args, **kwargs):
    raise NotImplementedError("Port from MATLAB pending.")

def MTFilter(*args, **kwargs):
    raise NotImplementedError("Helper for multitaper pipelines pending.")
