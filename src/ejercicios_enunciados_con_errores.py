# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)

# Diccionario para guardar las películas y sus votos
# peliculas = {}

# def anadir_pelicula():
#     nombre = input("Escribe el nombre de la película: ")
#     if nombre in peliculas:
#         print("Esa película ya está registrada.")
#     else:
#         peliculas[nombre] = 0
#         print(f"Película '{nombre}' añadida.")

# def votar():
#     if not peliculas:
#         print("No hay películas registradas. Añade una primero.")
#         return

#     print("\nPelículas disponibles para votar:")
#     lista = list(peliculas.keys())  
#     for i, nombre in enumerate(lista, start=1):
#         print(f"{i}. {nombre}")

#     try:
#         opcion = int(input("Escribe el número de la película que quieres votar: "))
#         if 1 <= opcion <= len(lista):
#             seleccionada = lista[opcion - 1]
#             peliculas[seleccionada] += 1
#             print(f"¡Gracias por tu voto por '{seleccionada}'!")
#         else:
#             print("Número inválido. Intenta otra vez.")
#     except ValueError:
#         print("Eso no es un número. Intenta otra vez.")

# def mostrar_resultados():
#     if not peliculas:
#         print("No hay películas registradas todavía.")
#     else:
#         print("\nResultados de la votación:")
#         for nombre, votos in peliculas.items():
#             print(f"{nombre}: {votos} voto(s)")

# def menu():
#     while True:
#         print("\n--- SISTEMA DE VOTACIONES ---")
#         print("1. Añadir película")
#         print("2. Votar por una película")
#         print("3. Mostrar resultados")
#         print("4. Salir")

#         opcion = input("Elige una opción (1-4): ")

#         if opcion == "1":
#             anadir_pelicula()
#         elif opcion == "2":
#             votar()
#         elif opcion == "3":
#             mostrar_resultados()
#         elif opcion == "4":
#             print("¡Hasta luego! Gracias por participar.")
#             break
#         else:
#             print("Opción no válida. Inténtalo de nuevo.")

# menu()


# 🧪 Ejercicios – Consola + Buenas Pr


# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena (TypeError o AttributeError)

# lista_nombres = ["  juan ", "maria", "PEPE", "Ana", "maria", "  juan ", "pepe"]
# def limpiar_nombres(nombres):
#     try:
#         nombres_limpios = [nombre.strip().title() for nombre in nombres if isinstance(nombre, str)]
#         nombres_unicos = sorted(set(nombres_limpios))
#         return nombres_unicos
#     except Exception as e:
#         print(f"Error al limpiar los nombres: {e}")
#         return []
# nombres_limpios = limpiar_nombres(lista_nombres)
# print("Lista de nombres únicos y limpios:")
# for nombre in nombres_limpios:
#     print(nombre)
    

# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

# print("Bienvenido al analizador de texto.")
# texto = input("Introduce un párrafo: ")
# if not texto.strip():
#     raise ValueError("El texto no puede estar vacío.")
# palabras = texto.split()
# contador_palabras = {}
# for palabra in palabras:
#     palabra = palabra.lower()
#     if palabra in contador_palabras:
#         contador_palabras[palabra] += 1
#     else:
#         contador_palabras[palabra] = 1
# palabra_mas_repetida = max(contador_palabras, key=contador_palabras.get)
# print(f"El párrafo contiene {len(palabras)} palabras.")
# print("Frecuencia de palabras:")
# for palabra, frecuencia in contador_palabras.items():
#     print(f"{palabra}: {frecuencia} vez/veces")
# print(f"La palabra más repetida es '{palabra_mas_repetida}' con {contador_palabras[palabra_mas_repetida]} repeticiones.")



# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar si el producto no existe.

inventario = {}
def anadir_producto():
    nombre = input("Nombre del producto: ").strip().lower()
    if nombre in inventario:
        print("El producto ya existe.")
    else:
        try:
            stock = int(input("Stock: "))
            precio = float(input("Precio: "))
            inventario[nombre] = {"stock": stock, "precio": precio}
            print(f"Producto '{nombre}' añadido.")
        except ValueError:
            print("Error: Stock y precio deben ser números.")
