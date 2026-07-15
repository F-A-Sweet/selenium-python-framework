import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_numbers(number):

    print(number)

    assert number > 0