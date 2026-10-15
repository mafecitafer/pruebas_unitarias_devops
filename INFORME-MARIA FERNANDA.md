# Informe: Pruebas unitarias con pytest



## 1\. Datos

* **Estudiante:** Maria Fernanda Gonzalez Arango
* **Repositorio (fork):** https://github.com/mafecitafer/pruebas\_unitarias\_devops
* **Módulos trabajados:** `calculadora`, `descuentos`, `validador` (carpeta `src/`)
* **Resultado final:** 79 pruebas en verde y 100 % de cobertura en los tres módulos (meta: 85 %)



## 2\. Análisis por módulo



Escribí las pruebas con estructura AAA (Arrange, Act, Assert) en dos tandas. La primera buscó **errores**: casos límite y entradas que el código debía rechazar o resolver de forma especial. La segunda buscó **cobertura**: ramas y mensajes de error que la primera no ejecutaba.



**calculadora (18 pruebas).** Probé un caso normal por cada operación y, sobre todo, los puntos donde una función puede fallar en silencio: listas vacías, números negativos y valores que no son los primeros de la lista. El criterio fue ir donde el código toma decisiones (`if`, bucles, inicialización), porque las operaciones aritméticas simples (`sumar`, `restar`) casi no tienen margen de error. Así aparecieron los bugs de `minimo` (una lista de positivos devolvía 0) y de `raiz\_cuadrada` (aceptaba negativos).



**descuentos (25 pruebas).** El criterio fue combinar cálculos con números fáciles de verificar a mano (precio 100, impuesto 19 %, descuento 10 %) y recorrer cada validación de entrada y cada escalón del descuento por volumen (10, 20, 50 y 100 unidades). Verificar a mano el resultado esperado de `calcular\_precio\_final` (107.1) fue lo que reveló que el impuesto se calculaba sobre el precio original y no sobre el precio ya descontado.



**validador (36 pruebas).** Para cada validador probé al menos un caso válido, uno vacío y uno que viola cada regla (sin arroba, contraseña sin mayúscula, cédula con letras, etc.), de modo que cada condición del código tuviera su propia prueba. En `validar\_fecha` probé fechas imposibles (31 de febrero, 29 de febrero en año no bisiesto) y, como contraste, un año bisiesto válido. Con ellas apareció que la función solo revisaba que el día estuviera entre 1 y 31.

**Alcance.** No trabajé `fibonacci`, `autenticacion`, `conversor`, `csv\_parser`, `manipulador\_texto`, `procesador\_texto` ni `utils`. El taller pide mínimo 3 bugs y 85 % en los módulos trabajados, y preferí profundizar en tres módulos antes que cubrir diez de forma superficial.



## 3\. Bugs encontrados

|#|Módulo / función|Entrada que lo revela|Resultado erróneo|Resultado esperado|Corrección|
|-|-|-|-|-|-|
|1|`calculadora.minimo`|`\[5, 3, 8]`|`0`|`3`|Inicializar con `min\_val = lista\[0]` en lugar de `0`|
|2|`calculadora.raiz\_cuadrada`|`-4`|Devuelve un número complejo, sin error|`ValueError`|Lanzar `ValueError` si `numero < 0`|
|3|`descuentos.calcular\_precio\_final`|`(100, 19, 10)`|`109.0`|`107.1`|Calcular el impuesto sobre `precio\_con\_descuento`|
|4|`validador.validar\_fecha`|`(31, 2, 2025)` y `(29, 2, 2023)`|`True`|`False`|Validar el día con `calendar.monthrange(año, mes)\[1]`|





**Evidencia de los fallos (pytest antes de corregir)**, guardada en `evidencias/pytest\_rojo.txt`:

```
FAILED tests/test\_calculadora.py::test\_raiz\_cuadrada\_de\_negativo\_lanza\_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test\_calculadora.py::test\_minimo\_lista\_de\_positivos - assert 0 == 3
FAILED tests/test\_descuentos.py::test\_precio\_final\_impuesto\_sobre\_precio\_descontado - assert 109.0 == 107.1 ± 1.1e-04
FAILED tests/test\_validador.py::test\_validar\_fecha\_31\_de\_febrero - assert True is False
FAILED tests/test\_validador.py::test\_validar\_fecha\_29\_febrero\_no\_bisiesto - assert True is False
5 failed, 22 passed
```

**Captura 1.** `pytest` en rojo, antes de corregir: 5 pruebas fallan por 4 bugs reales.

!\[pytest en rojo](evidencias/Cap 1cpytest\_rojo.png)

**Captura 2.** Después de corregir los 4 bugs, las 27 pruebas originales pasan (`27 passed`).

!\[pytest en verde](evidencias/Cap 2 pytest\_verde\_27.png)



## 4\. Salida de cobertura (después de corregir)

Comando: `python -m pytest --cov=src.calculadora --cov=src.descuentos --cov=src.validador --cov-report=term-missing`
Archivo: `evidencias/cobertura.txt`

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

**Captura 3.** Salida de cobertura final: 79 pruebas en verde y 100 % en los tres módulos.

!\[cobertura](evidencias/Cap 3 cobertura100.png)

La primera medición (con solo las 27 pruebas iniciales) dio 84 % en `calculadora`, 67 % en `descuentos` y 60 % en `validador`. La columna `Missing` mostró qué líneas no se ejecutaban (validaciones de entrada, escalones de volumen, funciones sin probar) y con eso diseñé la segunda tanda de pruebas.



## 5\. Reflexión final



Lo que más me enseñó este taller es que una prueba en rojo es una herramienta útil, no un fracaso: los cinco fallos iniciales me mostraron exactamente dónde estaban los bugs antes de tocar el código. El caso del impuesto en `calcular\_precio\_final` me llamó la atención porque la función "funcionaba" y devolvía un número razonable, y solo vi el error al calcular a mano el resultado esperado (107.1 frente a 109). Eso me hizo ver que una buena prueba parte de calcular el resultado correcto por mi cuenta, y no de copiar lo que devuelve el programa.



También aprendí que la cobertura es un buen mapa, pero no una garantía. Mi primera medición dio 84 %, 67 % y 60 %, y la columna `Missing` me indicó qué ramas nunca se ejecutaban, así que pude completar las pruebas con criterio. Aun así, llegar al 100 % solo significa que cada línea se ejecutó al menos una vez, no que el código esté libre de errores: los bugs aparecieron por los casos límite que elegí (listas de positivos, números negativos, fechas imposibles), no por el porcentaje.



La próxima vez escribiría las pruebas desde el principio pensando en los casos límite de cada función, y no dejaría para el final los casos de error. Además me llevo el flujo completo de trabajo con git (fork, commits claros por cada corrección, push), que no había usado de forma tan ordenada.

