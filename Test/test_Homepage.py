import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from PageObjects.Homepage import Homepage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log= self.getLogger()
        homepage = Homepage(self.driver)
        log.info('getting personal information')
        homepage.getName().send_keys(getData["Firstname"])
        homepage.getemail().send_keys(getData["Lastname"])
        homepage.getCheckBox().click()
        self.selectOptionsByText(homepage.getGender(),getData["Gender"])
        homepage.submitForm().click()
        log.info('get success message')
        alertText = homepage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestaData("Testcase2"))
    def getData(self,request):
        return request.param