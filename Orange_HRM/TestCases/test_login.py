import pytest
from selenium import webdriver
import time
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

logger = LogGen.loggen()

@pytest.fixture()
def drivers():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login(drivers):
    logger.info("===== Test Login Started =====")

    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    login_page = LoginPage(drivers)

    login_page.open_page(baseurl)
    time.sleep(1)
    login_page.user_name(username)
    time.sleep(1)
    login_page.pass_word(password)
    time.sleep(1)
    login_page.submit_button()
    time.sleep(1)

    logger.info("******** Login Successful *********")

    login_page.dropdown_click()
    time.sleep(2)
    login_page.logout_click()
    time.sleep(2)

    logger.info("===== Test Login Completed =====")
