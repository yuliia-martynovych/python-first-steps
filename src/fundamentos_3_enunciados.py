# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
def saludar():
    print("¡Hola, bienvenido/a!")
# Luego llama a la función una vez para comprobar que funciona.
saludar()

# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre) que imprima: "Hola, [nombre]!"

def saludar_persona(nombre):
    print(f"Hola, {nombre}!")
# Llama a la función dos veces con diferentes nombres.
saludar_persona("Julie")
saludar_persona("Teodor")

# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().
def sumar(a,b):
    return a + b
result = sumar(180, 20)
print(result)


# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y False si es impar.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Pruébala con varios números y muestra el resultado.

print(es_par(17820)) 
print(es_par(831))
print(es_par(984.64))
print(es_par(0))
print(es_par(-222))
print(es_par(-23))

# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."

def mensaje(nombre, edad):
    return f"Me llamo {nombre} y tengo {edad} años."

# Usa return y luego muestra el mensaje con print().
print(mensaje("Mateo",4))

# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b if b != 0 else "No se puede dividir por cero"

# Llama a cada una con un par de números y muestra los resultados.

print(sumar(30,20))
print(restar(100,50))
print(multiplicar(5,10))
print(dividir(100, 2))

# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede dividir por cero"

# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la edad que tendrás después de X años.

def edad_futura(edad_actual, años):
    return edad_actual + años

print(edad_futura(26,30))

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c) que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

def calcular_media(a, b, c):
    return (a + b + c) / 3
print(calcular_media(100, 400, 700))

# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión

def mostrar_menu():
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Cerrar sesión")

mostrar_menu()

# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *
# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L


def generar_contraseña(longitud):
    import random
    import string

    if longitud < 8:
        print("La longitud mínima de la contraseña es 8 caracteres.")
        return None

    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

