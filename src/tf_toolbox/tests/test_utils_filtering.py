import numpy as np
import pytest
from tf_toolbox.utils.filtering import ButFilter, FirFilter, Filter0

def test_butfilter_bandpass_shape(sample_signal):
    fs, x = sample_signal
    y = ButFilter(x, fs=fs, band=(6,12), order=4, btype='bandpass')
    assert y.shape == x.shape

def test_butfilter_lowpass_reduces_high_freq(sample_signal):
    fs, x = sample_signal
    y = ButFilter(x, fs=fs, band=15, order=4, btype='lowpass')
    # crude energy comparison above/below cutoff
    X = np.fft.rfft(x)
    Y = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(x.size, 1/fs)
    high = freqs > 30
    assert np.abs(Y[high]).mean() < np.abs(X[high]).mean()

def test_filter0_identity_stability(sample_signal):
    fs, x = sample_signal
    # identity IIR (b=[1], a=[1]); Filter0 should return x unchanged
    y = Filter0([1.0], [1.0], x)
    assert np.allclose(x, y)
