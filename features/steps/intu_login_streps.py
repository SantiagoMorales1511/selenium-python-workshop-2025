from behave import given, when, then
from selenium import webdriver
from pages.intu_page import IntuPage

@given('el usuario está en la página de login de Intu')
def step_given_user_on_intu_login_page(context):
    if not hasattr(context, 'driver'):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
    
    context.intu_page = IntuPage(context.driver)
    
    context.intu_page.open_login_page()

@when('el usuario inicia sesión con credenciales inválidas')
def step_when_user_logs_in_invalid(context):
    context.intu_page.login("usuario_invalido", "contraseña_invalida")

@when('el usuario intenta iniciar sesión sin ingresar credenciales')
def step_when_user_logs_in_empty(context):
    context.intu_page.login("", "")

@when('el usuario hace clic en el enlace de olvidó su contraseña')
def step_when_user_clicks_forgot_password(context):
    context.intu_page.click_forgot_password()

@then('el usuario debería ser redirigido a su página principal')
def step_then_redirected_to_main(context):
    assert context.intu_page.is_logged_in(), "No se ha iniciado sesión correctamente"

@then('debería mostrarse un mensaje de error')
def step_then_error_message_displayed(context):
    assert context.intu_page.is_error_message_displayed(), "No se muestra mensaje de error"

@then('debería ser redirigido a la página de recuperación de contraseña')
def step_then_redirected_to_recovery(context):
    recovery_url = "icesi.edu.co/moodle/login/forgot_password.php"
    current_url = context.driver.current_url
    assert recovery_url in current_url, f"No fuimos redirigidos a la página de recuperación. URL actual: {current_url}"