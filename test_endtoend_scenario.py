import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_python.Utilities.Baseclass import Baseclass


class TestOne(Baseclass):
    def teste2e(self):

        self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        cards=self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
        i=-1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText =="Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR,".card-footer button")[i].click()


        self.driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("ame")
        element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"United States of America")))
        self.driver.find_element(By.LINK_TEXT,"United States of America").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successtext
       # self.driver.close()
