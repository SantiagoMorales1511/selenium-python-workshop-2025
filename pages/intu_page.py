from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IntuPage(BasePage):
    LOGIN_URL = "https://icesi.edu.co/moodle/login/index.php"
    
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='Nombre de usuario']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Contraseña']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_LINK = (By.LINK_TEXT, "¿Olvidó su nombre de usuario o contraseña?")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, .error")
    USER_MENU = (By.CSS_SELECTOR, ".usermenu")
    
    def open_login_page(self):
        self.open_url(self.LOGIN_URL)
    
    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def click_forgot_password(self):
        self.click_element(self.FORGOT_LINK)
    
    def is_logged_in(self):
        return self.is_displayed(self.USER_MENU)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_message_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)