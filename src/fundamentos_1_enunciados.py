# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
a = "Hola"
b=25 
c=3.14 
d=True
e = None

print("a:", type(a)) 
print("b:", type(b)) 
print("c:", type(c)) 
print("d:", type(d)) 
print("e:", type(e)) 

# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

s = "42"
num = int(s)
num = (num+8)
print(num)

num2 = str(100)
print (type(num2))
print('Tu puntuación final es:', num2)

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

nombre = "Juan"
edad = 30
print("Hola, me llamo", nombre, "y tengo", edad, "años")


nombre1 = input("¿Cuál es tu nombre? ")
edad1 = input("¿Cuántos años tienes? ")
print("Hola, me llamo", nombre, "y tengo", edad, "años")

# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
# x = "gato"
# y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

x = "gato"
y = "perro"

y, x = x, y
print("x:", x)
print("y:", y)

# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
pan = 1.50
leche = 1.24
huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

total = pan + leche + huevos
print("El total de la compra es:", total)

# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.
num = int(input("Introduce un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.

facecontrol = int(input("Introduce tu edad: "))
if facecontrol >= 18:
    print("Puedes entrar")
else:
    print("Acceso denegado")

# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

print ("Elige una opción:")
print ("1. Ver perfil")
print ("2. Editar perfil")
print ("3. Cerrar sesión")

option = input("Introduce el número de tu opción:")

if option == "1":
    print("Mostrando tu perfil...")
elif option == "2":
    print("Abriendo editor de perfil..")
elif option == "3":
    print("Cerrando sesión. ¡Hasta pronto!")

# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

type_detection = input("Escribe algo: ")
try:
    int(type_detection)
    print("Has escrito un número entero")
except ValueError:
    try:
        float(type_detection)
        print("Has escrito un número decimal")
    except ValueError:
        if isinstance(type_detection, str):
            print("Parece que es una cadena de texto")
        else:
            print("No sé qué es esto")


# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print("Elige una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Introduce el número de tu opción:")
if opcion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3": 
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("No se puede dividir entre cero")

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

clasificador = int(input("Introduce tu edad: "))
if clasificador < 0:
    print("Edad no válida")
elif clasificador < 3:
    print("Bebé")
elif clasificador > 3 and clasificador < 12:
    print("Infancia")
elif clasificador > 12 and clasificador < 18:
    print("Adolescencia")
elif clasificador > 18 and clasificador < 65:
    print("Adulto")
elif clasificador > 99:
    print("Senior")