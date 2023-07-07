def ecuaciones_abc_1 ():
    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)
    return (c1, c2, c3, c4, c5)
print ("\nPrograma 9.\nQue resuelve ecuaciones:")
a = float(input("Escriba el valor de a: "))
b = float(input("Escriba el valor de b: "))
c = float(input("Escriba el valor de c: "))
(c1, c2, c3, c4, c5) = ecuaciones_abc_1 ()
print("El valor de c1 es:", c1)
print("El valor de c2 es:", c2)
print("El valor de c3 es:", c3)
print("El valor de c4 es:", c4)
print("El valor de c5 es:", c5)