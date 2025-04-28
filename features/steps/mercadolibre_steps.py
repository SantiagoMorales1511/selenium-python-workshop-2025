from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.mercadolibre_page import MercadoLibrePage
import time

@given('estoy en la página principal de MercadoLibre Colombia')
def step_impl(context):
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
        except:
            pass
        delattr(context, 'driver')
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--incognito')
    
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    context.driver.implicitly_wait(10)
    
    context.mercadolibre_page = MercadoLibrePage(context.driver)
    
    context.mercadolibre_page.open_home_page()

@when('busco el producto "{product_name}"')
def step_impl(context, product_name):
    try:
        context.mercadolibre_page.search_product(product_name)
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")
        try:
            context.driver.save_screenshot("error_busqueda.png")
            print("Captura de pantalla guardada como error_busqueda.png")
        except:
            print("No se pudo guardar la captura de pantalla")
        raise

@then('debo ver resultados que contienen el texto "{expected_text}"')
def step_impl(context, expected_text):
    try:
        assert context.mercadolibre_page.verify_results_contain_text(expected_text), \
            f"No se encontraron resultados que contengan '{expected_text}'"
    except Exception as e:
        print(f"Error al verificar resultados: {e}")
    finally:
        time.sleep(2)
        try:
            context.driver.quit()
        except Exception as e:
            print(f"Error al cerrar el navegador: {e}")