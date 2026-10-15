# Informe: Pruebas unitarias con pytest

## 1. Datos

* **Estudiante:** Maria Fernanda Gonzalez Arango
* **Repositorio (fork):** https://github.com/mafecitafer/pruebas_unitarias_devops
* **Módulos trabajados:** `calculadora`, `descuentos`, `validador` (carpeta `src/`)
* **Resultado final:** 79 pruebas en verde y 100 % de cobertura en los tres módulos (la meta era el 85 %)

---

## 2. Análisis por módulo

Organicé las pruebas usando la estructura AAA (*Arrange, Act, Assert*) y las fui sacando en dos tandas. Primero me enfoqué en buscar **errores** (casos límite y entradas raras que el programa debería rechazar o manejar bien) y después en conseguir **cobertura** (llegar a esas esquinas del código y mensajes de error que la primera tanda no tocaba).

* **calculadora (18 pruebas):** Probé lo básico de cada operación y, sobre todo, dónde se cae el código si uno no tiene cuidado: listas vacías, meter números negativos o valores que no están al inicio de la lista. Como las operaciones simples (`sumar`, `restar`) casi no fallan, me fijé más en las decisiones (`if`, bucles). Así salieron a flote los bugs en `minimo` (si le pasaba puras cosas positivas, devolvía 0 en vez del número menor) y en `raiz_cuadrada` (dejaba pasar los negativos).

* **descuentos (25 pruebas):** Aquí fui mezclando números fáciles de sacar a mano (por ejemplo: precio 100, 19 % de impuesto y 10 % de descuento) para revisar cada validación y los escalones por volumen (10, 20, 50 y 100 unidades). Haciendo la cuenta a mano de `calcular_precio_final` me dio 107.1, pero el programa escupía otra cosa; ahí descubrí que el impuesto se estaba calculando sobre el precio inicial y no sobre el valor ya rebajado.

* **validador (36 pruebas):** Para cada validador tiré al menos un caso bueno, uno vacío y uno que rompiera cada regla (correos sin arroba, claves sin mayúsculas, cédulas con letras, etc.). En `validar_fecha` probé fechas imposibles (tipo 31 de febrero o 29 de febrero en un año normal) comparadas con un bisiesto real, y me di cuenta de que la función tragaba cualquier cosa siempre y cuando el día estuviera entre 1 y 31.

* **Alcance:** No toqué `fibonacci`, `autenticacion`, `conversor`, `csv_parser`, `manipulador_texto`, `procesador_texto` ni `utils`. Como el taller pedía mínimo 3 bugs y el 85 % en lo trabajado, preferí concentrarme bien en tres módulos antes de hacer algo superficial en diez.

---

## 3. Bugs encontrados

| # | Módulo / función | Entrada que lo revela | Resultado erróneo | Resultado esperado | Corrección |
| - | - | - | - | - | - |
| 1 | `calculadora.minimo` | `[5, 3, 8]` | `0` | `3` | Empezar con `min_val = lista[0]` en vez de `0` |
| 2 | `calculadora.raiz_cuadrada` | `-4` | Da un número complejo sin avisar | `ValueError` | Lanzar un `ValueError` si `numero < 0` |
| 3 | `descuentos.calcular_precio_final` | `(100, 19, 10)` | `109.0` | `107.1` | Calcular el impuesto usando `precio_con_descuento` |
| 4 | `validador.validar_fecha` | `(31, 2, 2025)` y `(29, 2, 2023)` | `True` | `False` | Validar bien el día usando `calendar.monthrange(año, mes)[1]` |

**Evidencia de los fallos (pytest antes de corregir)**, guardada en `evidencias/pytest_rojo.txt`:

```text
FAILED tests/test_calculadora.py::test_raiz_cuadrada_de_negativo_lanza_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_calculadora.py::test_minimo_lista_de_positivos - assert 0 == 3
FAILED tests/test_descuentos.py::test_precio_final_impuesto_sobre_precio_descontado - assert 109.0 == 107.1 ± 1.1e-04
FAILED tests/test_validador.py::test_validar_fecha_31_de_febrero - assert True is False
FAILED tests/test_validador.py::test_validar_fecha_29_febrero_no_bisiesto - assert True is False
5 failed, 22 passed
```

**Captura 1.** `pytest` en rojo, antes de arreglar nada: 5 pruebas caídas por 4 bugs reales.
![pytest en rojo](evidencias/Cap 1cpytest_rojo.png)

**Captura 2.** Ya con los 4 bugs arreglados, las 27 pruebas originales pasan de largo (`27 passed`).
![pytest en verde](evidencias/Cap 2 pytest_verde_27.png)

---

## 4. Salida de cobertura (después de corregir)

Comando usado: `python -m pytest --cov=src.calculadora --cov=src.descuentos --cov=src.validador --cov-report=term-missing`  
Archivo: `evidencias/cobertura.txt`

```text
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src/calculadora.py        44      0   100%
src/descuentos.py         58      0   100%
src/validador.py          67      0   100%
----------------------------------------------------
TOTAL                    169      0   100%

79 passed
```

**Captura 3.** Cobertura final lista: 79 pruebas en verde y el 100 % en los tres módulos.
![cobertura](evidencias/Cap 3 cobertura100.png)

La primera vez que medí (solo con las 27 pruebas base) me dio 84 % en `calculadora`, 67 % en `descuentos` y 60 % en `validador`. Mirando la columna `Missing` supe exactamente qué líneas se estaban quedando por fuera (validaciones, rangos de volumen, etc.) y con eso armé la segunda tanda de pruebas para completar.

---

## 5. Reflexión final

Lo que más me dejó este taller es darme cuenta de que ver un fallo (*rojo*) en las pruebas no es un fracaso, sino una guía: los cinco errores del inicio me señalaron directo dónde estaba fallando el código antes de ponerme a modificar a ciegas. Lo del impuesto en `calcular_precio_final` me abrió los ojos porque la función parecía funcionar y devolvía un número "normal", pero al sacar la cuenta a mano me percaté del error. Eso me enseñó que una buena prueba nace de calcular uno mismo lo que debería salir, no de conformarse con lo que el programa responda inicialmente.

También entendí que el porcentaje de cobertura es una buena brújula, pero no una garantía absoluta. Empecé con 84 %, 67 % y 60 %, y la herramienta me ayudó a ver qué partes faltaban por probar. Sin embargo, llegar al 100 % solo significa que cada línea se ejecutó al menos una vez, no que el código sea invulnerable: los bugs reales los encontré pensando en los casos límite (listas de positivos, negativos, fechas raras), no por mirar métricas.

Si tuviera que hacerlo otra vez, escribiría las pruebas pensando en los casos límite desde el primer momento en lugar de dejarlos para el final. Además, me llevo un muy buen manejo del flujo de trabajo con git (hacer fork, commits ordenados por cada arreglo y sus respectivos push), que la verdad no tenía tan pulido.