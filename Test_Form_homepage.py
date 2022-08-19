from selenium_python.Utilities.Baseclass import Baseclass
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_python.homepackage_Data import Homepage_Data
from selenium_python.homepackage_Data.Homepage_Data import HomepageData
from selenium_python.pytest_package.Page_object.Homepage import Homepage


class TestHomepage(Baseclass):

    def test_form_submit(self,getdata):
        homepage= Homepage(self.driver)
        homepage.getname().send_keys(getdata["firstname"])
        homepage.getemail().send_keys(getdata["email"])
        homepage.getpassword().send_keys(getdata["password"])
        homepage.clickcheckbox().click()
        self.Selectoptionbytext(homepage.select_gender(),getdata["gender"])

        homepage.submitbtn().click()
        successmsg=homepage.getSuccessMessage().text
        # self.driver.find_element(By.NAME,"name").send_keys("hanika")
        # self.driver.find_element(By.NAME,"email").send_keys("test@test.com")
        # self.driver.find_element(By.ID,"exampleInputPassword1").send_keys("test")
        # self.driver.find_element(By.ID,"exampleCheck1").click()
        # select_gender= Select(self.driver.find_element(By.ID,"exampleFormControlSelect1"))
        # select_gender.select_by_visible_text("Male")
        # self.driver.find_element(By.XPATH,"//input[@value='Submit']").click()
        #successmsg=self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        assert ("Success" in successmsg)
        #assert successmsg == "Success! The Form has been submitted successfully!."
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.getTestData('testcase2'))
    def getdata(self,request):
        return request.param