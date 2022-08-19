import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_python.Utilities.Baseclass import Baseclass
from selenium_python.pytest_package.Page_object.Homepage import Homepage


class TestOne(Baseclass):
    def teste2e(self):
        log = self.getLogger()
        homepage=Homepage(self.driver)
        Checkout_page=homepage.shopItems()
        log.info("printing card title")
        cards = Checkout_page.getcardTitles()
        #self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        #cards=self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
        i=-1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            log.info(cardText)
            if cardText =="Blackberry":
                Checkout_page.addtoCart()[i].click()
        Checkout_page.checkoutcart().click()
        time.sleep(3)
        Confirm_page=Checkout_page.cart()
        time.sleep(3)
        #Confirmpage=confirmpage(self.driver)
        log.info("entering country name")
        Confirm_page.country().send_keys("ame")
        #self.driver.find_element(By.ID,"country").send_keys("ame")
        #element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"United States of America")))
        self.verifylinkpresence("United States of America")
        Confirm_page.country_text_click().click()
        Confirm_page.checkbox_click().click()
        Confirm_page.submit_btn().click()
        successtext=Confirm_page.success_text().text
        log.info("text matching in"+successtext)
        assert "Success! Thank you!" in successtext
       # self.driver.close()
