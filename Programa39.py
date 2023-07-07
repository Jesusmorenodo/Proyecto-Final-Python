def calcular_area_triangulo(base,altura):
    area = (base*altura) / 2
    return area
print("\nPrograma 39.\nCalcula el area de un triangulo:")
base = float(input("escriba la base: "))
altura = float(input("escribe la altura: "))
area = calcular_area_triangulo(base, altura)
print("el area del triangulo es" , area)
print("Fin del Programa")