Feature: Login en Intu (ICESI)
  Como usuario de la plataforma Intu
  Quiero poder iniciar sesión
  Para acceder a los recursos de la universidad

  Scenario: Intento de login con credenciales válidas
    Given el usuario está en la página de login de Intu
    When el usuario inicia sesión con credenciales válidas
    Then el usuario debería ser redirigido a su página principal

  Scenario: Intento de login con credenciales inválidas
    Given el usuario está en la página de login de Intu
    When el usuario inicia sesión con credenciales inválidas
    Then debería mostrarse un mensaje de error

  Scenario: Intento de login con campos vacíos
    Given el usuario está en la página de login de Intu
    When el usuario intenta iniciar sesión sin ingresar credenciales
    Then debería mostrarse un mensaje de error

  Scenario: Navegación a la página de recuperación de contraseña
    Given el usuario está en la página de login de Intu
    When el usuario hace clic en el enlace de olvidó su contraseña
    Then debería ser redirigido a la página de recuperación de contraseña