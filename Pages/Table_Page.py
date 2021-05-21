from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator


class TablesPage(BasePage):
    """locators """
    DueColumns = (By.XPATH, "//table[1]/tbody/tr/td[4]")
    DueTheadColumn = (By.XPATH, "//table[1]/thead/tr/th[4]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """page based actions"""
    def getAllDueElement(self):
        return self.getAllElementsText(self.DueColumns)

    def clickOnDueTheadColumn(self):
        self.click(self.DueTheadColumn)
