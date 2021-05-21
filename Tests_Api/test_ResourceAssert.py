import pytest

from Utilities.Utils import Utils
from Config.Configurator import Configurator




class Test_ResourceAssert():

    def test_ResourceAssert(self):
        headers = ''
        response = Utils.makeRequest(Configurator.API_BASE_URL + Configurator.UNKNOWN_API_ENDPOINT, '', headers,'GET')
        result_json = response.json()
        print("response from the get resource api call is " + str(result_json))
        page = result_json["page"]
        id = result_json["data"][1]["id"]
        year = result_json["data"][1]["year"]
        print("page from the response :" + str(page))
        assert page == 1
        print("id from the response : " + str(id))
        assert id == 2
        print("year from the response : " + str(year))
        assert year==2001