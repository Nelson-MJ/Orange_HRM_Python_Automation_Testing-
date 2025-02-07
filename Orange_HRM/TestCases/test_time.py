import time
import pytest

from PageObjects.TimePage import Time
from TestCases.test_login import LoginPage
from PageObjects.MyInfoPage import Myinfo
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

def test_myinfo(drivers):
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

    timesheet = Time(drivers)
    timesheet.time_page()
    timesheet.employee_name("Sagar akhil user")
    timesheet.view_button()
    time.sleep(2)

    logger.info("******** TimeSheet Tab Completed *********")
    timesheet.timesheet_tab()
    time.sleep(2)
    timesheet.my_timesheet_tab()
    timesheet.timesheet_period_date("2025-03-02 to 2025-09-02")
    timesheet.timesheet_edit()
    timesheet.project("Apache Software Foundation - ASF - Phase 1")
    timesheet.activity()
    timesheet.enter_time("9:00")
    timesheet.save()
    time.sleep(2)

    logger.info("******** MY TimeSheet Tab Completed *********")

    timesheet.attendance_tab()
    time.sleep(1)
    timesheet.my_record_tab()
    timesheet.date_my_record("2025-06-02")
    time.sleep(2)
    timesheet.view_button()
    time.sleep(2)

    logger.info("******** My Record Tab Completed *********")
    timesheet.attendance_tab()
    time.sleep(2)
    timesheet.punch_in_out_tab()
    timesheet.punch_in_date("2025-10-25")
    time.sleep(1)
    timesheet.punch_in_time("9:00 AM")
    time.sleep(1)
    timesheet.punch_in_note("This is a note")
    time.sleep(1)
    timesheet.punch_in_button()
    time.sleep(2)
    timesheet.punch_out_date("2026-10-25")
    time.sleep(1)
    timesheet.punch_out_time("9:00 PM")
    time.sleep(1)
    timesheet.note("This is a note")
    time.sleep(1)
    timesheet.out_button()
    time.sleep(2)

    logger.info("******** Punch In Punch Out Tab Completed *********")


    timesheet.attendance_tab()
    timesheet.employee_record_tab()
    timesheet.employee_name("Ronaldo")
    timesheet.date("2025-06-02")
    timesheet.view_button()
    time.sleep(2)

    logger.info("******** Employee Record Tab Completed *********")

    timesheet.report_tab()
    timesheet.project_report()
    timesheet.project_name("Apache Software Foundation - ASF - Phase 1")
    timesheet.project_from_date("2025-06-02")
    time.sleep(2)
    timesheet.project_to_date("2025-13-02")
    timesheet.view_button()
    time.sleep(2)

    logger.info("******** Project Report Tab Completed *********")
    timesheet.report_tab()
    timesheet.employee_reports()
    time.sleep(2)
    timesheet.employee_name("Ronaldo")
    timesheet.project_name("Apache Software Foundation - ASF - Phase 1")
    timesheet.project_from_date("2025-06-02")
    time.sleep(2)
    timesheet.project_to_date("2025-13-02")
    timesheet.view_button()
    time.sleep(2)

    logger.info("******** Employee Report Tab Completed *********")
    timesheet.project_info_tab()
    timesheet.customer_tab()
    timesheet.add_button()
    timesheet.name("ronaldo")
    timesheet.description("this is a description")
    timesheet.save()
    time.sleep(2)

    logger.info("******** Customer Tab Completed *********")

    timesheet.project_info_tab()
    time.sleep(2)
    timesheet.project_tab()
    timesheet.customer_name("ronaldo")
    time.sleep(2)
    timesheet.name_of_project("ACME Ltd")
    time.sleep(2)
    timesheet.project_admin("Ranga  Akunuri")
    timesheet.search()
    time.sleep(5)

    logger.info("******** Projects Tab Completed *********")
    logger.info("******** Time Page Automated Successfully *********")