from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Dashboard:
    def __init__(self,driver):
        self.driver = driver
        self.dashboard_by = By.LINK_TEXT
        self.dashboard_value = "Dashboard"
        self.timeatwork_by = By.XPATH
        self.timeatwork_value = "//button[@class='oxd-icon-button oxd-icon-button--solid-main orangehrm-attendance-card-action']/i[@class='oxd-icon bi-stopwatch']"
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
        self.pending_review_by = By.XPATH
        self.pending_review_value = "//p[text()='(1) Pending Self Review']"
        self.candidate_by = By.XPATH
        self.candidate_value = "//p[text()='(1) Candidate to Interview']"
        self.add_button_by = By.XPATH
        self.add_button_value = "//i[@class='oxd-icon bi-plus oxd-button-icon']"
        self.firstname_by = By.NAME
        self.firstname_value = "firstName"
        self.lastname_by = By.NAME
        self.lastname_value = "lastName"
        self.vacancydropdown_by = By.XPATH
        self.vacancydropdown_value = "//i[contains(@class, 'bi-caret-down-fill') and contains(@class, 'oxd-select-text--arrow')]"
        self.vacancy_select_by = By.XPATH
        self.vacancy_select_value =  "//div[@class='oxd-select-text-input' and text()='-- Select --']"
        self.email_by = By.XPATH
        self.email_value = "//label[text()='Email']/following::input[1]"
        self.contact_by = By.XPATH
        self.contact_value = "//label[text()='Contact Number']/following::input[1]"
        self.resume_by = By.XPATH
        self.resume_value = "//input[@type='file']"
        self.keywords_by = By.XPATH
        self.keywords_value = "//label[text()='Keywords']/following::input[1]"
        self.application_date_by = By.XPATH
        self.application_date_value = "//label[text()='Date of Application']/following::input[1]"
        self.candidatenote_by = By.XPATH
        self.candidatenote_value = "//label[text()='Notes']/following::input[1]"
        self.consent_by = By.XPATH
        self.consent_value = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
        self.save_by = By.XPATH
        self.save_value = "//button[text()=' Save ']"
        self.vacancy_button_by = By.XPATH
        self.vacancy_button_value = "//a[text() = 'Vacancies']"
        self.add_vacancy_by = By.XPATH
        self.add_vacancy_value = "//button[text() = ' Add ']"
        self.vacancy_name_by = By.XPATH
        self.vacancy_name_value = "//label[text()='Vacancy Name']/following::input[1]"
        self.job_titledropdown_by = By.XPATH
        self.job_titledropdown_value  = "//div[contains(@class, 'oxd-select-text-input')]"
        self.job_title_by = By.XPATH
        self.job_title_value = "//div[@role='listbox']//div[normalize-space(text())='Chief Executive Officer']"
        self.description_by = By.XPATH
        self.description_value = "//textarea[@placeholder='Type description here']"
        self.hiring_manager_by = By.XPATH
        self.hiring_manager_value = "//label[text()='Hiring Manager']/following::input[1]"
        self.no_of_position_by = By.XPATH
        self.no_of_position_value = "//label[text()='Number of Positions']/following::input[1]"
        self.save_candidate_by = By.XPATH
        self.save_candidate_value = "//button[text() = ' Save ']"
        self.assign_leave_By = By.XPATH
        self.assign_leave_value = "//button[@title='Assign Leave' and @type='button']"
        self.employee_name_by = By.XPATH
        self.employee_name_value = "//label[text()='Employee Name']/following::input[1]"
        self.leavetypedropdown_by = By.XPATH
        self.leavetypedropdown_value = "//i[contains(@class, 'oxd-icon') and contains(@class, 'bi-caret-down-fill') and contains(@class, 'oxd-select-text--arrow')]"
        self.leave_select_by = By.XPATH
        self.leave_select_value = "//div[@class='oxd-select-text-input' and text()='-- Select --']"
        self.fromdate_by = By.XPATH
        self.fromdate_value  = "//label[text()='From Date']/following::input[1]"
        self.todate_by = By.XPATH
        self.todate_value = "//label[text()='To Date']/following::input[1]"
        self.partialdays_dropdown_by = By.XPATH
        self.partialdays_dropdown_value = "//div[@class='oxd-select-text-input' and text()='All Days']"
        self.partial_select_by = By.XPATH
        self.partial_select_value = "//label[text()='Duration']/following::div[@class='oxd-select-text-input' and text()='Full Day']"
        self.durationdropdown_by = By.XPATH
        self.durationdropdown_value = "//label[text()='Duration']/following::i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
        self.duration_select_by = By.XPATH
        self.duration_select_value = "//label[text()='Duration']/following::div[@class='oxd-select-text-input' and text()='Full Day']"
        self.assign_by = By.XPATH
        self.assign_value = "//button[text()=' Assign ']"
        self.leave_list_By = By.XPATH
        self.leave_list_value = "//button[@class='oxd-icon-button orangehrm-quick-launch-icon' and @type='button' and @title='Leave List']"
        self.from_by = By.XPATH
        self.from_value = "//label[text()='From Date']/following::input[1]"
        self.to_date_by = By.XPATH
        self.to_date_value = "//label[text()='To Date']/following::input[1]"
        self.leave_statusdropdown_by = By.XPATH
        self.leave_statusdropdown_value = "(//div[@class='oxd-select-text-input' and text()='-- Select --'])[1]"
        self.leave_status_by = By.XPATH
        self.leave_status_value = "(//span[text()='Rejected'])[1]"
        self.leave_typedropdown_by = By.XPATH
        self.leave_typedropdown_value = "(//div[@class='oxd-select-text-input' and text()='-- Select --'])[2]"
        self.leavetype_by = By.XPATH
        self.leavetype_value = "//div[@role='listbox']//span[text()='CAN - Vacation']"
        self.employee_hint_by = By.XPATH
        self.employee_hint_value = "//label[text()='Employee Name']/following::input[1]"
        self.search_by = By.XPATH
        self.search_value = "//button[text()=' Search ']"
        self.timesheets_by = By.XPATH
        self.timesheets_value = "//button[@class='oxd-icon-button orangehrm-quick-launch-icon' and @title='Timesheets']"
        self.employeename_by = By.XPATH
        self.employeename_value = "//label[text()='Employee Name']/following::input[1]"
        self.view_by = By.XPATH
        self.view_value = "(//button[@type='submit' and contains(., 'View')])[1]"
        self.apply_leave_by = By.XPATH
        self.apply_leave_value = "//button[@title='Apply Leave']"
        self.Leave_typedropdown_by = By.XPATH
        self.Leave_typedropdown_value = "(//div[@class='oxd-select-text-input' and text()='-- Select --'])[1]"
        self.Leave_type_by = By.XPATH
        self.Leave_type_value = "//div[@role='listbox']//span[text()='CAN - Bereavement']"
        self.Fromdate_by = By.XPATH
        self.Fromdate_value = "//label[text()='From Date']/following::input[1]"
        self.To_date_by = By.XPATH
        self.To_date_value = "//label[text()='To Date']/following::input[1]"
        self.apply_by = By.XPATH
        self.apply_value = "//button[text() = ' Apply ']"
        self.myleave_by = By.XPATH
        self.myleave_value = "//button[@class='oxd-icon-button orangehrm-quick-launch-icon' and @title='My Leave']"
        self.myleave_fromdate_by = By.XPATH
        self.myleave_fromdate_value = "//label[text()='From Date']/following::input[1]"
        self.myleave_todate_by = By.XPATH
        self.myleave_todate_value = "//label[text()='To Date']/following::input[1]"
        self.myleave_statusdropdown_by = By.XPATH
        self.myleave_statusdropdown_value = "//label[text()='Show Leave with Status']/following::div[contains(@class, 'oxd-select-text-input')][1]"
        self.myleave_status_by = By.XPATH
        self.myleave_status_value = "(//span[text()='Rejected'])[1]"
        self.myleave_search_by = By.XPATH
        self.myleave_search_value = "(//button[@type='submit' and contains(., ' Search ')])[1]"
        self.my_timesheet_by = By.XPATH
        self.my_timesheet_value = "//button[@title='My Timesheet']"
        self.timesheet_period_by = By.XPATH
        self.timesheet_period_value = "//p[text()='Timesheet Period']/following::input[@class='oxd-input oxd-input--active']"
        self.timesheet_edit_by = By.XPATH
        self.timesheet_edit_value = "//button[@type='button' and contains(@class, 'oxd-button--ghost') and text()=' Edit ']"
        self.project_by = By.XPATH
        self.project_value = "//th[contains(text(), 'Project')]/following::input[@placeholder='Type for hints...']"
        self.activitydropdown_by = By.XPATH
        self.activitydropdown_value ="//th[contains(text(), 'Activity')]/following::i[contains(@class, 'oxd-icon bi-caret-down-fill')][1]"
        self.save_project_by = By.XPATH
        self.save_project_value = "//button[text()=' Save ']"
        self.enter_time_by = By.XPATH
        self.enter_time_value = "//td[contains(@class, 'orangehrm-timesheet-table-body-cell') and contains(@class, '--duration-input')]//input[contains(@class, 'oxd-input')]"
        self.pie_engineering_by = By.XPATH
        self.pie_engineering_value = "//span[@title='Engineering']"
        self.pie_humanresource_by = By.XPATH
        self.pie_humanresource_value = "//span[@title='Human Resources']"
        self.pie_unassigned_by = By.XPATH
        self.pie_unassigned_value = "//span[@title='Unassigned']"
        self.pie_texas_by = By.XPATH
        self.pie_texas_value = "//span[@title='Texas R&D']"
        self.pie_newYork_by = By.XPATH
        self.pie_newYork_value = "//span[@title='New York Sales Office']"


    def dashboard_click(self):
        self.driver.find_element(self.dashboard_by,self.dashboard_value).click()
    def time_At_work_button(self):
        self.driver.find_element(self.timeatwork_by,self.timeatwork_value).click()
    def punch_in_date(self,date):
        element = self.driver.find_element(self.punchin_date_by, self.punchin_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def punch_in_time(self,time):
        element = self.driver.find_element(self.punchin_time_by,self.punchin_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(time)
    def punch_in_note(self,note):
        self.driver.find_element(self.Note_by,self.Note_value).send_keys(note)
    def punch_in_button(self):
        self.driver.find_element(self.In_by,self.In_value).click()
    def punch_out_date(self,date):
        element = self.driver.find_element(self.punchout_date_by, self.punchout_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def punch_out_time(self,time):
        element = self.driver.find_element(self.punchout_time_by,self.punchout_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(time)
    def note(self,note):
        self.driver.find_element(self.Note_by,self.Note_value).send_keys(note)
    def out_button(self):
        self.driver.find_element(self.out_by,self.out_value).click()
    def pending_review(self):
        # self.driver.back()
        self.driver.find_element(self.pending_review_by,self.pending_review_value).click()
    def candidate_review(self):
        self.driver.back()
        self.driver.find_element(self.candidate_by,self.candidate_value).click()
    def add_button(self):
        self.driver.find_element(self.add_button_by,self.add_button_value).click()
    def firstname(self,name):
        self.driver.find_element(self.firstname_by,self.firstname_value).send_keys(name)
    def lastname(self,name):
        self.driver.find_element(self.lastname_by, self.lastname_value).send_keys(name)
    def vacancy(self):
        self.driver.find_element(self.vacancydropdown_by,self.vacancydropdown_value).click()
        self.driver.find_element(self.vacancy_select_by,self.vacancy_select_value).click()
    def email(self,email):
        self.driver.find_element(self.email_by,self.email_value).send_keys(email)
    def contact(self,number):
        self.driver.find_element(self.contact_by,self.contact_value).send_keys(number)
    def resume(self,path):
        self.driver.find_element(self.resume_by,self.resume_value).send_keys(path)
    def keyword(self,words):
        self.driver.find_element(self.keywords_by,self.keywords_value).send_keys(words)
    def date_of_application(self,date):
        element = self.driver.find_element(self.application_date_by,self.application_date_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)

    def note_of_candidate(self,note):
        self.driver.find_element(self.candidatenote_by,self.candidatenote_value).send_keys(note)
    def consent(self):
        self.driver.find_element(self.consent_by,self.consent_value).click()
    def save(self):
        self.driver.find_element(self.save_by,self.save_value).click()
    def vacancy_tab(self):
        self.driver.find_element(self.vacancy_button_by,self.vacancy_button_value).click()
        self.driver.find_element(self.add_vacancy_by,self.add_vacancy_value).click()
    def vacancy_name(self,name):
        element = self.driver.find_element(self.vacancy_name_by,self.vacancy_name_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def job_title(self):
        self.driver.find_element(self.job_titledropdown_by,self.job_titledropdown_value).click()
        self.driver.find_element(self.job_title_by,self.job_title_value).click()
    def description(self,text):
        element = self.driver.find_element(self.description_by,self.description_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def hiring_manager(self,text):
        element = self.driver.find_element(self.hiring_manager_by,self.hiring_manager_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def number_of_position(self,text):
        element = self.driver.find_element(self.no_of_position_by,self.no_of_position_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def save_candidate(self):
        self.driver.find_element(self.save_candidate_by,self.save_candidate_value).click()
    def dashboard(self):
        self.driver.find_element(self.dashboard_by,self.dashboard_value).click()
    def assign_leave(self):
        self.driver.back()
        self.driver.back()
        self.driver.find_element(self.assign_leave_By,self.assign_leave_value).click()
    def employee_name(self,name):
        self.driver.find_element(self.employee_name_by,self.employee_name_value).send_keys(name)
    def leave_type(self):
        self.driver.find_element(self.leavetypedropdown_by,self.leavetypedropdown_value).click()
        self.driver.find_element(self.leave_select_by,self.leave_select_value).click()
    def from_date(self,date):
        element = self.driver.find_element(self.fromdate_by,self.fromdate_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def to_date(self,date):
        element = self.driver.find_element(self.todate_by,self.todate_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def partial_day(self):
        self.driver.find_element(self.partialdays_dropdown_by,self.partialdays_dropdown_value).click()
    def duration(self):
        self.driver.find_element(self.durationdropdown_by,self.durationdropdown_value).click()
        self.driver.find_element(self.duration_select_by,self.duration_select_value).click()

    def assign_button(self):
        self.driver.find_element(self.assign_by,self.assign_value).click()
    def leave_list(self):
        self.driver.back()
        self.driver.find_element(self.leave_list_By,self.leave_list_value).click()
    def fromdate(self,date):
        element = self.driver.find_element(self.from_by,self.from_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def To_Date(self,date):
       element =  self.driver.find_element(self.to_date_by,self.to_date_value)
       element.send_keys(Keys.CONTROL+"a")
       element.send_keys(Keys.BACKSPACE)
       element.send_keys(date)
    def leave_status(self):
        self.driver.find_element(self.leave_statusdropdown_by,self.leave_statusdropdown_value).click()
        self.driver.find_element(self.leave_status_by,self.leave_status_value).click()
    def leavetype(self):
        self.driver.find_element(self.leave_typedropdown_by,self.leave_typedropdown_value).click()
        self.driver.find_element(self.leavetype_by,self.leavetype_value).click()
    def employee_name_hint(self,name):
        element = self.driver.find_element(self.employee_hint_by,self.employee_hint_value)
        element.send_keys(Keys.CONTROL+'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def search(self):
        self.driver.find_element(self.search_by,self.search_value).click()
    def timesheets(self):
        self.driver.back()
        self.driver.find_element(self.timesheets_by,self.timesheets_value).click()
    def employeename(self,name):
        element= self.driver.find_element(self.employeename_by,self.employeename_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def view_button(self):
        self.driver.find_element(self.view_by,self.view_value).click()
    def apply_leave(self):
        self.driver.back()
        self.driver.find_element(self.apply_leave_by,self.apply_leave_value).click()
    def apply_leave_type(self):
        self.driver.find_element(self.Leave_typedropdown_by,self.Leave_typedropdown_value).click()
        self.driver.find_element(self.Leave_type_by,self.Leave_type_value).click()
    def leave_from_date(self,date):
        element = self.driver.find_element(self.Fromdate_by,self.Fromdate_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def leave_to_date(self,date):
        element = self.driver.find_element(self.To_date_by,self.To_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def apply(self):
        self.driver.find_element(self.apply_by,self.apply_value).click()
    def my_leave_button(self):
        self.driver.back()
        self.driver.find_element(self.myleave_by,self.myleave_value).click()
    def myleave_fromdate(self,date):
        element = self.driver.find_element(self.myleave_fromdate_by,self.myleave_fromdate_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def myleave_todate(self,date):
        element = self.driver.find_element(self.myleave_todate_by,self.myleave_todate_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def myleave_status(self):
        self.driver.find_element(self.myleave_statusdropdown_by,self.myleave_statusdropdown_value).click()
        self.driver.find_element(self.myleave_status_by,self.myleave_status_value).click()
    def search_myleave(self):
        self.driver.find_element(self.myleave_search_by,self.myleave_search_value).click()
    def my_timesheet_button(self):
        self.driver.back()
        self.driver.find_element(self.my_timesheet_by,self.my_timesheet_value).click()
    def timesheet_period_date(self,date):
        element = self.driver.find_element(self.timesheet_period_by,self.timesheet_period_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def timesheet_edit(self):
        self.driver.find_element(self.timesheet_edit_by,self.timesheet_edit_value).click()
    def project(self,name):
        element = self.driver.find_element(self.project_by, self.project_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def activity(self):
        self.driver.find_element(self.activitydropdown_by,self.activitydropdown_value).click()
    def enter_time(self, text):
        element = self.driver.find_element(self.enter_time_by, self.enter_time_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def save_project(self):
            self.driver.find_element(self.save_project_by, self.save_project_value).click()

    def back_dashboard(self):
        self.driver.find_element(self.dashboard_by,self.dashboard_value).click()
    def pie_chart_engineering(self):
        self.driver.find_element(self.pie_engineering_by,self.pie_engineering_value).click()
    def pie_chart_human_resource(self):
        self.driver.find_element(self.pie_humanresource_by,self.pie_humanresource_value).click()
    def pie_chart_unassigned(self):
        self.driver.find_element(self.pie_unassigned_by,self.pie_unassigned_value).click()
    def pie_chart_texas(self):
        self.driver.find_element(self.pie_texas_by,self.pie_texas_value).click()
    def pie_chart_new_york(self):
        self.driver.find_element(self.pie_newYork_by,self.pie_newYork_value).click()







