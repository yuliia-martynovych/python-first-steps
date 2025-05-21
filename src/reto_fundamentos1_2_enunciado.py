# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

# print("Bienvenido al gestor de contactos")
# print("¿Qué quieres hacer?")
# print("1. Añadir contacto")
# print("2. Ver contactos")
# print("3. Buscar por nombre")
# print("4. Salir")
# contactos = []  # Lista para almacenar los contactos
# while True:
#     opcion = input("Selecciona una opción (1-4): ")
#     if opcion == "1":
#         nombre = input("Introduce el nombre: ")
#         edad = input("Introduce la edad: ")
#         ciudad = input("Introduce la ciudad: ")
#         contacto = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
#         contactos.append(contacto)
#         print(f"Contacto {nombre} añadido.")
#     elif opcion == "2":
#         print("Lista de contactos:")
#         for contacto in contactos:
#             print(f"Nombre: {contacto['nombre']} - Edad: {contacto['edad']} - Ciudad: {contacto['ciudad']}")
#     elif opcion == "3":
#         nombre_buscar = input("Introduce el nombre a buscar: ")
#         encontrado = False
#         for contacto in contactos:
#             if contacto["nombre"].lower() == nombre_buscar.lower():
#                 print(f"Contacto encontrado: Nombre: {contacto['nombre']} - Edad: {contacto['edad']} - Ciudad: {contacto['ciudad']}")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print(f"No se encontró el contacto con el nombre {nombre_buscar}.")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#         break
#     else:
#         print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")