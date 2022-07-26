import pytest
from FramesWorks.BaseClass import BaseClass
@pytest.mark.usefixture("dataLoad")
class TestExample(BaseClass):
    def test_editProfile(self,dataLoad):
        self.getlogger()
        log = self.getlogger()
        log.info(dataLoad)
        log.info(dataLoad[2])
        #print(dataLoad)
        print(dataLoad[2])
