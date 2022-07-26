import pytest
class TestExample:

    @pytest.mark.usefixtures("setup")
    def test_fixture1(self):
        print("I will be executing steps in fixture1 test")

    def test_fixture2(self):
        print("I will be executing steps in fixture2 test")

    def test_fixture3(self):
        print("I will be executing steps in fixture3 test")

    def test_fixture4(self):
        print("I will be executing steps in fixture4 test")