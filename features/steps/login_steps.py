from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    if not hasattr(context, 'driver'):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
    
    context.login_page = LoginPage(context.driver)
    
    context.inventory_page = InventoryPage(context.driver)
    
    context.login_page.open_login_page()

@when('the user logs in with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_page.login("standard_user", "secret_sauce")

@when('the user logs in with invalid credentials')
def step_when_user_logs_in_invalid(context):
    context.login_page.login("invalid_user", "invalid_password")

@when('the user logs in with empty credentials')
def step_when_user_logs_in_empty(context):
    context.login_page.login("", "")

@then('the user should be redirected to the inventory page')
def step_then_redirected_to_inventory(context):
    assert context.inventory_page.is_on_inventory_page(), "No fuimos redirigidos a la página de inventario"

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    assert context.login_page.is_error_message_displayed(), "No se muestra mensaje de error"