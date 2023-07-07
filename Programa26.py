def clf_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Isósceles"
    else:
        return "Escaleno"
print("\nPrograma 26.\nQue determine las calificaciones de los lados de un triangulo:")
l1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
l2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
l3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
cl = clf_triangulo(l1, l2, l3)
print("La clasificación del triángulo es:",cl)