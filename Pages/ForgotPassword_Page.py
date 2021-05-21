from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator


class ForgotPassword(BasePage):
    """locators """
    Email = (By.ID, "email")
    RetrivePasswordBtn = (By.XPATH, "//form/button/i[contains(.,'Retrieve password')]")
    ForgotPasswordText = (By.XPATH, "//div/h2")
    InternalServerErrorMessage = (By.XPATH , "//h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """forgot password page based actions"""

    def typeemail(self, email):
        return self.type(self.Email, email)

    """perform login """
    def clickOnRetrivePasswordBtn(self):
        self.click(self.RetrivePasswordBtn)

    def getForgotPassworText(self):
        return self.getElementText(self.ForgotPasswordText)

    def getErrorMessage(self):
        return self.getElementText(self.InternalServerErrorMessage)