from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    
    def is_on_inventory_page(self):
        return self.is_displayed(self.INVENTORY_CONTAINER)
    
    def get_url(self):
        return self.driver.current_url
    
    def get_product_count(self):
        products = self.find_elements(self.PRODUCT_ITEMS)
        return len(products)
    
    def add_product_to_cart(self, product_index=0):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if product_index < len(buttons):
            buttons[product_index].click()
        else:
            raise IndexError(f"Índice de producto {product_index} fuera de rango")
    
    def click_shopping_cart(self):
        self.click_element(self.SHOPPING_CART)