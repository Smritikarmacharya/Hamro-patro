import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    #Setup for each test
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()