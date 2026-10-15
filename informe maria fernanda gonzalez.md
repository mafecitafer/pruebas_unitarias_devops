# Informe: Pruebas unitarias con pytest

 1. Datos
* Estudiante: Maria Fernanda Gonzalez Arango
* Repositorio (fork): https://github.com/mafecitafer/pruebas_unitarias_devops
* Módulos trabajados: calculadora, descuentos, validador (carpeta src/)
* Resultado final: 79 pruebas en verde y 100 % de cobertura en los tres módulos (meta: 85 %)


## 2. Análisis por módulo

Organicé los archivos de prueba dentro de la carpeta tests/ (test_calculadora.py, test_descuentos.py y test_validador.py), siguiendo la estructura AAA (Arrange, Act, Assert). El trabajo lo dividí en dos etapas: primero me enfoqué en escribir pruebas para detectar errores y casos límite, y luego agregué casos para cubrir las líneas o ramas que aún no se ejecutaban.

* calculadora (18 pruebas): Probé las operaciones principales y me centré en los casos donde el código podía fallar silenciosamente, como listas vacías, números negativos y listas con valores positivos. Para validar los errores esperados (como en raíz cuadrada de números negativos) utilicé pytest.raises(ValueError). Esto permitió detectar que minimo devolvía 0 al recibir solo positivos y que raiz_cuadrada aceptaba números negativos sin lanzar error.

* descuentos (25 pruebas): Diseñé pruebas combinando valores sencillos de verificar manualmente (por ejemplo, precio de 100, impuesto del 19 % y descuento del 10 %) y usando pytest.approx para evitar fallos por precisión de decimales. Recorrí las validaciones de entrada y los tramos de descuento por volumen (10, 20, 50 y 100 unidades). Al comprobar a mano el resultado de calcular_precio_final, noté que la función aplicaba el impuesto sobre el valor original y no sobre el precio ya descontado.

* validador (36 pruebas): Incluí casos válidos, entradas vacías y casos que violaran las reglas de cada función (correos sin arroba, contraseñas sin mayúsculas, cédulas con letras). En validar_fecha probé fechas inválidas como el 31 de febrero o el 29 de febrero en años no bisiestos. Esto reveló que la función original solo revisaba que el día estuviera en el rango de 1 a 31.


## 3. Bugs encontrados y correcciones

1. calculadora.minimo: Al pasar [5, 3, 8] devolvía 0 en lugar de 3. Se corrigió inicializando la variable con el primer elemento de la lista (min_val = lista[0]).
2. calculadora.raiz_cuadrada: Al ingresar un número negativo como -4 devolvía un número complejo sin lanzar excepción. Se ajustó para lanzar un ValueError cuando el parámetro sea menor a cero.
3. descuentos.calcular_precio_final: Con un precio de 100, 19 % de impuesto y 10 % de descuento devolvía 109.0 en vez de 107.1. Se corrigió calculando el impuesto sobre el valor con descuento.
4. validador.validar_fecha: Aceptaba fechas como (31, 2, 2025) y (29, 2, 2023) devolviendo True. Se corrigió validando el límite de días según el mes y año mediante calendar.monthrange.


## 4. Cobertura de código y evidencias

Para el manejo del repositorio mantuve un flujo de Git ordenado: registré primero los commits con las pruebas que fallaban en rojo y posteriormente los commits con las correcciones correspondientes en el código fuente.

El reporte de cobertura final obtenido en la terminal muestra un 100 % de cobertura en los tres módulos trabajados:

* src/calculadora.py: 44 líneas, 0 omitidas (100 %)
* src/descuentos.py: 58 líneas, 0 omitidas (100 %)
* src/validador.py: 67 líneas, 0 omitidas (100 %)
* Total: 169 líneas probadas, 79 pruebas ejecutadas en verde.

En la primera medición con las 27 pruebas iniciales la cobertura era del 84 % en calculadora, 67 % en descuentos y 60 % en validador. La columna de líneas no cubiertas me sirvió de guía para diseñar la segunda tanda de pruebas hasta completar la totalidad de las sentencias.


## 5. Reflexión final

Este taller me permitió comprender el valor práctico de las pruebas en rojo como mecanismo de diagnóstico previo a la modificación del código. Descubrir el fallo en calcular_precio_final me demostró la importancia de calcular previamente el resultado esperado de forma independiente en lugar de asumir como correcto el valor devuelto por la aplicación.

Por otra parte, pude constatar que la cobertura es una métrica útil para identificar zonas no ejecutadas, pero no reemplaza el diseño consciente de casos de prueba. El 100 % de cobertura asegura que cada línea se ejecutó, pero la detección de los fallos dependió de la selección de las entradas límite trabajadas.
