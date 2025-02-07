from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_by = By.NAME
        self.username_value = "username"
        self.password_by = By.NAME
        self.password_value = "password"
        self.login_by = By.XPATH
        self.login_value = "//button[@type ='submit']"
        self.profile_dropdown_by = By.XPATH
        self.profile_dropdown_value = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logout_by = By.XPATH
        self.logout_value = "//a[@class='oxd-userdropdown-link']"


    def open_page(self, url):
        self.driver.get(url)

    def user_name(self, username):
        self.driver.find_element(self.username_by, self.username_value).send_keys(username)

    def pass_word(self, password):
        self.driver.find_element(self.password_by, self.password_value).send_keys(password)

    def submit_button(self):
        self.driver.find_element(self.login_by, self.login_value).click()

    def dropdown_click(self):
        self.driver.find_element(self.profile_dropdown_by,self.profile_dropdown_value).click()

    def logout_click(self):
        self.driver.find_element(self.logout_by,self.logout_value).click()


