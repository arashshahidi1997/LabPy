import numpy as np
import numpy.testing as npt
from base import local_minima

def test_basic_minima():
    x = [3, 2, 4, 1, 5, 0, 6]
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=0)
    npt.assert_array_equal(mins, np.array([1, 3, 5]))
    npt.assert_array_equal(vals, np.array([2.0, 1.0, 0.0]))

def test_spacing_pruning():
    x = [3, 2, 4, 1, 5, 0, 6]
    mins, vals = local_minima(x, NotCloserThan=3, LessThan=None, MaxNumberOfResults=0)
    npt.assert_array_equal(mins, np.array([5]))
    npt.assert_array_equal(vals, np.array([0.0]))

def test_lessthan_filter():
    x = [3, 2, 4, 1, 5, 0, 6]
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=1, MaxNumberOfResults=0)
    npt.assert_array_equal(mins, np.array([5]))
    npt.assert_array_equal(vals, np.array([0.0]))

def test_maxnumber_positive():
    x = [3, 2, 4, 1, 5, 0, 6]
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=2)
    npt.assert_array_equal(mins, np.array([5, 3]))  # 0@5, 1@3
    npt.assert_array_equal(vals, np.array([0.0, 1.0]))

def test_maxnumber_negative():
    x = [3, 2, 4, 1, 5, 0, 6]
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=-2)
    npt.assert_array_equal(mins, np.array([1, 3]))  # 2@1, 1@3 (largest two minima)
    npt.assert_array_equal(vals, np.array([2.0, 1.0]))

def test_padding_when_few_minima():
    x = [1, 0, 1]  # only one minimum at index 1
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=3)
    npt.assert_array_equal(np.isnan(mins), np.array([False, True, True]))
    npt.assert_array_equal(np.isnan(vals), np.array([False, True, True]))
    npt.assert_array_equal(mins[:1].astype(int), np.array([1]))
    npt.assert_array_equal(vals[:1], np.array([0.0]))

def test_empty_input_returns_empty_or_nan():
    x = []
    mins, vals = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=0)
    npt.assert_array_equal(mins, np.array([], dtype=int))
    npt.assert_array_equal(vals, np.array([], dtype=float))

    mins2, vals2 = local_minima(x, NotCloserThan=None, LessThan=None, MaxNumberOfResults=2)
    npt.assert_array_equal(np.isnan(mins2), np.array([True, True]))
    npt.assert_array_equal(np.isnan(vals2), np.array([True, True]))
