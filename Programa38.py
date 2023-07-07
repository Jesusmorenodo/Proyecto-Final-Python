def sumar_Numeros_pares(N):
    sumap = 0
    for s in range (1, N+1):
        if s % 2 == 0:
            sumap += s
    return sumap
l = 20
suma = sumar_Numeros_pares(l)
print("\nPrograma 38.\nQue Calcule la suma de numeros pares:")
print("La suma de los numeros pares es:", suma)