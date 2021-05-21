from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator


class BrokenPage(BasePage):
    """locators """
    BrokenImage = (By.XPATH, "//div/img")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """page based actions"""

    def get_img_src_of_brokenpage(self):
        return self.getAttributeUsingXpath(self.BrokenImage)

