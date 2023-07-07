def calcular_a_trapesio ():
    A = B1 + B2 * Alt / 2
    return (A)
print("\nPrograma 6\nQue calcula el area de un trapesio:")
B1 = float(input("Escriba el valor de base 1: "))
B2 = float(input("Escriba el valor de base 2: "))
Alt = float(input("Escriba el valor de la Altura: "))
A = calcular_a_trapesio ()
print("El area de un trapesio es de: ", A)