# Any pytest should start with test_ or end with _test
# pytest methods should starts with test
# Any code should be wrapped in method only
# Same repetative  object names should not allowed in Pytest
#Method name should have sense
# -k stands for method names execution, -s logs in output , -v stands for more info metadata
# you can run specific file with py.test <filename>
# Works on CMD ( C:\Users\Srinivas\PycharmProjects\Udemy\FramesWorks/py.test -v -s)
# (path:py.test Test_Demo2.py -v -s) // "(py.test -k CreditCard -v -s) when we need same bank details available in different test cases)"
# You can mark (tag) tests @pytest.mark.smoke and then  run with -m ( in CMD "py.test -m smoke -v -s")
# We use "Skip" for skip the assertionError in TestCases
import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because strings do  not  match"


def test_CreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"
