from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework_from_scratch.utilities.web_ui.base_page import BasePage

class NewEmailPage(BasePage):
    __notification_label = (By.XPATH, '//p[1]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_notification(self):
        notification = self.wait_until_element_located(self.__notification_label)
        return self.get_text(notification)