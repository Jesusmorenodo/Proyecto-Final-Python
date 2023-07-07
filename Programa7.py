def volumen_prisma_r ():
    V= L * An * Alt
    return (V)
print ("\nPrograma 7\nQue calcule el volumen de un prisma rectangular:")
L = float(input("Escriba el valor de el largo: "))
An = float(input("Escriba el valor de el ancho: "))
Alt = float(input("Escriba el valor de la altura: "))
V= volumen_prisma_r()
print("El volumen de un prisma rectangular es: ", V)