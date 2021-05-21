from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator

class LoginPage(BasePage):
    """locators """
    Username = (By.ID, "username")
    Password = (By.ID, "password")
    LoginBtn = (By.XPATH, "//button/i[contains(.,'Login')]")
    InvalidMessage = (By.XPATH, "(//div/div[contains(.,'Your username is invalid')])[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """page based actions"""

    """getting title of the page"""
    def get_login_page_Title(self):
        return self.getTitle()

    """perform login """
    def perform_login(self, username, password):
        self.type(self.Username, username)
        self.type(self.Password, password)
        self.click(self.LoginBtn)

    def getInvalidMessage(self):
        return self.getElementText(self.InvalidMessage)