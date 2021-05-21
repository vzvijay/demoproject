from Pages.ForgotPassword_Page import ForgotPassword
from Tests.test_base import BaseTest

class Test_ForgotPassword(BaseTest):
    """ i m validing message after click on retrive password since i m getting internal server error """
    def test_forgotPasswordfuntionality(self):
        self.forgotpassword_page = ForgotPassword(self.driver)

        """redirect to forgot password page"""
        self.driver.get("http://the-internet.herokuapp.com/forgot_password")

        """validate landed on forgot password page"""
        assert "Forgot Password" in self.forgotpassword_page.getForgotPassworText()

        """enter email in email input box to retriver password"""
        self.forgotpassword_page.typeemail("test@gmail.com")

        """click on retrive password btn"""
        self.forgotpassword_page.clickOnRetrivePasswordBtn()

        """validate error message"""
        assert  "Internal Server Error" in self.forgotpassword_page.getErrorMessage()
