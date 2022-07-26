import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last ")

@pytest.fixture()
def dataLoad():
    print("I will print later")
    return ["Anushka","Shetty","AnushkaShettyAcademy"]

@pytest.fixture(params= [("chrome","Shetty"),("Firefox","Anushka"),("IE","ss")])
def crossBrowser(request):
    return request.param

