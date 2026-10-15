import pytest
from src.descuentos import (aplicar_descuento, calcular_descuento,
                            calcular_precio_final, descuento_por_volumen,
                            descuento_cumulativo, descuento_apilado)

def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -1, 10
    # Act / Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_calcular_descuento_monto_correcto():
    # Arrange
    precio, porcentaje = 200, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(20)

def test_calcular_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -1, 10
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)

def test_calcular_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio, porcentaje = 100, 150
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)

def test_precio_final_precio_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = -1, 19, 10
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)

def test_precio_final_impuesto_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, -5, 10
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)

def test_precio_final_descuento_invalido_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, 19, 150
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)

def test_volumen_cantidad_negativa_lanza_error():
    # Arrange
    cantidad, precio_unitario = -1, 10
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)

def test_volumen_precio_unitario_negativo_lanza_error():
    # Arrange
    cantidad, precio_unitario = 10, -1
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)

def test_volumen_veinte_unidades_diez_por_ciento():
    # Arrange
    cantidad, precio_unitario = 20, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(180)

def test_volumen_cincuenta_unidades_quince_por_ciento():
    # Arrange
    cantidad, precio_unitario = 50, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(425)

def test_volumen_cien_unidades_veinte_por_ciento():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(800)

def test_cumulativo_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -1, [10]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)

def test_cumulativo_sin_descuentos_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100

def test_cumulativo_descuento_invalido_lanza_error():
    # Arrange
    precio, descuentos = 100, [10, 150]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)

def test_apilado_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -1, [10]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)

def test_apilado_sin_descuentos_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100

def test_apilado_suma_porcentajes():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(70)
