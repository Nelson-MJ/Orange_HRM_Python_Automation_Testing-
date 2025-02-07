from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

class Time:
    def __init__(self,driver):
        self.driver = driver
        self.time_page_by = By.XPATH
        self.time_page_value = "//span[text() = 'Time']"
        self.employeename_by = By.XPATH
        self.employeename_value = "//label[text()='Employee Name']/following::input[1]"
        self.view_by = By.XPATH
        self.view_value = "(//button[@type='submit' and contains(., 'View')])[1]"
        self.timesheet_tab_by = By.XPATH
        self.timesheet_tab_value = "//span[text() = 'Timesheets ']"
        self.myTimesheet_by = By.XPATH
        self.myTimesheet_value = "//a[text() = 'My Timesheets']"
        self.timesheet_period_by = By.XPATH
        self.timesheet_period_value = "//p[text()='Timesheet Period']/following::input[@class='oxd-input oxd-input--active']"
        self.timesheet_edit_by = By.XPATH
        self.timesheet_edit_value = "//button[@type='button' and contains(@class, 'oxd-button--ghost') and text()=' Edit ']"
        # self.submit_by = By.XPATH
        # self.submit_value  = "//button[text()=' Submit ']"
        self.project_by = By.XPATH
        self.project_value = "//th[contains(text(), 'Project')]/following::input[@placeholder='Type for hints...']"
        self.activitydropdown_by = By.XPATH
        self.activitydropdown_value = "//th[contains(text(), 'Activity')]/following::i[contains(@class, 'oxd-icon bi-caret-down-fill')][1]"
        self.enter_time_by = By.XPATH
        self.enter_time_value = "//td[contains(@class, 'orangehrm-timesheet-table-body-cell') and contains(@class, '--duration-input')]//input[contains(@class, 'oxd-input')]"
        self.save_project_by = By.XPATH
        self.save_project_value = "//button[text()=' Save ']"
        self.attendance_tab_by = By.XPATH
        self.attendance_tab_value = "//span[text()='Attendance ']"
        self.myRecord_tab_by = By.XPATH
        self.myRecord_tab_value = "//a[text()='My Records']"
        self.date_myRecord_by = By.XPATH
        self.date_myRecord_value = "//label[text()='Date']/following::input[1]"
        self.punchInOut_tab_by = By.XPATH
        self.punchInOut_tab_value = "//a[text()='Punch In/Out']"
        self.punchin_date_by = By.XPATH
        self.punchin_date_value = "//label[text()='Date']/following::input[1]"
        self.punchin_time_by = By.XPATH
        self.punchin_time_value = "//label[text()='Time']/following::input[1]"
        self.Note_by = By.XPATH
        self.Note_value = "//textarea[@placeholder='Type here']"
        self.In_by = By.XPATH
        self.In_value = "//button[text()=' In ']"
        self.punchout_date_by = By.XPATH
        self.punchout_date_value = "//label[text()='Date']/following::input[1]"
        self.punchout_time_by = By.XPATH
        self.punchout_time_value = "//label[text()='Time']/following::input[1]"
        self.Note_by = By.XPATH
        self.Note_value = "//textarea[@placeholder='Type here']"
        self.out_by = By.XPATH
        self.out_value = "//button[text()=' Out ']"
        self.employee_record_by = By.XPATH
        self.employee_record_value = "//a[text() = 'Employee Records']"
        self.date_by = By.XPATH
        self.date_value = "//label[text()='Date']/following::input[1]"
        self.reportTab_by = By.XPATH
        self.reportTab_value = "//span[text() = 'Reports ']"
        self.projectReports_by = By.XPATH
        self.projectReports_value = "//a[text() = 'Project Reports']"
        self.project_name_by = By.XPATH
        self.project_name_value = "//label[text()='Project Name']/following::input[1]"
        self.projectDateFrom_by = By.XPATH
        self.projectDateFrom_value = "//label[text()='Project Date Range']/following::input[@placeholder='From'][1]"
        self.projectDateTo_by = By.XPATH
        self.projectDateTo_value = "//label[text()='Project Date Range']/following::input[@placeholder='To'][1]"
        self.employeeReportsTab_by = By.XPATH
        self.employeeReportsTab_value = "//a[text() = 'Employee Reports']"
        self.project_infoTab_by = By.XPATH
        self.project_infoTab_value = "//span[text() = 'Project Info ']"
        self.customer_tab_by = By.XPATH
        self.customer_tab_value = "//a[text() = 'Customers']"
        self.add_by = By.XPATH
        self.add_value = "//button[text() = ' Add ']"
        self.name_by = By.XPATH
        self.name_value = "//label[text()='Name']/following::input[1]"
        self.description_by = By.XPATH
        self.description_value = "//label[text()='Description']/following::textarea[1]"
        self.projectsTab_by = By.XPATH
        self.projectsTab_value = "//a[@role='menuitem' and text()='Projects']"
        self.customer_name_by = By.XPATH
        self.customer_name_value = "//label[text()='Customer Name']/following::input[1]"
        self.projects_by = By.XPATH
        self.projects_value = "//label[text()='Project']/following::input[1]"
        self.project_admin_by = By.XPATH
        self.project_admin_value = "//label[text()='Project Admin']/following::input[1]"
        self.search_by = By.XPATH
        self.search_value = "//button[text() = ' Search ']"


    def time_page(self):
        self.driver.find_element(self.time_page_by,self.time_page_value).click()
    def employee_name(self,name):
        element= self.driver.find_element(self.employeename_by,self.employeename_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def view_button(self):
        self.driver.find_element(self.view_by,self.view_value).click()
    def timesheet_tab(self):
        self.driver.find_element(self.timesheet_tab_by,self.timesheet_tab_value).click()
    def my_timesheet_tab(self):
        self.driver.find_element(self.myTimesheet_by,self.myTimesheet_value).click()
    def timesheet_period_date(self,date):
        element = self.driver.find_element(self.timesheet_period_by,self.timesheet_period_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def timesheet_edit(self):
        self.driver.find_element(self.timesheet_edit_by,self.timesheet_edit_value).click()
    # def submit_button(self):
    #     self.driver.find_element(self.submit_by,self.submit_value).click()
    def project(self,name):
        element = self.driver.find_element(self.project_by, self.project_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def activity(self):
        self.driver.find_element(self.activitydropdown_by,self.activitydropdown_value).click()
    def enter_time(self,text):
        element = self.driver.find_element(self.enter_time_by,self.enter_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def save(self):
        self.driver.find_element(self.save_project_by, self.save_project_value).click()
    def attendance_tab(self):
        self.driver.find_element(self.attendance_tab_by,self.attendance_tab_value).click()
    def my_record_tab(self):
        self.driver.find_element(self.myRecord_tab_by,self.myRecord_tab_value).click()
    def date_my_record(self,date):
        element = self.driver.find_element(self.date_myRecord_by, self.date_myRecord_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def punch_in_out_tab(self):
        self.driver.find_element(self.punchInOut_tab_by,self.punchInOut_tab_value).click()
    def punch_in_date(self,date):
        element = self.driver.find_element(self.punchin_date_by, self.punchin_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def punch_in_time(self,text):
        element = self.driver.find_element(self.punchin_time_by,self.punchin_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def punch_in_note(self,note):
        self.driver.find_element(self.Note_by,self.Note_value).send_keys(note)
    def punch_in_button(self):
        self.driver.find_element(self.In_by,self.In_value).click()
    def punch_out_date(self,date):
        element = self.driver.find_element(self.punchout_date_by, self.punchout_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def punch_out_time(self,text):
        element = self.driver.find_element(self.punchout_time_by,self.punchout_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def note(self,note):
        self.driver.find_element(self.Note_by,self.Note_value).send_keys(note)
    def out_button(self):
        self.driver.find_element(self.out_by,self.out_value).click()
    def employee_record_tab(self):
        self.driver.find_element(self.employee_record_by,self.employee_record_value).click()
    def date(self,date):
         element = self.driver.find_element(self.date_by, self.date_value)
         element.send_keys(Keys.CONTROL + "a")
         element.send_keys(Keys.BACKSPACE)
         element.send_keys(date)
    def report_tab(self):
        self.driver.find_element(self.reportTab_by,self.reportTab_value).click()
    def project_report(self):
        self.driver.find_element(self.projectReports_by,self.projectReports_value).click()
    def project_name(self,name):
        element = self.driver.find_element(self.project_name_by,self.project_name_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def project_from_date(self,date):
        element = self.driver.find_element(self.projectDateFrom_by,self.projectDateFrom_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def project_to_date(self,date):
        element = self.driver.find_element(self.projectDateTo_by,self.projectDateTo_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def employee_reports(self):
        self.driver.find_element(self.employeeReportsTab_by,self.employeeReportsTab_value).click()
    def project_info_tab(self):
        self.driver.find_element(self.project_infoTab_by,self.project_infoTab_value).click()
    def customer_tab(self):
        self.driver.find_element(self.customer_tab_by,self.customer_tab_value).click()
    def add_button(self):
        self.driver.find_element(self.add_by,self.add_value).click()
    def name(self,name):
        element = self.driver.find_element(self.name_by, self.name_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def description(self,text):
        element = self.driver.find_element(self.description_by, self.description_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def project_tab(self):
        self.driver.find_element(self.projectsTab_by,self.projectsTab_value).click()
    def customer_name(self,name):
        element = self.driver.find_element(self.customer_name_by,self.customer_name_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def name_of_project(self,name):
        element = self.driver.find_element(self.projects_by,self.projects_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)

    def project_admin(self,name):
        element = self.driver.find_element(self.project_admin_by, self.project_admin_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def search(self):
        self.driver.find_element(self.search_by,self.search_value).click()



