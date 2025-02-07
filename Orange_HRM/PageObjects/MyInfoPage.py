from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class Myinfo:
    def __init__(self,driver):
        self.driver = driver
        self.myinfo_page_by = By.LINK_TEXT
        self.myinfo_page_value = "My Info"
        self.profile_click_by = By.XPATH
        self.profile_click_value = "//div[contains(@class, 'orangehrm-edit-employee-image-wrapper')]//img[contains(@class, 'employee-image')]"
        self.add_profile_by = By.XPATH
        self.add_profile_value = "//input[@type = 'file']"
        self.save_profile_pic_by = By.XPATH
        self.save_profile_pic_value = "//button[text()=' Save ']"
        self.firstname_by = By.XPATH
        self.firstname_value = "//input[@name='firstName' and @placeholder='First Name']"
        self.middlename_by = By.XPATH
        self.middlename_value = "//input[@name='middleName' and @placeholder='Middle Name']"
        self.lastname_by = By.XPATH
        self.lastname_value = "//input[@name='lastName' and @placeholder='Last Name']"
        self.employeeid_by = By.XPATH
        self.employeeid_value ="//label[text()='Employee Id']/following::input[1]"
        self.other_id_by = By.XPATH
        self.other_id_value = "//label[text()='Other Id']/following::input[1]"
        self.license_by = By.XPATH
        self.license_value = "//label[text()=\"Driver's License Number\"]/following::input[1]"
        self.licenseexpire_by = By.XPATH
        self.licenseexpire_value = "//label[text()='License Expiry Date']/following::input[1]"
        self.nationality_dropdown_by = By.XPATH
        self.nationality_dropdown_value =  "//div[@class='oxd-select-text--after']/i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
        self.nationality_by = By.XPATH
        self.nationality_value = "//div[contains(@class, 'oxd-select-dropdown')]//span[text()='Indian']"
        self.status_dropdown_by = By.XPATH
        self.status_dropdown_value = "//label[text()='Marital Status']/following::div[@class='oxd-select-text--after'][1]"
        self.status_By = By.XPATH
        self.status_value = "//div[contains(@class, 'oxd-select-dropdown')]//span[text()='Single']"
        self.DOB_By = By.XPATH
        self.DOB_value = "//label[text()='Date of Birth']/following::input[1]"
        self.Gender_By = By.XPATH
        self.Gender_value = "//label[text()='Female']"
        self.save_by = By.XPATH
        self.save_value = "(//button[text()=' Save '])[1]"
        self.Contact_details_By = By.XPATH
        self.Contact_details_value = "//a[text() = 'Contact Details']"
        self.street1_by = By.XPATH
        self.street1_value = "//label[text()='Street 1']/following::input[1]"
        self.street2_by = By.XPATH
        self.street2_value = "//label[text()='Street 2']/following::input[1]"
        self.City_by = By.XPATH
        self.City_value = "//label[text()='City']/following::input[1]"
        self.state_by = By.XPATH
        self.state_value = "//label[text()='State/Province']/following::input[1]"
        self.postal_by = By.XPATH
        self.postal_value = "//label[text()='Zip/Postal Code']/following::input[1]"
        self.Countrydropdown_by = By.XPATH
        self.Countrydropdown_value = "//i[contains(@class, 'bi-caret-down-fill') and contains(@class, 'oxd-select-text--arrow')]"
        self.Country_by = By.XPATH
        self.Country_value = "//div[contains(@class, 'oxd-select-dropdown')]//span[text()='India']"
        self.Home_no_by = By.XPATH
        self.Home_no_value = "//label[text()='Home']/following::input[1]"
        self.Mobile_no_by = By.XPATH
        self.Mobile_no_value = "//label[text()='Mobile']/following::input[1]"
        self.Work_no_by = By.XPATH
        self.Work_no_value = "//label[text()='Work']/following::input[1]"
        self.email_by = By.XPATH
        self.email_value = "//label[text()='Work Email']/following::input[1]"
        self.otheremail_by = By.XPATH
        self.otheremail_value = "//label[text()='Other Email']/following::input[1]"
        self.savedetailspage_by = By.XPATH
        self.savedetailspage_value = "//button[text()=' Save ']"
        self.emergencycontactpage_by = By.XPATH
        self.emergencycontactpage_value = "//a[text()='Emergency Contacts']"
        self.add_button_by = By.XPATH
        self.add_button_value = "//button[contains(@class, 'oxd-button') and contains(., 'Add')]"
        self.add_name_by = By.XPATH
        self.add_name_value = "//label[text()='Name']/following::input[1]"
        self.add_relationship_by =By.XPATH
        self.add_relationship_value = "//label[text()='Relationship']/following::input[1]"
        self.add_homeno_by = By.XPATH
        self.add_homeno_value = "//label[text()='Home Telephone']/following::input[1]"
        self.add_mobile_by = By.XPATH
        self.add_mobile_value = "//label[text()='Mobile']/following::input[1]"
        self.save_add_by = By.XPATH
        self.save_add ="//button[text()=' Save ']"
        self.immigration_by = By.XPATH
        self.immigration_value = "//a[text()='Immigration']"
        self.add_immigration_by = By.XPATH
        self.add_immigration_value = "//button[contains(@class, 'oxd-button') and contains(@class, 'oxd-button--text') and text()=' Add ']"
        self.add_passport_by = By.XPATH
        self.add_passport_value = "//label[text()='Passport']"
        self.add_number_by = By.XPATH
        self.add_number_value = "//label[text()='Number']/following::input[1]"
        self.issued_date_by = By.XPATH
        self.issued_date_value = "//label[text()='Issued Date']/following::input[1]"
        self.expiry_date_by = By.XPATH
        self.expiry_date_value = "//label[text()='Expiry Date']/following::input[1]"
        self.eligible_status_by = By.XPATH
        self.eligible_status_value = "//label[text()='Eligible Status']/following::input[1]"
        self.issuedby_dropdown_by = By.XPATH
        self.issuedby_dropdown_value = "//div[@class='oxd-select-text-input' and text()='-- Select --']"
        self.issuedby_by = By.XPATH
        self.issuedby_value = "//div[contains(@class, 'oxd-select-dropdown')]//span[text()='India']"
        self.eligiblereview_by = By.XPATH
        self.eligiblereview_value = "//label[text()='Eligible Review Date']/following::input[1]"
        self.save_immigration_by = By.XPATH
        self.save_immigration_value ="//button[text()=' Save ']"
        self.add_attachment_by = By.XPATH
        self.add_attachment_value = "//h6[text()='Attachments']/following::button[text()=' Add ']"
        self.browse_by = By.XPATH
        self.browse_value = "//input[@type='file']"
        self.save_attachment_by = By.XPATH
        self.save_attachment_value = "//button[text()=' Save ']"



    def open_page(self,url):
        self.driver.get(url)
    def myinfo_page(self):
        self.driver.find_element(self.myinfo_page_by,self.myinfo_page_value).click()
    def profile_picture(self,picture):
        self.driver.find_element(self.profile_click_by,self.profile_click_value).click()
        self.driver.find_element(self.add_profile_by, self.add_profile_value).send_keys(picture)
        self.driver.find_element(self.save_profile_pic_by,self.save_profile_pic_value).click()
        self.driver.back()
    def first_name(self,firstname):
        element = self.driver.find_element(self.firstname_by,self.firstname_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(firstname)
    def middle_name(self,middlename):
        element = self.driver.find_element(self.middlename_by,self.middlename_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(middlename)
    def last_name(self,lastname):
        element = self.driver.find_element(self.lastname_by,self.lastname_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(lastname)
    def employee_id(self,employeeid):
        element = self.driver.find_element(self.employeeid_by,self.employeeid_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(employeeid)
    def other_id(self,otherid):
        element = self.driver.find_element(self.other_id_by,self.other_id_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(otherid)
    def license(self,driverlicense):
        element = self.driver.find_element(self.license_by,self.license_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(driverlicense)
    def license_expire(self,driverlicenseexpire):
        element = self.driver.find_element(self.licenseexpire_by,self.licenseexpire_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(driverlicenseexpire)
    def nationality_select(self):
        self.driver.find_element(self.nationality_dropdown_by,self.nationality_dropdown_value).click()
        self.driver.find_element(self.nationality_by, self.nationality_value).click()
    def martial_status(self):
        self.driver.find_element(self.status_dropdown_by,self.status_dropdown_value).click()
        self.driver.find_element(self.status_By,self.status_value).click()
    def date_of_birth(self,DOB):
        element = self.driver.find_element(self.DOB_By,self.DOB_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(DOB)
    def gender(self):
        self.driver.find_element(self.Gender_By,self.Gender_value).click()
    def save(self):
        self.driver.find_element(self.save_by,self.save_value).click()
    def contact_details_page(self):
        self.driver.find_element(self.Contact_details_By,self.Contact_details_value).click()
    def street_1(self,street):
        element = self.driver.find_element(self.street1_by,self.street1_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(street)
    def street_2(self,street2):
        element = self.driver.find_element(self.street2_by,self.street2_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(street2)
    def city(self,city):
        element = self.driver.find_element(self.City_by,self.City_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(city)
    def state(self,state):
        element = self.driver.find_element(self.state_by,self.state_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(state)
    def postal_code(self,postal):
        element = self.driver.find_element(self.postal_by,self.postal_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(postal)
    def country(self):
        self.driver.find_element(self.Countrydropdown_by,self.Countrydropdown_value).click()
        self.driver.find_element(self.Country_by,self.Country_value).click()
    def home(self,number):
        element = self.driver.find_element(self.Home_no_by, self.Home_no_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def mobile(self,number):
        element = self.driver.find_element(self.Mobile_no_by, self.Mobile_no_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def work(self,number):
        element = self.driver.find_element(self.Work_no_by, self.Work_no_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def email(self,email):
        element = self.driver.find_element(self.email_by, self.email_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(email)
    def other_email(self,email):
        element = self.driver.find_element(self.otheremail_by, self.otheremail_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(email)
    def save_details_page(self):
        self.driver.find_element(self.savedetailspage_by,self.savedetailspage_value).click()
    def emergency_contact_page(self):
        self.driver.find_element(self.emergencycontactpage_by,self.emergencycontactpage_value).click()
    def add_button(self):
        self.driver.find_element(self.add_button_by,self.add_button_value).click()
    def add_name(self,name):
        element = self.driver.find_element(self.add_name_by,self.add_name_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(name)
    def add_relationship(self,status):
        element = self.driver.find_element(self.add_relationship_by,self.add_relationship_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(status)
    def add_home_number(self,number):
        element = self.driver.find_element(self.add_homeno_by,self.add_homeno_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def add_mobile_number(self,number):
        element = self.driver.find_element(self.add_mobile_by,self.add_mobile_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def save_emergency_contact(self):
        self.driver.find_element(self.save_add_by,self.save_value).click()
    def immigration_page(self):
        self.driver.find_element(self.immigration_by,self.immigration_value).click()
    def add_immigration(self):
        self.driver.find_element(self.add_immigration_by,self.add_immigration_value).click()
    def add_passport(self):
        self.driver.find_element(self.add_passport_by,self.add_passport_value).click()
    def add_number(self,number):
        element = self.driver.find_element(self.add_number_by,self.add_number_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)
    def issued_date(self,date):
        element = self.driver.find_element(self.issued_date_by,self.issued_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def expiry_date(self,date):
        element = self.driver.find_element(self.expiry_date_by,self.expiry_date_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def eligibility_status(self,status):
        element = self.driver.find_element(self.eligible_status_by,self.eligible_status_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(status)
    def issued_by(self):
        self.driver.find_element(self.issuedby_dropdown_by,self.issuedby_dropdown_value).click()
        self.driver.find_element(self.issuedby_by,self.issuedby_value).click()
    def eligible_review_date(self,date):
        element = self.driver.find_element(self.eligiblereview_by,self.eligiblereview_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
    def save_immigration(self):
        self.driver.find_element(self.save_immigration_by,self.save_immigration_value).click()
    def add_attachment(self):
        self.driver.find_element(self.add_attachment_by,self.add_attachment_value).click()
    def browse_click(self,path):
        self.driver.find_element(self.browse_by,self.browse_value).send_keys(path)
    def save_attachment(self):
        self.driver.find_element(self.save_attachment_by,self.save_attachment_value).click()















