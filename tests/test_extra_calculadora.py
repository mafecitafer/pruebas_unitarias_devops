import pytest
from src.calculadora import (restar, multiplicar, potencia, maximo, minimo,
                             calcular_area_rectangulo,
                             calcular_perimetro_rectangulo)

def test_restar_dos_numeros():
    # Arrange
    a, b = 5, 3
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 2

def test_multiplicar_dos_numeros():
    # Arrange
    a, b = 4, 3
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 12

def test_potencia_base_dos_exponente_tres():
    # Arrange
    base, exponente = 2, 3
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 8

def test_maximo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act / Assert
    with pytest.raises(ValueError):
        maximo(lista)

def test_minimo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act / Assert
    with pytest.raises(ValueError):
        minimo(lista)

def test_area_rectangulo_valida():
    # Arrange
    base, altura = 3, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 12

def test_perimetro_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = -1, 4
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)
