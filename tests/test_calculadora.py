
import pytest
from src.calculadora import (sumar, dividir, raiz_cuadrada, promedio,
                             maximo, minimo, calcular_area_rectangulo,
                             calcular_perimetro_rectangulo)

def test_sumar_dos_positivos():
    # Arrange
    a, b = 2, 3
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 5

def test_dividir_numeros_normales():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5

def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 5, 0
    # Act / Assert
    with pytest.raises(ValueError):
        dividir(a, b)

def test_raiz_cuadrada_de_nueve():
    # Arrange
    numero = 9
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 3

def test_raiz_cuadrada_de_negativo_lanza_error():  # BUG 1
    # Arrange
    numero = -4
    # Act / Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

def test_promedio_lista_normal():
    # Arrange
    lista = [2, 4, 6]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 4

def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act / Assert
    with pytest.raises(ValueError):
        promedio(lista)

def test_maximo_con_negativos():
    # Arrange
    lista = [-5, -2, -9]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == -2

def test_minimo_lista_de_positivos():  # BUG 2
    # Arrange
    lista = [5, 3, 8]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3

def test_area_rectangulo_negativa_lanza_error():
    # Arrange
    base, altura = -1, 5
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)

def test_perimetro_rectangulo():
    # Arrange
    base, altura = 3, 4
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 14
