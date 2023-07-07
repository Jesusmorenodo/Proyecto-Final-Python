def conversiones_unidades ():
    P = M * 3.28
    PLG = M *  39.37
    return (P, PLG)
print ("\nPrograma 10.\nQue resuelve conversiones de unidades:")
M= float(input("Ingrese la cantidad de metros: "))
(P, PLG) = conversiones_unidades ()
print("La conversion de metros a pies es de:", P)
print("La conversion de metros a pulgadas es de:", PLG)