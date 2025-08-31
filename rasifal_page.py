# from selenium.webdriver.common.by import By

# class RashifalPage:
#     def __init__(self, driver):
#         self.driver = driver

#     def is_tula_visible(self):
#         #Method to check if 'Tula' rashi is visible on the page
#         try:
#             # Locate the Tula rashi text (adjust the XPath based on the actual website's structure)
#             tula_rashi = self.driver.find_element(By.XPATH, "//div[@id='rashifal_tula']")
#             return tula_rashi.is_displayed()
#         except:
#             return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RashifalPage:
    # Updated XPath to match any element containing "तुला"
    TULA_ELEMENT = (By.XPATH, "//*[contains(text(),'तुला')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_tula_visible(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(self.TULA_ELEMENT))
            return element.is_displayed()
        except:
            return False
     