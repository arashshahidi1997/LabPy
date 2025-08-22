import numpy as np
from tf_toolbox.spectral.classical import welch_psd, periodogram_psd

def test_welch_psd_shapes(sample_signal):
    fs, x = sample_signal
    f, Pxx = welch_psd(x, fs, nperseg=256)
    assert f.ndim == 1
    assert Pxx.shape[-1] == f.size

def test_periodogram_peak_near_8hz(sample_signal):
    fs, x = sample_signal
    f, Pxx = periodogram_psd(x, fs)
    peak_f = f[Pxx.argmax()]
    assert 7.0 <= peak_f <= 9.0