def actualizar_stock():
    nombre = input("Nombre del producto a actualizar: ")
    if nombre not in inventario:
        print("El producto no existe.")
    else:
        try:
            nuevo_stock = int(input("Nuevo stock: "))
            inventario[nombre]["stock"] = nuevo_stock
            print(f"Stock de '{nombre}' actualizado a {nuevo_stock}.")
        except ValueError:
            print("Error: Stock debe ser un número.")
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    if nombre not in inventario:
        print("El producto no existe.")
    else:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado.")
def ver_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for nombre, datos in inventario.items():
            print(f"{nombre}: Stock = {datos['stock']}, Precio = {datos['precio']}")
def menu_inventario():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Actualizar stock")
        print("3. Eliminar producto")
        print("4. Ver inventario")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            anadir_producto()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            ver_inventario()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
menu_inventario()

# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)

print("Bienvenido al generador de alias seguro.")
nombre = input("Introduce tu nombre: ").strip()
apellido = input("Introduce tu apellido: ").strip()
if len(nombre) < 2 or len(apellido) < 3:
    raise ValueError("El nombre debe tener al menos 2 letras y el apellido al menos 3 letras.")
import random
import string
numero_aleatorio = random.randint(10, 99)
simbolo_aleatorio = random.choice(string.punctuation)
alias = f"{apellido[:3].upper()}{nombre[:2].lower()}{numero_aleatorio}{simbolo_aleatorio}"
print(f"Tu alias seguro es: {alias}")

# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

print("Bienvenido al comprobador de contraseñas seguras.")
contraseña = input("Introduce una contraseña: ").strip()
if len(contraseña) < 8:
    raise ValueError("La contraseña debe tener al menos 8 caracteres.")
if not any(char.isupper() for char in contraseña):
    raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
if not any(char.islower() for char in contraseña):
    raise ValueError("La contraseña debe contener al menos una letra minúscula.")
if not any(char.isdigit() for char in contraseña):
    raise ValueError("La contraseña debe contener al menos un número.")
print("La contraseña es segura.")


# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)

print("Bienvenido al simulador de reservas de hotel.")
habitaciones = {f"10{i}": None for i in range(1, 11)}
def ver_habitaciones_disponibles():
    print("Habitaciones disponibles:")
    for habitacion, nombre in habitaciones.items():
        if nombre is None:
            print(habitacion)
def reservar_habitacion():
    ver_habitaciones_disponibles()
    habitacion = input("Introduce el número de habitación a reservar: ").strip()
    if habitacion not in habitaciones:
        print("Habitación no válida.")
        return
    if habitaciones[habitacion] is not None:
        print("La habitación ya está reservada.")
        return
    nombre = input("Introduce tu nombre: ").strip()
    habitaciones[habitacion] = nombre
    print(f"Reserva confirmada para {nombre} en la habitación {habitacion}.")
def cancelar_reserva():
    habitacion = input("Introduce el número de habitación a cancelar: ").strip()
    if habitacion not in habitaciones:
        print("Habitación no válida.")
        return
    if habitaciones[habitacion] is None:
        print("No hay reserva para esta habitación.")
        return
    habitaciones[habitacion] = None
    print(f"Reserva cancelada para la habitación {habitacion}.")
def ver_reservas_confirmadas():
    print("Reservas confirmadas:")
    for habitacion, nombre in habitaciones.items():
        if nombre is not None:
            print(f"{habitacion}: {nombre}")
def menu_reservas():
    while True:
        print("\n--- MENÚ DE RESERVAS ---")
        print("1. Ver habitaciones disponibles")
        print("2. Reservar habitación")
        print("3. Cancelar reserva")
        print("4. Ver reservas confirmadas")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            ver_habitaciones_disponibles()
        elif opcion == "2":
            reservar_habitacion()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            ver_reservas_confirmadas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
menu_reservas()