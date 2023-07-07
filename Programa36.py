def cont_de_impuestos():
    c = 0
    tl = 0
    
    while c < 5:
        p = float(input("Ingrese el precio del articulo: "))
        i = p * 0.07
        tl = i
        c += 1
        print("El total de impuestos a pagar es:", tl)
print("\nPrograma 36.\nContador que calcule impuestos: ")
(tl) = cont_de_impuestos()