from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Configurator import Configurator
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class NotificationPage(BasePage):
    """locators """
    ClickHereLink = (By.XPATH, "//div/p/a[contains(.,'Click here')]")
    ActionSuccessFullText = (By.XPATH, "(//div[contains(@id,'flash')])[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configurator.BASE_URL)

    """page based actions"""

    def clickOnClickHere(self):
        return self.click(self.ClickHereLink)

    def getActionSuccessFullText(self):
        return self.getElementText(self.ActionSuccessFullText)

    def loopedScript(self):
        print("here")
        notification = ''
        print(notification)
        count = 1
        while 'Action successful' not in notification:
            print(notification)
            count: count + 1
            print(count)
            self.clickOnClickHere()
            time.sleep(2)
            try:
                notification = self.getActionSuccessFullText()
            except TimeoutException:
                time.sleep(2)
            if count == 10:
                break
        print(notification)
        assert 'Action successful' in notification