Feature: Búsqueda de productos en MercadoLibre
  Como usuario de MercadoLibre
  Quiero buscar productos específicos
  Para encontrar ofertas y realizar compras

  Scenario: Buscar iPhone 13 en MercadoLibre
    Given estoy en la página principal de MercadoLibre Colombia
    When busco el producto "iPhone 13"
    Then debo ver resultados que contienen el texto "iPhone"