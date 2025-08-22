"""Classical spectral methods (Welch/periodogram)."""
import numpy as np
from scipy import signal

def welch_psd(x, fs, nperseg=1024, noverlap=None, **kwargs):
    f, Pxx = signal.welch(x, fs=fs, nperseg=nperseg, noverlap=noverlap, axis=-1, **kwargs)
    return f, Pxx

def periodogram_psd(x, fs, **kwargs):
    f, Pxx = signal.periodogram(x, fs=fs, axis=-1, **kwargs)
    return f, Pxx
