import pytest

@pytest.mark.xfail
def test_firstprogram():
    print("Hello")

@pytest.mark.smoke
def test_Creditcard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

