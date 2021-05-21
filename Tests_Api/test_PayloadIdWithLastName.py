import pytest

from Utilities.Utils import Utils
from Config.Configurator import Configurator


class Test_PayloadWithLastName():

    def test_PayloadWithLastName(self):
        headers = ''
        response = Utils.makeRequest(Configurator.API_BASE_URL + Configurator.USERS_PAGE_2_ENDPOINT, '', headers, 'GET')
        result_json = response.json()
        data = result_json["data"]
        id_result = list(map(lambda x: int(x["id"]), data))
        print(id_result)
        assert 7 in id_result
        lastname_result = list(map(lambda x: str(x["last_name"]), data))
        print(lastname_result)
        assert "Lawson" in lastname_result
