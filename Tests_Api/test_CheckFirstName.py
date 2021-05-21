
from Utilities.Utils import Utils
from Config.Configurator import Configurator


class Test_FirstName():
    def test_FirstName(self):
        headers = ''
        response = Utils.makeRequest(Configurator.API_BASE_URL + Configurator.USERS_2_ENDPOINT, '', headers, 'GET')
        result_json = response.json()
        data = result_json["data"]['first_name']
        print(data)
        assert data == 'John'