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