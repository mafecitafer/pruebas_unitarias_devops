from src.validador import (validar_email, validar_telefono, validar_edad,
                           validar_password, validar_fecha, validar_cedula)

def test_validar_email_valido():
    # Arrange
    email = "mfe@unal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is True

def test_validar_email_sin_arroba():
    # Arrange
    email = "mfeunal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False

def test_validar_telefono_con_guiones():
    # Arrange
    telefono = "300-123-4567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is True

def test_validar_edad_sobre_el_limite():
    # Arrange
    edad = 121
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False

def test_validar_password_sin_mayuscula():
    # Arrange
    password = "abcdefg1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False

def test_validar_fecha_valida():
    # Arrange
    dia, mes, año = 15, 6, 2025
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is True

def test_validar_fecha_31_de_febrero():  # BUG
    # Arrange
    dia, mes, año = 31, 2, 2025
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_validar_fecha_29_febrero_no_bisiesto():  # BUG
    # Arrange
    dia, mes, año = 29, 2, 2023
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert
    assert resultado is False

def test_validar_cedula_con_letras():
    # Arrange
    cedula = "12345abc"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False
