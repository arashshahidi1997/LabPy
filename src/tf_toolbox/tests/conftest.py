import numpy as np
import pytest

@pytest.fixture
def rng():
    return np.random.default_rng(0)

@pytest.fixture
def sample_signal(rng):
    fs = 1250.0
    t = np.arange(0, 2.0, 1/fs)  # 2 s
    x = np.sin(2*np.pi*8*t) + 0.5*np.sin(2*np.pi*40*t) + 0.1*rng.standard_normal(t.size)
    return fs, x

@pytest.fixture
def two_channel_signal(sample_signal):
    fs, x = sample_signal
    y = 0.5*x + 0.05*np.roll(x, 3)
    XY = np.vstack([x, y])
    return fs, XY
