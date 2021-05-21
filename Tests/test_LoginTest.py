from Pages.Login_Page import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    def test_form_valdation_login_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.driver.get("http://the-internet.herokuapp.com/login")
        self.loginPage.perform_login("test", "test")
        assert  "Your username is invalid!" in self.loginPage.getInvalidMessage()
