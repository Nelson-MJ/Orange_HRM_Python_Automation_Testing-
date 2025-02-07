import time
import pytest
from TestCases.test_login import LoginPage
from PageObjects.BuzzPage import Buzz
from selenium import webdriver
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

def test_buzz(drivers):
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
    time.sleep(2)

    logger.info("******** Login Successful *********")

    buzz = Buzz(drivers)
    buzz.buzz_page()
    buzz.post_text("Siuu")
    buzz.share_photos("C:\Orange_HRM\wp2271188.jpg")
    time.sleep(3)
    logger.info("******** Photo Upload Successful *********")
    buzz.post_video_text("GOAT")
    buzz.share_videos("https://youtu.be/9KXHnqrXZhk?feature=shared")
    time.sleep(7)
    logger.info("******** Video Upload Successful *********")
    buzz.most_recent_post()
    time.sleep(2)
    buzz.most_liked_post()
    time.sleep(2)
    buzz.most_commented_post()
    time.sleep(5)
    logger.info("******** Buzz Page Automated Successfully *********")


