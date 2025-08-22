import numpy as np
from typing import Iterable, Optional, Tuple

def local_minima(x: Iterable[float],
                 NotCloserThan: Optional[int] = None,
                 LessThan: Optional[float] = None,
                 MaxNumberOfResults: Optional[int] = None
                ) -> Tuple[np.ndarray, np.ndarray]:
    """
    Python translation of MATLAB LocalMinima.m

    Parameters
    ----------
    x : 1D iterable
        Data vector.
    NotCloserThan : int or None
        Minimum spacing (in samples) required between returned minima.
        If None, no spacing constraint is applied.
    LessThan : float or None
        If provided, only consider points with x < LessThan. If None, consider all points.
    MaxNumberOfResults : int or None
        If None or 0: return all minima (after spacing).
        If >0: return up to K smallest minima values (ascending), padding with NaN if fewer found.
        If <0: return up to |K| largest minima values (descending), padding with NaN if fewer found.

    Returns
    -------
    Mins : np.ndarray
        Indices (0-based) of selected minima (possibly padded with NaN if MaxNumberOfResults is set).
    Values : np.ndarray
        Corresponding x-values at those minima (same padding behavior as above).

    Notes
    -----
    - This function mirrors the first (active) implementation block of the MATLAB code (before the early 'return').
    - Indexing is 0-based (Python), not 1-based (MATLAB).
    """

    x = np.asarray(x, dtype=float).ravel()
    nPoints = x.size
    if nPoints == 0:
        if MaxNumberOfResults is None or MaxNumberOfResults == 0:
            return np.array([], dtype=int), np.array([], dtype=float)
        k = abs(MaxNumberOfResults)
        return np.full(k, np.nan), np.full(k, np.nan)

    # only look at those below LessThan
    if LessThan is None:
        BelowThresh = np.arange(nPoints, dtype=int)
    else:
        BelowThresh = np.flatnonzero(x < LessThan).astype(int)

    xBelow = x[BelowThresh]

    # handle gaps due to thresholding (translate MATLAB's [0; idx] / [idx; nPoints+1] to 0-based)
    if BelowThresh.size == 0:
        # No candidates; handle MaxNumberOfResults padding logic at end
        Mins = np.array([], dtype=int)
    else:
        gap_left  = np.flatnonzero(np.diff(np.r_[-1, BelowThresh]) > 1)  # positions in xBelow where a gap starts
        gap_right = np.flatnonzero(np.diff(np.r_[BelowThresh, nPoints]) > 1)

        sDiff = np.sign(np.diff(xBelow))
        LeftSign  = np.r_[1, sDiff]
        RightSign = np.r_[sDiff, -1]

        # apply gap sign overrides
        if gap_left.size:
            LeftSign[gap_left] = -1
        if gap_right.size:
            RightSign[gap_right] = 1

        # replace zero right signs with next non-zero to the right
        zeros = np.flatnonzero(RightSign == 0)
        for i in reversed(zeros.tolist()):
            # safe because we always have appended -1 at end; keep propagating
            RightSign[i] = RightSign[i + 1]

        # local minima among the surviving indices
        mins_mask = (LeftSign < 0) & (RightSign > 0)
        Mins = BelowThresh[np.flatnonzero(mins_mask)]

    # remove minima that are too close to each other
    if NotCloserThan is not None and Mins.size:
        Mins = Mins.astype(int)
        while True:
            too_close = np.flatnonzero(np.diff(Mins) < NotCloserThan)
            if too_close.size == 0:
                break
            # For each close pair, drop the one with the larger value
            left_vals  = x[Mins[too_close]]
            right_vals = x[Mins[too_close + 1]]
            # 0 means drop left, 1 means drop right
            offsets = np.argmax(np.c_[left_vals, right_vals], axis=1)
            delete_idx = np.unique(too_close + offsets)
            Mins = np.delete(Mins, delete_idx)

    # Values handling and optional limiting/padding
    if MaxNumberOfResults is not None and MaxNumberOfResults != 0:
        k = abs(MaxNumberOfResults)
        if Mins.size == 0:
            # return k NaNs for both
            return np.full(k, np.nan), np.full(k, np.nan)

        # sort by value asc/desc
        vals = x[Mins]
        if MaxNumberOfResults > 0:
            order = np.argsort(vals, kind='stable')
        else:
            order = np.argsort(-vals, kind='stable')

        Mins_sorted = Mins[order]
        vals_sorted = vals[order]

        if Mins_sorted.size < k:
            # pad
            M_pad = np.full(k, np.nan)
            V_pad = np.full(k, np.nan)
            M_pad[:Mins_sorted.size] = Mins_sorted
            V_pad[:vals_sorted.size] = vals_sorted
            return M_pad, V_pad
        else:
            return Mins_sorted[:k], vals_sorted[:k]
    else:
        return Mins.astype(float) if Mins.size == 0 else Mins, x[Mins]
