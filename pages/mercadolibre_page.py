from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time

class MercadoLibrePage(BasePage):
    """Clase simplificada para interactuar con la página de MercadoLibre."""
    
    BASE_URL = "https://www.mercadolibre.com.co"
    
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.nav-search-input")
    
    def open_home_page(self):
        """Abre la página principal de MercadoLibre Colombia."""
        self.open_url(self.BASE_URL)
        time.sleep(3)
    
    def search_product(self, product_name):
        """Busca un producto en MercadoLibre usando método simplificado."""
        try:
            search_box = self.driver.find_element(*self.SEARCH_INPUT)
            search_box.clear()
            search_box.send_keys(product_name)
            search_box.send_keys(Keys.RETURN)
            
            time.sleep(5)
        except Exception as e:
            print(f"Error al buscar: {e}")
            try:
                search_box = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Buscar')]")
                search_box.clear()
                search_box.send_keys(product_name)
                search_box.send_keys(Keys.RETURN)
                time.sleep(5)
            except Exception as e2:
                print(f"También falló el enfoque alternativo: {e2}")
                raise
    
    def verify_results_contain_text(self, text):
        """Verifica si la página de resultados contiene el texto especificado."""
        page_source = self.driver.page_source.lower()
        
        try:
            self.driver.save_screenshot("mercadolibre_results.png")
            print(f"Captura de pantalla guardada como mercadolibre_results.png")
        except Exception as e:
            print(f"No se pudo guardar la captura de pantalla: {e}")
        
        contains_text = text.lower() in page_source
        
        if not contains_text:
            print(f"No se encontró '{text}' en la página de resultados")
        else:
            print(f"Se encontró '{text}' en la página de resultados")
            
        return contains_text