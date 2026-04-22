# GA1-220501093-04-AA1-EV01 – Fundamentos de Python: variables, operadores y manipulación de cadenas

**Autor:** Jose Manuel Ruiz Zapata
**Ficha:** 3144585
---

# Sección 1 – La función `print()`

## Laboratorio 1: Trabajando con la función `print()`

### 1. Imprimir "¡Hola, Mundo!" con comillas dobles
print("¡Hola, Mundo!")

Muestra en la pantalla el texto ¡Hola, Mundo!.
print() es la orden que le dice a Python que muestre algo. Las comillas dobles le indican que lo que está dentro es texto, no órdenes.

### 2. Imprimir el nombre propio
print("Jose Ruiz")

En la terminal muestra el texto que se puso entre comillas Jose Ruiz.

### 3. Error al quitar las comillas dobles (línea comentada para que no falle el programa)
#### print(¡Hola, Mundo!)

En la ejecucion aparece:
  File "c:\SENA\fundamentos_python\src\seccion1\lab1_print.py", line 1
    print(¡Hola, Mundo!)
          ^
SyntaxError: invalid character '¡' (U+00A1)

El signo ¡ no es una letra ni un número. Python solo deja que los nombres de variables que tenga letras, números y guiones. El signo ¡ no está permitido,entonces Python lo que hace es que se detiene cuando lo lee y por eso aparece: "carácter inválido".


### 4. Error al quitar los paréntesis (línea comentada)
#### print "¡Hola, Mundo!"  

Error que aparece en la consola:

  File "c:\SENA\fundamentos_python\src\seccion1\lab1_print.py", line 3
    print"¡Hola, Mundo!"
    ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

en la consola claramente dice que faltarian los parentesis al llamar a print y tembien aparece que si quise decir print(...)

Al escribir print"¡Hola, Mundo!" sin paréntesis, Python no entiende que es lo que se quier mostrar. Por eso señala con el símbolo ^ justo el lugar donde está el problema y te sugiere la solución: agregar los paréntesis.

### 5. Experimentos

#### print('¡Hola, Mundo!')     
En consola aparece ¡Hola, Mundo!    
Funciona igual que las comillas dobles. Las dos son válidas para texto.

#### print("Hola"); print("Mundo")  
En cosola aparece  
Hola
Mundo      
Los dos se ejecutan uno a la vez y cada print muestra su texto y luego salta de línea.

#### print("Línea 1")                           
#### print("Línea 2") 
En consola aparece
Linea 1
Linea 2
Es la forma más normal y ordenada. Cada print va en su propia línea y se lee mejor.

## Laboratorio 2: La función `print()` y sus argumentos `sep` y `end`

El editor muestra algo como esto:

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

La salida es: Programming***Essentials***in...Python

### Explicacion de los argumentos

#### sep
Define el texto que se pone entre los argumentos que se le da a print().
Por defecto: sep=" " (un espacio).
En el codigo seria: sep="***" hace que entre "Programming", "Essentials" y "in" aparezcan tres asteriscos, así: Programming***Essentials***in.

#### end
Define el texto que se pone al final de todo lo que imprime print(), justo antes de que termine la línea.
end="\n" esto lo que hace es un salto de línea.
En el codigo seria: end="..." hace que después de "in" se agreguen tres puntos, pero sin saltar de línea.

## Laboratorio 3: Dando formato a la salida

### Código original
El programa dibuja una flecha con asteriscos:

```python
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```

Si se ejecuta mostraria una flecha apuntando hacia arriba:

```python
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****
```

### Cambios del codigo

#### Minimizar el número de print() usando \n
En lugar de usar 8 print(), se puede usar uno solo insertando saltos de línea \n dentro de la cadena, el resultado es el mismo, mostrando la flecha hacia arriba usando este codigo:

```python
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
```

#### Hacer la flecha el doble de grande
Para agrandar la flecha, puedes duplicar cada línea pero con cuidado de que los espacios también se dupliquen. Una forma sencilla es multiplicar las cadenas:

```python
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****       *****")
print("  *           *")
print("  *           *")
print("  *           *")
print("  ***********")
```      
Salida de la cosola:

```python
        *
       * *
      *   *
     *     *
    *       *
   *         *
  *           *
 *             *
*****       *****
  *           *
  *           *
  *           *
   ***********
```

Se duplicaron los espacios de la izquierda y también se duplicó el ancho de la flecha (más asteriscos en las líneas horizontales). La forma es la misma, pero ahora mide el doble en alto y ancho.

#### Duplicar la flecha, colocando ambas una al lado de la otra

```python
print("    *" * 2)
print("   * *" * 2)
print("  *   *" * 2)
print(" *     *" * 2)
print("***   ***" * 2)
print("  *   *" * 2)
print("  *   *" * 2)
print("  *****" * 2)
```

