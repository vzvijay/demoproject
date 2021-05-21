from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator


class InputsPage(BasePage):
    """locators """
    NumberBox = (By.XPATH, "//div/input")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """page based actions"""

    def typeNumber(self, number):
        return self.type(self.NumberBox, number)

    def getValueAttributeLength(self):
        value = self.driver.execute_script("return document.getElementsByTagName('input')[0].value")
        return len(value)
