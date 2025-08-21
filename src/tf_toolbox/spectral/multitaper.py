"""Multitaper spectral estimators."""
import numpy as np
from scipy import signal

def mtparam(*args, **kwargs):  # MATLAB: mtparam / mtparamEd
    raise NotImplementedError

def mtfft(*args, **kwargs):
    raise NotImplementedError

def mtcsd(*args, **kwargs):  # cross-spectral density
    raise NotImplementedError

def mtcsdfast(*args, **kwargs):
    raise NotImplementedError

def mtcsdlong(*args, **kwargs):
    raise NotImplementedError

def mtcsdglong(*args, **kwargs):
    raise NotImplementedError

def mtchd(*args, **kwargs):  # coherence density
    raise NotImplementedError

def mtchdfast(*args, **kwargs):
    raise NotImplementedError

def mtchglong(*args, **kwargs):
    raise NotImplementedError

def mtptcsd(*args, **kwargs):  # point-process csd
    raise NotImplementedError

def mtptchd(*args, **kwargs):  # point-process coherence
    raise NotImplementedError
