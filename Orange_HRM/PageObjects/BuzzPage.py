from selenium.webdriver.common.by import By

class Buzz:
    def __init__(self,driver):
        self.driver = driver
        self.buzz_by = By.XPATH
        self.buzz_value = "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Buzz']"
        self.posttext_by= By.XPATH
        self.posttext_value = "//textarea[contains(@class, 'oxd-buzz-post-input') and @placeholder=\"What's on your mind?\"]"
        self.sharephotos_button_by = By.XPATH
        self.sharephotos_button_value = "//button[contains(@class, 'oxd-glass-button') and contains(., 'Share Photos')]"
        self.share_photos_by = By.XPATH
        self.share_photos_value = "//input[@type='file']"
        self.click_share_by = By.XPATH
        self.click_share_value= "//button[text() = ' Share ']"
        self.postvideo_text_by = By.XPATH
        self.postvideo_text_value = "//textarea[contains(@class, 'oxd-buzz-post-input') and @placeholder=\"What's on your mind?\"]"
        self.share_videobutton_by = By.XPATH
        self.share_videobutton_value = "//button[contains(@class, 'oxd-glass-button') and contains(., ' Share Video')]"
        self.share_videolink_by =  By.XPATH
        self.share_videolink_value = "//textarea[@placeholder='Paste Video URL']"
        self.click_videoshare_by = By.XPATH
        self.click_videoshare_value = "//button[text() = ' Share ']"
        self.recent_post_by = By.XPATH
        self.recent_post_value = "//button[text() = ' Most Recent Posts ']"
        self.most_like_by = By.XPATH
        self.most_like_value = "//button[text() = ' Most Liked Posts ']"
        self.most_comments_by = By.XPATH
        self.most_comments_value = "//button[text() = ' Most Commented Posts ']"


    def buzz_page(self):
        self.driver.find_element(self.buzz_by,self.buzz_value).click()
    def post_text(self,text):
        self.driver.find_element(self.posttext_by,self.posttext_value).send_keys(text)
    def share_photos(self,photo):
        self.driver.find_element(self.sharephotos_button_by,self.sharephotos_button_value).click()
        self.driver.find_element(self.share_photos_by,self.share_photos_value).send_keys(photo)
        self.driver.find_element(self.click_share_by,self.click_share_value).click()
    def post_video_text(self,text):
        self.driver.find_element(self.postvideo_text_by,self.postvideo_text_value).send_keys(text)
    def share_videos(self,url):
        self.driver.find_element(self.share_videobutton_by,self.share_videobutton_value).click()
        self.driver.find_element(self.share_videolink_by,self.share_videolink_value).send_keys(url)
        self.driver.find_element(self.click_videoshare_by,self.click_videoshare_value).click()
    def most_recent_post(self):
        self.driver.find_element(self.recent_post_by,self.recent_post_value).click()
    def most_liked_post(self):
         self.driver.find_element(self.most_like_by, self.most_like_value).click()
    def most_commented_post(self):
        self.driver.find_element(self.most_comments_by,self.most_comments_value).click()