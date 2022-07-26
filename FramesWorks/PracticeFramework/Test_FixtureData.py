import pytest

from FramesWorks.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample1(BaseClass):
    def test_editProfile(self,dataContain):
        log = self.getlogger()
        log.info(dataContain[0])
        log.info(dataContain[1])
        print(dataContain[2])

