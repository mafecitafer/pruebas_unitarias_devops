from src.validador import (validar_email, validar_telefono, validar_edad,
                           validar_password, validar_url, validar_fecha,
                           validar_cedula)

def test_email_vacio_es_invalido():
    # Arrange
    email = ""
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False

def test_email_con_dos_arrobas_es_invalido():
    # Arrange
    email = "a@b@c.com"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False

def test_email_sin_usuario_es_invalido():
    # Arrange
    email = "@dominio.com"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False

def test_email_dominio_sin_punto_es_invalido():
    # Arrange
    email = "usuario@dominio"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False

def test_telefono_vacio_es_invalido():
    # Arrange
    telefono = ""
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False

def test_telefono_con_letras_es_invalido():
    # Arrange
    telefono = "abc1234567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False

def test_telefono_muy_corto_es_invalido():
    # Arrange
    telefono = "123"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False

def test_edad_no_entera_es_invalida():
    # Arrange
    edad = "20"
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False

def test_edad_negativa_es_invalida():
    # Arrange
    edad = -1
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False

def test_edad_valida():
    # Arrange
    edad = 25
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is True

def test_password_vacia_es_invalida():
    # Arrange
    password = ""
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False

def test_password_corta_es_invalida():
    # Arrange
    password = "Ab1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False

def test_password_sin_minuscula_es_invalida():
    # Arrange
    password = "ABCDEFG1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False

def test_password_sin_numero_es_invalida():
    # Arrange
    password = "Abcdefgh"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False

def test_password_valida():
    # Arrange
    password = "Abcdefg1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is True

def test_url_vacia_es_invalida():
    # Arrange
    url = ""
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is False

def test_url_valida():
    # Arrange
    url = "https://unal.edu.co"
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is True

def test_url_con_protocolo_ftp_es_invalida():
    # Arrange
    url = "ftp://ejemplo.com"
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is False

def test_fecha_con_dia_decimal_es_invalida():
    # Arrange
    dia, mes, año = 1.5, 1, 2025
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_fecha_con_mes_trece_es_invalida():
    # Arrange
    dia, mes, año = 10, 13, 2025
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_fecha_con_dia_cero_es_invalida():
    # Arrange
    dia, mes, año = 0, 5, 2025
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_fecha_con_año_fuera_de_rango_es_invalida():
    # Arrange
    dia, mes, año = 10, 5, 1800
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_fecha_29_febrero_año_bisiesto_es_valida():
    # Arrange
    dia, mes, año = 29, 2, 2024
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is True

def test_cedula_vacia_es_invalida():
    # Arrange
    cedula = ""
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False

def test_cedula_valida():
    # Arrange
    cedula = "1234567890"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is True

def test_cedula_muy_corta_es_invalida():
    # Arrange
    cedula = "123"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False

def test_cedula_muy_larga_es_invalida():
    # Arrange
    cedula = "12345678901"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False
