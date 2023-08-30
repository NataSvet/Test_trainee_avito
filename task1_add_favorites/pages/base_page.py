
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class BasePage():
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator),message=f"Элемент не кликабален локатор {locator}")
    
    def presence_of_element_located(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator), message=f"Не найден элемент по локатору{locator}")
    
    def visibility_of_element_located(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator), message=f"Не найден элемент с локатором {locator}")

        
    
