def  regla_tres ():
    D = c3 * b2 / a1
    return (D)
print ("\nPrograma 11\nQue resuelve una regla de tres:")
a1= float(input("Ingrese el primer valor: "))
b2 = float(input("Ingrese el segundo valor: "))
c3 = float(input("Ingrese el tercer valor: "))
D = regla_tres ()
print ("El valor de la regla es:", D)