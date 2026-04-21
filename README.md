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
