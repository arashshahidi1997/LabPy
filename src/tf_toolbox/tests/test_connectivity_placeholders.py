import pytest
from tf_toolbox.connectivity.ccg import CCG

@pytest.mark.xfail(reason="CCG not implemented yet")
def test_ccg_stub():
    CCG(None)  # should raise NotImplementedError once implemented
