"""Peak/trough detection and cycle helpers."""
import numpy as np

def LocalMinima(x, min_separation=1):
    idx = np.where((x[1:-1] < x[:-2]) & (x[1:-1] < x[2:]))[0] + 1
    if min_separation > 1 and idx.size:
        keep = [idx[0]]
        for i in idx[1:]:
            if i - keep[-1] >= min_separation:
                keep.append(i)
        idx = np.array(keep)
    return idx

def PowerPeakStats(*args, **kwargs):
    raise NotImplementedError

def PhaseFromCycles(*args, **kwargs):
    raise NotImplementedError
