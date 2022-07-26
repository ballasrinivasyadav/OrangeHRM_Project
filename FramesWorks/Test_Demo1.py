# Any code should be wrapped in method only
# Same repetative  object names should not allowed in Pytest
#Method name should have sense
# -k stands for method names execution, -s logs in output , -v stands for more info metadata
# you can run specific file with py.test <filename>
# Works on CMD ( C:\Users\Srinivas\PycharmProjects\Udemy\FramesWorks/py.test -v -s)
# (path:py.test Test_Demo2.py -v -s) // "(py.test -k CreditCard -v -s) when we need same bank details available in different test cases)"
# You can mark (tag) tests @pytest.mark.smoke and then  run with -m ( in CMD "py.test -m smoke -v -s")
# We use "Skip" for skip the assertionError in TestCases
# "Xfail" runs but it not shown Status of PASSES or FAILED in execution (@pytest.mark.xfail) (run by py.test -v -s)
#Fixture are used as setup and tear down methods for test cases- conftest file to generalize
#Fixture and make it available to  all test cases(fixture name into parameters of method)
#Datadriven and parametermization can be done with return statements in List format
#when you define fixture scope to class only, it will run once before class initiated and at the end
#Download from (pytest.html report) pip install pytest-html // (CMD:py.test --html=report.html -s)

import pytest
@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")

@pytest.mark.xfail
def test_CreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])