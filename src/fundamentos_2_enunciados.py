# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

fruits = ["manzana", "banana", "naranja", "uva", "kiwi"]
print(f"Primer elemento: {fruits[0]}")
print(f"Último elemento: {fruits[-1]}")

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

fruits.append("fresa")  # Añadir un nuevo elemento
fruits.remove("banana")  # Eliminar un elemento
print(f"Lista actualizada: {fruits}")


# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

numbers = [5, 2, 9, 1, 5, 6]
print(f"Números desordenados: {numbers}")
numbers.sort()  # Ordenar de menor a mayor
print(f"Números ordenados: {numbers}")

# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordinates = (40.7128, -74.0060)  # Coordenadas de Nueva York
print(f"Coordenadas: {coordinates}")


# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

fixed_tuple = (1, 2, 3)
try:
    fixed_tuple[0] = 10  # Intentar cambiar un elemento
except TypeError as e:
    print(f"Error: {e}")

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

user = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario de usuario: {user}")

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

user["ciudad"] = "Barcelona"  # Cambiar el valor de ciudad
user["email"] = "juan@gmail.com"  # Añadir nueva clave
print(f"Diccionario actualizado: {user}")

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

for key, value in user.items():
    print(f"{key}: {value}")

# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

names = ["Juan", "Ana", "Juan", "Pedro", "Ana"]
unique_names = set(names)  # Crear un set para eliminar duplicados
print(f"Nombres únicos: {unique_names}")

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
difference = set_A - set_B  # Elementos en A pero no en B
print(f"Elementos en A pero no en B: {difference}")

# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

hobbies = {
    "Juan": ["fútbol", "cine"],
    "Ana": ["lectura", "pintura"],
    "Pedro": ["música", "videojuegos"]
}
hobbies["Juan"].append("correr")  # Añadir un nuevo hobby a Juan
print(f"Hobbies de Juan: {hobbies['Juan']}")
print(f"Hobbies de Ana: {hobbies['Ana']}")
print(f"Hobbies de Pedro: {hobbies['Pedro']}")

