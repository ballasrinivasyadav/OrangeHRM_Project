import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataContain():
    print("User profile data being created")
    return ["Sri","Nivasa","SRINIVASA.COM"]

@pytest.fixture(params=("chrome","Anushka","Shetty"))
def crossBrowser(request):
    return request.param


