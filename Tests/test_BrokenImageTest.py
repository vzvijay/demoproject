from Pages.Broken_Page import BrokenPage
from Tests.test_base import BaseTest
from Utilities.Utils import Utils
from Config.Configurator import Configurator


class Test_BrokenImage(BaseTest):

    def test_broken_images(self):
        headers = ''
        self.brokenPage = BrokenPage(self.driver)
        self.driver.get("http://the-internet.herokuapp.com/broken_images")
        attributes = self.brokenPage.get_img_src_of_brokenpage()
        for value in attributes:
            print(value)
            response = Utils.makeRequest(value, '', headers, 'GET')
            result_json = response.status_code
            print(value + "->>" + str(result_json))
            if (response.status_code != 200):
                assert 404 == response.status_code
