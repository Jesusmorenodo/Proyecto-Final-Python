def Intercambiar_variables():
    print("Programa 1 \nIntercambiar variables")
    A = 7
    B = 0
    C = 0
    B = A
    C = B
    A = A
    return(A,B,C)
A,B,C = Intercambiar_variables()
print(A,B,C)