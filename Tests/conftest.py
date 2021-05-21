import pytest
from selenium import  webdriver
from Config.Configurator import Configurator

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    if(request.param == "chrome"):
        web_driver=webdriver.Chrome(executable_path=Configurator.CHROME_EXECUTABLE_PATH)
    request.cls.driver=web_driver
    yield
    web_driver.close()