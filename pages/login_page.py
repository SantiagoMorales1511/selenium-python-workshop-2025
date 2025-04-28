from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Clase para interactuar con la página de login de SauceDemo."""
    
    LOGIN_URL = "https://www.saucedemo.com/"
    
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def open_login_page(self):
        """Abre la página de login."""
        self.open_url(self.LOGIN_URL)
    
    def login(self, username, password):
        """Realiza el login con las credenciales proporcionadas."""
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Obtiene el mensaje de error si existe."""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_message_displayed(self):
        """Verifica si se muestra un mensaje de error."""
        return self.is_displayed(self.ERROR_MESSAGE)