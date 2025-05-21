print("Hola desde main.py")

# def calcular_area_rectangulo(base, altura):
#     return base * altura

# def calcular_area_cuadrado(lado):
#     return lado * lado

# def calcular_area_triangulo(base, altura):
#     return 0.5 * base * altura

def calcular_area(figura, base=None, altura=None, lado=None):
    if figura == "rectangulo":
        return base * altura
    elif figura == "cuadrado":
        return lado * lado
    elif figura == "triangulo":
        return 0.5 * base * altura
    else:
        raise ValueError("Figura no reconocida")
    
calcular_area("rectangulo", base=5, altura=10)
calcular_area("cuadrado", lado=4)
calcular_area("triangulo", base=5, altura=10)