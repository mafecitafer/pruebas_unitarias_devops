import pytest
from src.descuentos import (aplicar_descuento, calcular_precio_final,
                            descuento_por_volumen, descuento_cumulativo,
                            descuento_apilado)

def test_aplicar_descuento_diez_por_ciento():
    # Arrange
    precio, porcentaje = 200, 10
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(180)

def test_aplicar_descuento_porcentaje_invalido():
    # Arrange
    precio, porcentaje = 100, 101
    # Act / Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_precio_final_impuesto_sobre_precio_descontado():  # BUG
    # Arrange
    precio, impuesto, descuento = 100, 19, 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(107.1)

def test_descuento_por_volumen_en_el_limite_de_10():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(95)

def test_descuento_por_volumen_sin_descuento():
    # Arrange
    cantidad, precio_unitario = 5, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(50)

def test_descuento_cumulativo_dos_descuentos():
    # Arrange
    precio, descuentos = 100, [10, 10]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(81)

def test_descuento_apilado_mayor_a_100_lanza_error():
    # Arrange
    precio, descuentos = 100, [60, 50]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)
