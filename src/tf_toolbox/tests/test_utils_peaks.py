import numpy as np
from tf_toolbox.utils.peaks import LocalMinima

def test_localminima_basic():
    x = np.array([3,2,1,2,3,  3,1,3,  0,1,0])
    idx = LocalMinima(x)
    # known minima at 2, 6, 8, 10 (0-based indexing)
    assert set(idx.tolist()) == {2,6,8,10}
