import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import time

# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="edge")

@pytest.fixture(scope="class")

def setup(request):
    global driver
    # browser_name=request.config.getoption("browser_name")
    # if browser_name == "chrome":
    #     driver=webdriver.Chrome(executable_path="C:\\hanika\\Hanika\\Python+selenium\\drivers\\chromedriver.exe")
    #
    # elif browser_name == "edge":
    #     driver = webdriver.Edge(executable_path="C:\\hanika\\Hanika\\Python+selenium\\drivers\\msedgedriver.exe")
    driver = webdriver.Chrome(executable_path="C:\\hanika\\Hanika\\Python+selenium\\drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()

