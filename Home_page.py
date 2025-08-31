from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.hamropatro.com"

    def open(self):
        #Method to open the homepage
        self.driver.get(self.url)

    def click_rashifal(self):
        #Method to click on the Rashifal tab
        rashifal_tab = self.driver.find_element(By.XPATH, "//a[@href='/rashifal']")
        rashifal_tab.click()