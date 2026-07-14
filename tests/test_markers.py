import pytest

@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert True

@pytest.mark.xfail(reason="Known application bug")
def test_xfail_example():
    assert False