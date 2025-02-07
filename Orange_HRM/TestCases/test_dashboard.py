import time
import pytest
from PageObjects.DashboardPage import Dashboard
from TestCases.test_login import LoginPage
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

    dash = Dashboard(drivers)
    dash.dashboard_click()
    time.sleep(1)
    dash.time_At_work_button()
    time.sleep(1)
    dash.punch_in_date("2025-10-25")
    time.sleep(1)
    dash.punch_in_time("9:00 AM")
    time.sleep(1)
    dash.punch_in_note("This is a note")
    time.sleep(1)
    dash.punch_in_button()
    time.sleep(2)
    dash.punch_out_date("2026-10-25")
    time.sleep(1)
    dash.punch_out_time("9:00 PM")
    time.sleep(1)
    dash.note("This is a note")
    time.sleep(1)
    dash.out_button()
    time.sleep(3)

    logger.info("******** Time At Work Section Completed *********")

    dash.pending_review()
    time.sleep(2)
    dash.candidate_review()
    time.sleep(1)
    dash.add_button()
    time.sleep(1)
    dash.firstname("Cristiano")
    dash.lastname("Ronaldo")
    dash.vacancy()
    dash.email("ronaldo@gmail.com")
    dash.contact("9876543212")
    dash.resume("C:\Orange_HRM\Resume.txt")
    time.sleep(2)
    dash.keyword("Resume, Name, Role")
    dash.date_of_application("2024-11-10")
    dash.note_of_candidate("this is a note")
    dash.consent()
    dash.save()
    time.sleep(2)

    logger.info("******** Candidate Tab Completed *********")

    dash.vacancy_tab()
    dash.vacancy_name("Ronaldo")
    dash.description("this is a description box")
    time.sleep(2)
    dash.hiring_manager("Ravi M B")
    time.sleep(2)
    dash.number_of_position("6")
    dash.save_candidate()
    time.sleep(2)
    dash.dashboard()
    logger.info("******** Vacancy Tab Completed *********")
    logger.info("******** My Action Section Completed *********")


    dash.assign_leave()
    dash.employee_name("ronaldo")
    time.sleep(1)
    dash.leave_type()
    dash.from_date("2025-01-01")
    dash.to_date("2025-01-08")
    time.sleep(2)
    dash.partial_day()
    time.sleep(2)
    dash.duration()
    dash.assign_button()

    logger.info("******** Assign Leave Completed *********")
    dash.leave_list()
    dash.fromdate("2025-01-08")
    dash.To_Date("2025-01-20")
    dash.leave_status()
    dash.leavetype()
    dash.employee_name_hint("ronaldo")
    dash.search()

    logger.info("******** Leave List Completed*********")


    dash.timesheets()
    dash.employeename("Sagar akhil user")
    dash.view_button()
    time.sleep(2)

    logger.info("******** Timesheet Completed*********")

    dash.apply_leave()
    dash.apply_leave_type()
    dash.leave_from_date("2025-01-08")
    dash.leave_to_date("2025-01-12")
    dash.apply()

    logger.info("******** Apply Leave Completed*********")

    dash.my_leave_button()
    dash.myleave_fromdate("2025-01-12")
    dash.myleave_todate("2025-01-20")
    dash.myleave_status()
    dash.search_myleave()

    logger.info("******** My Leave Completed*********")

    dash.my_timesheet_button()
    dash.timesheet_period_date("2025-03-02 to 2025-09-02")
    dash.timesheet_edit()
    dash.project("Apache Software Foundation - ASF - Phase 1")
    dash.activity()
    dash.enter_time("9:00")
    dash.save_project()


    logger.info("******** My TimeSheet Completed*********")
    logger.info("********Quick Launch Section Completed*********")

    dash.back_dashboard()
    dash.pie_chart_engineering()
    time.sleep(2)
    dash.pie_chart_human_resource()
    time.sleep(2)
    dash.pie_chart_unassigned()
    dash.pie_chart_texas()
    dash.pie_chart_new_york()
    time.sleep(5)

    logger.info("******** Pie Chart Section Completed*********")
    logger.info("******** Dashboard Page Completed*********")