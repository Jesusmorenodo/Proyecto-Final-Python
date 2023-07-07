def resolver_ecuaciones():
    A = 20-(7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 -(8 * x ) + 2
    E = ((5 * x) + 78 ) /28
    F = (((6 * x) -7)/4) + (((3 * 7) -5)/7)
    return (A, B, C, D, E, F)
print("\nPrograma 8.\nPrograma que resuelve ecuaciones.")
x = float(input("Escriba el valor de x: "))
(A, B, C, D, E, F) = resolver_ecuaciones()
print("El resultado de A es:", A)
print("El resultado de B es:", B)
print("El resultado de C es:", C)
print("El resultado de D es:", D)
print("El resultado de E es:", E)
print("El resultado de F es:", F)