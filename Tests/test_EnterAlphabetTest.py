from Pages.Inputs_Page import InputsPage
from Tests.test_base import BaseTest

import time


class Test_EnterAlphabet(BaseTest):

    def test_alphabet_input_number(self):
        self.inputPage = InputsPage(self.driver)
        """open input page"""
        self.driver.get("http://the-internet.herokuapp.com/inputs")

        """type number to test numbers  are  allowed"""
        self.inputPage.typeNumber("aaaa")
        time.sleep(5)
        length = self.inputPage.getValueAttributeLength()
        assert length > 0




