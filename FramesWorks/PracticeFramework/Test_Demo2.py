import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Test failed strings do not match"

def test_Creditcard():
    a = 4
    b = 6
    assert a+2 == 6 , "Addition do not match"