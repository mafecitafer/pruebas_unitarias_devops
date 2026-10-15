# INFORME: Pruebas unitarias con pytest

## 1. DATOS
* Estudiante: Maria Fernanda Gonzalez Arango
* Repositorio (fork): https://github.com/mafecitafer/pruebas_unitarias_devops
* Herramientas: Python 3.13, pytest 8.0.0, pytest-cov 4.0.0
* Módulos trabajados: calculadora, descuentos, validador (carpeta src/)
* Resultado final: 79 pruebas en verde y 100 % de cobertura en los tres módulos (meta: 85 %)


## 2. ANALISIS POR MODULO

Las pruebas están en la carpeta tests/ (test_calculadora.py, test_descuentos.py y test_validador.py, más un archivo test_extra_*.py por módulo) y todas siguen la estructura AAA (Arrange, Act, Assert). Trabajé en dos etapas: primero escribí pruebas para encontrar errores y casos límite, y después agregué casos (los archivos test_extra_*.py) para cubrir las líneas que todavía no se ejecutaban.

* calculadora (18 pruebas): Probé las operaciones principales y me fijé sobre todo en los casos donde el código podía fallar sin avisar: listas vacías, números negativos y listas con solo valores positivos. Para los errores esperados (como la raíz de un número negativo) usé pytest.raises(ValueError). Así encontré que minimo devolvía 0 cuando la lista tenía solo positivos y que raiz_cuadrada aceptaba números negativos sin lanzar error.

* descuentos (25 pruebas): Usé valores fáciles de verificar a mano (precio de 100, impuesto del 19 % y descuento del 10 %) y pytest.approx para evitar problemas con los decimales. Probé las validaciones de entrada y cada tramo del descuento por volumen (10, 20, 50 y 100 unidades). Al calcular a mano el resultado de calcular_precio_final vi que la función aplicaba el impuesto sobre el precio original y no sobre el precio ya con descuento.

* validador (36 pruebas): Incluí casos válidos, entradas vacías y casos que rompen las reglas de cada función (correos sin arroba, contraseñas sin mayúscula, cédulas con letras). En validar_fecha probé fechas imposibles como el 31 de febrero o el 29 de febrero en un año no bisiesto. Con eso vi que la función original solo revisaba que el día estuviera entre 1 y 31.

No trabajé los demás módulos de src/ (fibonacci, autenticacion, conversor, csv_parser, manipulador_texto, procesador_texto y utils). Preferí profundizar en tres módulos que cubrir los diez de forma superficial.


## 3. BUGS ENCONTRADOS Y CORRECCIONES

| # | Módulo / función | Entrada que lo revela | Resultado erróneo | Resultado esperado | Corrección |
|---|---|---|---|---|---|
| 1 | calculadora.minimo | [5, 3, 8] | 0 | 3 | Inicializar con el primer elemento de la lista (min_val = lista[0]) |
| 2 | calculadora.raiz_cuadrada | -4 | Número complejo, sin excepción | ValueError | Lanzar ValueError cuando el número es menor a cero |
| 3 | descuentos.calcular_precio_final | (100, 19, 10) | 109.0 | 107.1 | Calcular el impuesto sobre el precio con descuento |
| 4 | validador.validar_fecha | (31, 2, 2025) y (29, 2, 2023) | True | False | Validar el máximo de días según el mes y el año con calendar.monthrange |

Salida de pytest antes de corregir (archivo evidencias/pytest_rojo.txt): fallaron 5 pruebas, que corresponden a estos 4 bugs.

```
FAILED tests/test_calculadora.py::test_raiz_cuadrada_de_negativo_lanza_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_calculadora.py::test_minimo_lista_de_positivos - assert 0 == 3
FAILED tests/test_descuentos.py::test_precio_final_impuesto_sobre_precio_descontado - assert 109.0 == 107.1 ± 1.1e-04
FAILED tests/test_validador.py::test_validar_fecha_31_de_febrero - assert True is False
FAILED tests/test_validador.py::test_validar_fecha_29_febrero_no_bisiesto - assert True is False
5 failed, 22 passed
```

Después de aplicar las cuatro correcciones, las 27 pruebas iniciales pasaron en verde.


## 4. COBERTURA Y EVIDENCIAS

En git hice primero los commits con las pruebas que fallaban en rojo y después los commits con las correcciones en el código fuente.

Comando: python -m pytest --cov=src.calculadora --cov=src.descuentos --cov=src.validador --cov-report=term-missing

```
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src/calculadora.py        44      0   100%
src/descuentos.py         58      0   100%
src/validador.py          67      0   100%
----------------------------------------------------
TOTAL                    169      0   100%

79 passed
```

En la primera medición, con las 27 pruebas iniciales, la cobertura era 84 % en calculadora, 67 % en descuentos y 60 % en validador. La columna de líneas sin cubrir me mostró qué casos faltaban y con eso armé la segunda tanda de pruebas.

# Evidencias de las ejecuciones (carpeta evidencias/): pytest_rojo.txt, pytest_verde.txt y cobertura.txt.

# Capturas de las ejecuciones (carpeta evidencias/): 01_pytest_rojo.txt, 02_pytest_verde_27.txt y 03_cobertura_100.txt.


## 5. REFLEXION FINAL

Lo que más me sirvió de este taller fue ver las pruebas fallando antes de arreglar nada. Con las pruebas en rojo supe exactamente dónde estaban los bugs, y no tuve que adivinar. El que más me llamó la atención fue el de calcular_precio_final: la función devolvía un número que parecía normal (109), y solo me di cuenta de que estaba mal porque hice la cuenta a mano y me dio 107.1. Ahí entendí que hay que calcular primero el resultado esperado y no confiar en lo que devuelve el código.

También vi que la cobertura sirve más como guía que como meta. Al principio tenía 84 %, 67 % y 60 %, y mirando qué líneas faltaban supe qué casos me hacían falta. Llegar al 100 % solo quiere decir que todas las líneas se ejecutaron, no que el código no tenga errores. Los bugs los encontré por los casos límite que escogí, como la lista de positivos, el número negativo y el 31 de febrero.

Lo más difícil fue el manejo de git y los errores del código. Tuve problemas con el token de GitHub para hacer el push y con la sangría de Python: mezclé tabulaciones con espacios al editar y me salió un TabError, y luego otro error de sintaxis que me obligó a restaurar el archivo original y volver a aplicar las correcciones. Eso me enseñó a revisar con git diff y con pytest antes de hacer cada commit. La próxima vez haría las pruebas de errores y casos límite desde el principio, no al final.