Multiplicar una cadena por 2 la repite dos veces. Así cada línea original se duplica, y el resultado son dos flechas completas, una al lado de la otra.

Salida de la consola:

```python
    *    *
   * *   * *
  *   *  *   *
 *     * *     *
***   ******   ***
  *   *  *   *
  *   *  *   *
  *****  *****
```

#### Eliminar una comilla

```python
  File "c:\SENA\fundamentos_python\src\seccion1\lab3.py", line 35
    print("    *)
          ^
SyntaxError: unterminated string literal (detected at line 35)
```

Falta la comilla de cierre. Python señala el error al final de la línea porque esperaba encontrar " pero la línea terminó. El error real está donde falta la comilla, pero Python lo detecta al llegar al final sin encontrarla.

#### Eliminar un paréntesis

```python
  File "c:\SENA\fundamentos_python\src\seccion1\lab3.py", line 39
    print("***   ***"
         ^
SyntaxError: '(' was never closed
```

Falta el paréntesis de cierre ). Python espero el paréntesis de cierre. El error está en la línea donde se abrio el paréntesis pero no se cerro.

#### Cambiar print a Print
```python
  File "c:\SENA\fundamentos_python\src\seccion1\lab3.py", line 44, in <module>
    Print("    *")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Python distingue mayúsculas de minúsculas. La función correcta se escribe print todo en minúsculas. Al escribir Print, Python lo que hace es buscar una función o variable con ese nombre, no la encuentra y lanza el error.

#### Reemplazar comillas dobles por apóstrofes

```python
print('    *')
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```

Las comillas simples ' y las comillas dobles " son equivalentes en Python para crear cadenas. El cambio no produce error, siempre que abras y cierres con el mismo tipo.

#### Codigo incorrecto

```python
print("    *')
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```

Este seria el error que aparece en cosola:

```python
  File "c:\SENA\fundamentos_python\src\seccion1\lab3.py", line 53
    print("    *')
          ^
SyntaxError: unterminated string literal (detected at line 53)
```

Si se abre con " se tiene que cerrar con ". Mezclar los dos tipos hace que Python reconozca dónde termina la cadena.

# Sección 2 – Literales de Python

## Laboratorio: Literales de Python – Cadenas

Escribe un **solo** `print()` que produzca exactamente esta salida: 

```python
"Estoy"""aprendiendo"""""Python"""
```

### Solución

```python
print("\"Estoy\"\"\"aprendiendo\"\"\"\"\"Python\"\"\"")
```

Para que Python muestre una comilla doble dentro de una cadena, hay que escaparla con la diagonal invertida \".

La cadena completa empieza y termina con ". Todo lo que está dentro se interpreta como texto.

Cuando se quiere una comilla doble visible en la salida, escribimos \".

Las comillas que pide la salida:

Una al inicio: \", luego Estoy, tres comillas seguidas: \"\"\", luego aprendiendo, cinco comillas seguidas: \"\"\"\"\", luego Python, tres comillas al final: \"\"\"

# Sección 3 - Operadores: herramientas de manipulación de datos

### Ejercicio 1

**Expresión:**  
`5 + 3 * 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. La multiplicación (*) tiene mayor prioridad que la suma (+).
2. Primero se calcula `3 * 2 = 6`.
3. Luego se suma `5 + 6 = 11`.

**Resultado:** `11`

**Comprobación en Python:**

```python
print(5 + 3 * 2)
```

## Ejercicio 2

**Expresión:**
`8 / 2 + 4 * 3`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. La división (/) y la multiplicación (*) tienen la misma prioridad y se evalúan de izquierda a derecha.
2. Primero 8 / 2 = 4.0.
3. Luego 4 * 3 = 12.
4. Finalmente 4.0 + 12 = 16.0.

**Resultado:** 16.0

**Comprobación en Python:**

```python
print(8 / 2 + 4 * 3)
```

## Ejercicio 3

**Expresión:**
`(7 + 3) * 2 - 5`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Los paréntesis tienen la máxima prioridad. Primero (7 + 3) = 10.
2. Luego la multiplicación: 10 * 2 = 20.
3. Finalmente la resta: 20 - 5 = 15.

**Resultado:** 15

**Comprobación en Python:**

```python
print((7 + 3) * 2 - 5)
```

## Ejercicio 4

**Expresión:**
`10 - 4 + 2 * 3`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. La multiplicación tiene prioridad: 2 * 3 = 6.
2. Luego 10 - 4 = 6.
3. Luego 6 + 6 = 12.

**Resultado:** 12

**Comprobación en Python:**

```python
print(10 - 4 + 2 * 3)
```

## Ejercicio 5

**Expresión:**
`(10 / 2) * (3 + 2) - 4`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Paréntesis: 10 / 2 = 5.0 y 3 + 2 = 5.
2. Multiplicación: 5.0 * 5 = 25.0.
3. Resta: 25.0 - 4 = 21.0.

**Resultado:** 21.0

**Comprobación en Python:**

```python
print((10 / 2) * (3 + 2) - 4)
```

## Ejercicio 6

**Expresión:**
2 + 3 * (4 - 1)

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Paréntesis: 4 - 1 = 3.
2. Multiplicación: 3 * 3 = 9.
3. Suma: 2 + 9 = 11.

**Resultado:** 11

**Comprobación en Python:**

```python
print(2 + 3 * (4 - 1))
```

## Ejercicio 7

**Expresión:**
5 * 2 ** 3

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Exponenciación primero: 2 ** 3 = 8.
2. Multiplicación: 5 * 8 = 40.

**Resultado:** 40

**Comprobación en Python:**
```python
print(5 * 2 ** 3)
```

## Ejercicio 8

**Expresión:**
6 + 4 / 2 ** 2

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Exponenciación: 2 ** 2 = 4.
2. División: 4 / 4 = 1.0.
3. Suma: 6 + 1.0 = 7.0.

**Resultado:** 7.0

**Comprobación en Python:**

```python
print(6 + 4 / 2 ** 2)
```

## Ejercicio 9

**Expresión:**
10 % 3 + 2 * 5

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. 10 % 3 = 1.
2. 2 * 5 = 10.
3. Suma: 1 + 10 = 11.

**Resultado:** 11

**Comprobación en Python:**

```python
print(10 % 3 + 2 * 5)
```

## Ejercicio 10

**Expresión:**
(8 + 2) * 3 ** 2

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Paréntesis: 8 + 2 = 10.
2. Exponenciación: 3 ** 2 = 9.
3. Multiplicación: 10 * 9 = 90.

**Resultado:** 90

**Comprobación en Python:**

```python
print((8 + 2) * 3 ** 2)
```

## Ejercicio 11

**Expresión:**
7 + 2 * (3 + 5) / 4

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Paréntesis: 3 + 5 = 8.
2. Multiplicación: 2 * 8 = 16.
3. División: 16 / 4 = 4.0.
4. Suma: 7 + 4.0 = 11.0.

**Resultado:** 11.0

**Comprobación en Python:**

```python
print(7 + 2 * (3 + 5) / 4)
```

## Ejercicio 12

**Expresión:**
2 ** 3 * 4 / 2

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Exponenciación: 2 ** 3 = 8.
2. Multiplicación: 8 * 4 = 32.
3. División: 32 / 2 = 16.0.

**Resultado:** 16.0

**Comprobación en Python:**

```python
print(2 ** 3 * 4 / 2)
```

## Ejercicio 13

**Expresión:**
9 - 6 + 3 ** 2

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Exponenciación: 3 ** 2 = 9.
2. 9 - 6 = 3.
3. 3 + 9 = 12.

**Resultado:** 12

**Comprobación en Python:**

```python
print(9 - 6 + 3 ** 2)
```

## Ejercicio 14

**Expresión:**
(7 - 2) * 5 + 3 ** 2

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Paréntesis: 7 - 2 = 5.
2. Exponenciación: 3 ** 2 = 9.
3. Multiplicación: 5 * 5 = 25.
4. Suma: 25 + 9 = 34.

**Resultado:** 34

**Comprobación en Python:**

```python
print((7 - 2) * 5 + 3 ** 2)
```

## Ejercicio 15

**Expresión:**
4 * 2 ** 3 / 8 + 1

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución paso a paso:**

1. Exponenciación: 2 ** 3 = 8.
2. Multiplicación: 4 * 8 = 32.
3. División: 32 / 8 = 4.0.
4. Suma: 4.0 + 1 = 5.0.

**Resultado:** 5.0

**Comprobación en Python:**

```python
print(4 * 2 ** 3 / 8 + 1)
```
# Sección 4 – Variables

## Laboratorio: Variables (las manzanas de Juan, María y Adán)

- Juan tenía **3** manzanas.
- María tenía **5** manzanas.
- Adán tenía **6** manzanas.

Se deben crear variables, asignar los valores, imprimirlos, sumarlos y mostrar el total.

#### Código solución

```python
# Asignar valores

john = 3
mary = 5
adam = 6

# Imprimir las variables separadas por comas
print(john, mary, adam, sep=",")

# Sumar todas las manzanas
total_apples = john + mary + adam

# Imprimir el total
print(total_apples)
```

## Explicación paso a paso
**Crear las variables**

john = 3 → se crea la variable john y se guarda el número 3.
Lo mismo para mary y adam.

**Imprimir las tres variables en una línea, separadas por comas**

print(john, mary, adam, sep=",")

sep="," hace que entre cada valor se ponga una coma, sin espacios.

La salida será: 3,5,6

**Sumar los valores**

total_apples = john + mary + adam

Se calcula 3 + 5 + 6 = 14 y se guarda en total_apples.

**Imprimir el total**

print(total_apples) lo que muestra 14.

**Salida esperada**

3,5,6
14

## Experimentos adicionales

**Mostrar el total con un mensaje:**

```python
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")

total_apples = john + mary + adam

print("Número total de manzanas:", total_apples)
```

Salida: Número total de manzanas: 14

### Nuevas variables

```python
naranjas = 10
peras = 7
frutas_total = naranjas + peras
```

### Operaciones aritméticas

```python
suma = john + naranjas
resta = mary - adam
multiplicacion = peras * 2
division = total_apples / 3
division_entera = total_apples // 3
modulo = total_apples % 3
```

### Mostrar resultados

```python
print("Suma de john + naranjas:", suma)
print("Resta de mary - adam:", resta)
print("Multiplicación peras * 2:", multiplicacion)
print("División total_apples / 3:", division)
print("División entera total_apples // 3:", division_entera)
print("Residuo total_apples % 3:", modulo)
```

### Cadena con entero en la misma línea

```python
print("Número total de manzanas:", total_apples)
print("Total de frutas: " + str(frutas_total))
```

### Salida de los experimentos:
Suma de john + naranjas: 13
Resta de mary - adam: -1
Multiplicación peras * 2: 14
División total_apples / 3: 4.666666666666667
División entera total_apples // 3: 4
Residuo total_apples % 3: 2
Número total de manzanas: 14
Total de frutas: 17

## Laboratorio: Variables – un convertidor simple (millas a kilómetros)

Se debe completar un programa que convierta:
- Millas a kilómetros (1 milla = 1.61 km)
- Kilómetros a millas

### Código solución

```python
kilometers = 12.25
miles = 7.38
```

### Conversiones

```python
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
```

### Salida con round() para redondear a 2 decimales

```python
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

## Explicación paso a paso
**Convertir millas a kilómetros**

miles_to_kilometers = miles * 1.61

Multiplicamos 7.38 × 1.61 = 11.8818.
Luego round(..., 2) lo deja en 11.88.

**Convertir kilómetros a millas**

kilometers_to_miles = kilometers / 1.61

Dividimos 12.25 ÷ 1.61 ≈ 7.608...
Redondeado a 2 decimales da 7.61.

**Uso de round()**

La función round(valor, decimales) redondea el número a la cantidad de decimales que se indique.

Si no se pone el segundo argumento, redondea al entero más cercano.

**Múltiples argumentos en print()**

print(miles, "millas son", round(...), "kilómetros")

La función print() acepta varios argumentos separados por coma y los muestra en una sola línea,
añadiendo un espacio entre ellos automáticamente.

### Experimentos adicionales

#### Convertidor USD a EUR

```python
usd = 100
tipo_cambio = 0.92
eur = usd * tipo_cambio
print(usd, "USD son", round(eur, 2), "EUR")
```

#### Convertidor Celsius a Fahrenheit

```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(celsius, "°C son", round(fahrenheit, 1), "°F")
```

#### Probando round() sin decimales y con diferentes precisiones

```python
numero = 3.14159
print("Original:", numero)
print("Redondeado a 0 decimales:", round(numero))
print("Redondeado a 2 decimales:", round(numero, 2))
print("Redondeado a 3 decimales:", round(numero, 3))
```

#### Formas de combinar texto y números

```python
total_apples = 14
print("Total de manzanas:", total_apples)
print("Total: " + str(total_apples) + " manzanas")
print(f"Tenemos {total_apples} manzanas")
```  
#### Explicación de cada experimento

**Convertidor USD a EUR**

Se multiplica la cantidad en USD por el tipo de cambio (0.92).

round(eur, 2) redondea a 2 decimales porque el resultado puede tener muchos decimales.

**Convertidor Celsius a Fahrenheit**

Fórmula: °F = °C × 9/5 + 32.

Se usa round(..., 1) para mostrar solo un decimal, suficiente para temperaturas.

**Experimentos con round()**

round(numero) sin segundo argumento redondea al entero más cercano (3).

Con ,2 da dos decimales (3.14), con ,3 da tres decimales (3.142).

Útil para controlar la precisión de los resultados.

**Combinar cadenas y números**

Coma en print(): añade espacio automático.

Concatenación con +: requiere convertir el número a cadena con str().

f-string (recomendado): se escribe f"texto {variable}", es más legible y moderno.