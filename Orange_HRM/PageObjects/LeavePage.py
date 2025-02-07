import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By



class Leave:
    def __init__(self,driver):
        self.driver = driver
        self.leave_by = By.XPATH
        self.leave_value = "//span[text() = 'Leave']"
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
        self.applyTab_by = By.XPATH
        self.applyTab_value = "//a[text() = 'Apply']"
        self.myLeaveTab_by = By.XPATH
        self.myLeaveTab_value = "//a[text() = 'My Leave']"
        self.myleave_fromdate_by = By.XPATH
        self.myleave_fromdate_value = "//label[text()='From Date']/following::input[1]"
        self.myleave_todate_by = By.XPATH
        self.myleave_todate_value = "//label[text()='To Date']/following::input[1]"
        self.myleave_statusdropdown_by = By.XPATH
        self.myleave_statusdropdown_value = "//label[text()='Show Leave with Status']/following::div[contains(@class, 'oxd-select-text-input')][1]"
        self.myleave_status_by = By.XPATH
        self.myleave_status_value = "(//span[text()='Rejected'])[1]"
        self.leave_type_by = By.XPATH
        self.leave_type_value = "//div[text() = '-- Select --']"
        self.myleave_search_by = By.XPATH
        self.myleave_search_value = "//button[text() = ' Search ']"
        self.entitlementTab_by = By.XPATH
        self.entitlementTab_value = "//span[text() = 'Entitlements ']"
        self.add_entitlement_by = By.XPATH
        self.add_entitlement_value = "//a[text() = 'Add Entitlements']"
        self.multiEmployees_radio_by = By.XPATH
        self.multiEmployees_radio_value = "//label[text() = 'Multiple Employees']"
        self.location_by = By.XPATH
        self.location_value = "//div[text() = '-- Select --'][1]"
        self.leaveType_by = By.XPATH
        self.leaveType_value = "//label[text()='Leave Type']/ancestor::div[contains(@class, 'oxd-input-group')]//div[contains(@class, 'oxd-select-text')]"
        self.sub_unit_by = By.XPATH
        self.sub_unit_value = "//label[text()='Sub Unit']/ancestor::div[contains(@class, 'oxd-input-group')]//div[contains(@class, 'oxd-select-text')]"
        self.leavePeriod_by = By.XPATH
        self.leavePeriod_value = "//label[text()='Leave Period']/ancestor::div[contains(@class, 'oxd-input-group')]//div[contains(@class, 'oxd-select-text')]"
        self.entitlement_by = By.XPATH
        self.entitlement_value = "//label[text()='Entitlement']/following::input[1]"
        self.save_entitlement_by = By.XPATH
        self.save_entitlement_value = "//button[text() = ' Save ']"
        self.ok_by = By.XPATH
        self.ok_value = "//button[text() = ' Ok ']"
        self.reportsTab_by = By.XPATH
        self.reportsTab_value = "//span[text() = 'Reports ']"
        self.reportTab1_by = By.XPATH
        self.reportsTab1_value = "//a[text() = 'Leave Entitlements and Usage Report']"
        self.leave_type_radio_by = By.XPATH
        self.leave_type_radio_value = "//label[text() = 'Leave Type']"
        self.past_employee_checkbox_by = By.XPATH
        self.past_employee_checkbox_value = "//span[contains(@class, 'oxd-switch-input')]"
        self.generate_by = By.XPATH
        self.generate_value = "//button[text() = ' Generate ']"
        self.assign_leave_tab_by = By.XPATH
        self.assign_leave_tab_value = "//a[contains(text(), 'Assign Leave')]"
        self.assign_leave_By = By.XPATH
        self.assign_leave_value = "//button[@title='Assign Leave' and @type='button']"
        self.employee_name_by = By.XPATH
        self.employee_name_value = "//label[text()='Employee Name']/following::input[1]"
        self.leavetypedropdown_by = By.XPATH
        self.leavetypedropdown_value = "//i[contains(@class, 'oxd-icon') and contains(@class, 'bi-caret-down-fill') and contains(@class, 'oxd-select-text--arrow')]"
        self.leave_select_by = By.XPATH
        self.leave_select_value = "//div[@class='oxd-select-text-input' and text()='-- Select --']"
        self.fromdate_by = By.XPATH
        self.fromdate_value = "//label[text()='From Date']/following::input[1]"
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




    def leave_page(self):
        self.driver.find_element(self.leave_by,self.leave_value).click()
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
    def apply_tab(self):
        self.driver.find_element(self.applyTab_by,self.applyTab_value).click()
    def my_leave_tab(self):
        self.driver.find_element(self.myLeaveTab_by,self.myLeaveTab_value).click()
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

    def leave_type(self):
        dropdown = self.driver.find_element(self.leave_type_by, self.leave_type_value)
        dropdown.click()
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ENTER)

    def search_my_leave(self):
        self.driver.find_element(self.myleave_search_by,self.myleave_search_value).click()
    def entitlement_tab(self):
        self.driver.find_element(self.entitlementTab_by,self.entitlementTab_value).click()
    def add_entitlement(self):
        self.driver.find_element(self.add_entitlement_by,self.add_entitlement_value).click()
    def multiple_employees_radiobtn(self):
        self.driver.find_element(self.multiEmployees_radio_by,self.multiEmployees_radio_value).click()
    def location(self):
        dropdown = self.driver.find_element(self.location_by, self.location_value)
        dropdown.click()
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ENTER)
    def leave_type_entitlement(self):
        actions = ActionChains(self.driver)
        dropdown = self.driver.find_element(self.leaveType_by, self.leaveType_value)
        dropdown.click()
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
    def sub_unit(self):
        actions = ActionChains(self.driver)
        dropdown = self.driver.find_element(self.sub_unit_by, self.sub_unit_value)
        dropdown.click()
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
    def leave_period(self):
        actions = ActionChains(self.driver)
        dropdown = self.driver.find_element(self.leavePeriod_by, self.leavePeriod_value)
        dropdown.click()
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
    def entitlement(self,text):
        element = self.driver.find_element(self.entitlement_by,self.entitlement_value)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)
    def save_entitlement(self):
        self.driver.find_element(self.save_entitlement_by,self.save_entitlement_value).click()
    def ok_button(self):
        self.driver.find_element(self.ok_by,self.ok_value).click()
    def report_tab(self):
        self.driver.find_element(self.reportsTab_by,self.reportsTab_value).click()
    def report_tab1(self):
        self.driver.find_element(self.reportTab1_by,self.reportsTab1_value).click()
    def leave_type_radio_button(self):
        self.driver.find_element(self.leave_type_radio_by,self.leave_type_radio_value).click()
    def past_employees_checkbox(self):
        self.driver.find_element(self.past_employee_checkbox_by,self.past_employee_checkbox_value).click()
    def generate_button(self):
        self.driver.find_element(self.generate_by,self.generate_value).click()
    def assign_leave_tab(self):
        self.driver.find_element(self.assign_leave_tab_by,self.assign_leave_tab_value).click()
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


