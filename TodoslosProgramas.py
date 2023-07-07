print("Programa que tenga todos los programas\n")
def Intercambiar_variables():
    A = 7
    B = 0
    C = 0
    B = A
    C = B
    A = A
    return(A,B,C)
print("Programa 1.\nIntercambiar variables:")
(A,B,C) = Intercambiar_variables()
print(A,B,C)

def Transformar_Valores():
    A = 10
    B = 20
    AUX = 10
    return (A, B, AUX)
print("\nPrograma 2.\nTransformar Valores:")
(A, B, AUX) = Transformar_Valores()
print(A,B,AUX)
def Imprimir_Datos():
    D = A + B + C / 3
    return (D)
print("\nPrograma 3.\nImprimir datos:")
A = float(input("Leer A: "))
B = float(input("Leer B: "))
C = float(input("Leer C: "))
D = Imprimir_Datos()
print ("Imprimir: ", D)

def Programa_calcular_area_t():
    area = B * A / 2
    return (area)
print ("\nPrograma 4.\nQue calcula el area de un triangulo: ")
Base = input("Escriba la Base: ")
Altura = input("Escriba la Altura: ")
Hipotenusa = input("Escriba la Hipotenusa: ")
B = float(Base)
A = float(Altura)
area = Programa_calcular_area_t()
print("Imprimir: ", area)

def calcular_per_rectangulo():
    P = AB+ BC + CD + DA
    return (P)
print("\nPrograma 5.\nQue calcule el perimetro de un rectangulo:")
AB = float(input("Escriba el valor de AB: "))
BC = float(input("Escriba el valor de BC: "))
CD = float(input("Escriba el valor de CD: "))
DA = float(input("Escriba el valor de DA: "))    
P = calcular_per_rectangulo()
print("El area de un rectangulo es: ", P)

def calcular_a_trapesio():
    A = B1 + B2 * Alt / 2
    return (A)
print("\nPrograma 6.\nQue calcula el area de un trapesio:")
B1 = float(input("Escriba el valor de base 1: "))
B2 = float(input("Escriba el valor de base 2: "))
Alt = float(input("Escriba el valor de la Altura: "))
A = calcular_a_trapesio()
print("El area de un trapesio es de: ", A)

def volumen_prisma_r():
    V= L * An * Alt
    return (V)
print ("\nPrograma 7.\nQue calcule el volumen de un prisma rectangular:")
L = float(input("Escriba el valor de el largo: "))
An = float(input("Escriba el valor de el ancho: "))
Alt = float(input("Escriba el valor de la altura: "))
V= volumen_prisma_r()
print("El volumen de un prisma rectangular es: ", V)

def resolver_ecuaciones():
    A = 20-(7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 -(8 * x ) + 2
    E = ((5 * x) + 78 ) /28
    F = (((6 * x) -7)/4) + (((3 * 7) -5)/7)
    return (A, B, C, D, E, F)

print("\nPrograma 8.\nPrograma que resuelve ecuaciones:")
x = float(input("Escriba el valor de x: "))
(A, B, C, D, E, F) = resolver_ecuaciones()
print("El resultado de A es:", A)
print("El resultado de B es:", B)
print("El resultado de C es:", C)
print("El resultado de D es:", D)
print("El resultado de E es:", E)
print("El resultado de F es:", F)

def ecuaciones_abc_1():
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
(c1, c2, c3, c4, c5) = ecuaciones_abc_1()
print("El valor de c1 es:", c1)
print("El valor de c2 es:", c2)
print("El valor de c3 es:", c3)
print("El valor de c4 es:", c4)
print("El valor de c5 es:", c5)

def conversiones_unidades():
    P = M * 3.28
    PLG = M *  39.37
    return (P, PLG)
print ("\nPrograma 10.\nResuelve conversiones de unidades:")
M= float(input("Ingrese la cantidad de metros: "))
(P, PLG) = conversiones_unidades()
print("La conversion de metros a pies es de:", P)
print("La conversion de metros a pulgadas es de:", PLG)

def regla_tres():
    D = c3 * b2 / a1
    return (D)
print ("\nPrograma 11\nQue resuelve una regla de tres:")
a1= float(input("Ingrese el primer valor: "))
b2 = float(input("Ingrese el segundo valor: "))
c3 = float(input("Ingrese el tercer valor: "))
D = regla_tres()
print ("El valor de la regla es:", D)

def calcular_interes_prestamo(m, tm, pl):
    td = tm / 100
    c = m * (td * (1 + td) ** pl) / ((1 + td) ** pl - 1)
    i = m * td
    cap = c - i
    return (c, i, cap)
print("\nPrograma 12.\nCalcula el interés de un préstamo:")
m = float(input("Ingrese el monto del préstamo: "))
tm = float(input("Ingrese la tasa de interés mensual (%): "))
pl = int(input("Ingrese el plazo del préstamo en meses: "))
(c, i, cap) = calcular_interes_prestamo(m, tm, pl)
print("La cuota mensual a pagar es:", round(c,2))
print("Del monto total:")
print("Monto para intereses:", round(i,2))
print("Monto para capital:", round(cap,2))

def calcular_salario_trb():
   SS = S * 0.0514
   SE = S * 0.02
   P = 50
   SN = S - SS - SE - P
   return (SN, SS, SE, P)
print("\nPrograma 13.\nQue calcule salario neto de los trabajadores:")
S = float(input("Ingresa su Salario Mensual: "))
SN, SS, SE, P = calcular_salario_trb()
print("Su saldo a pagar de seguro social es de:", SS)
print("Su saldo a pagar de seguro educativo es de:", SE)
print("Su saldo a pagar de prestamo es de: ", P)
print("El salario a pagar es de:", round(SN, 2))

def costo_compra_combustible(Litro):
    a = Litro * 0.98 * 1.07
    return a
print("\nPrograma 14.\nQue calcule el costo de compra de gasolina:")
Litro = float(input("Valor de cantidad de litros: "))
ct = costo_compra_combustible(Litro)
print(ct)

def compra_impuestos():
    PA = A1 + A2 + A3
    I = PA * 1.07
    return (I)
print("\nPrograma.15\nQue calcule el total de la compra con impuesto:")
A1 = float(input("Escribir valor del articulo 1: "))
A2 = float(input("Escribir valor del articulo 2: "))
A3 = float(input("Escribir valor del articulo 3: "))
(I) = compra_impuestos()
print("total de la compra con el impuesto es de: ", round(I, 2))

def cal_nota_final():
    PE1 = N1 * 0.20
    PE2 = N2 * 0.15
    PE3 = N3 * 0.25
    PE4 = N4 * 0.10
    PE5 = N5 * 0.30
    NT = PE1 + PE2 + PE3 + PE4 + PE5 / 100
    return (NT)
print("\nPrograma 16.\nQue calcule la nota final:")
N1 = float(input("Ingresa la primera evaluación: "))
N2 = float(input("Ingresa la segunda evaluación: "))
N3 = float(input("Ingresa la tercera evaluación: "))
N4 = float(input("Ingresa la cuarta evaluación: "))
N5 = float(input("Ingresa la quinta evaluación: "))
(NT) = cal_nota_final()
print("La nota final es de :",round(NT, 2))

def convrt_cantidad_unid(g, kg, cm, m):
    g = kg * 1000
    kg = g * 0.001
    cm = m * 100
    m = cm * 0.01
    return (g, kg, cm, m)
print("\nPrograma 17.\nQue convierta cantidades de unidades:")
g= float(input("Ingrese el valor en gramos: "))
kg =float(input("Ingrese el valor en kilogramos: "))
m = float(input("Ingrese el valor en metros: "))
cm = float(input("Ingrese el valor en centímetros:"))
(g, kg, cm, m) = convrt_cantidad_unid(g, kg, cm, m)
print("El resultado es:", g)
print("El resultado es:", kg)
print("El resultado es:", cm)
print("El resultado es:", m)

def interes_compuesto():
    ti = i / 100
    Cf = Ci * (1 + ti) ** n
    return (Cf)
print("\nPrograma 18.\nQue calcule el interés compuesto:")
Ci = float(input("Ingrese el capital inicial: "))
i = float(input("Ingrese la tasa de interés (%): "))
n = float(input("Ingrese el período del ahorro: "))
(Cf) = interes_compuesto()
print("El capital final es: ", Cf)

def compra_articulos():
    CSI = A1 + A2 + A3 + A4 + A5
    CNI = CSI * 1.07
    TDC = CNI
    return (CSI, CNI)
print("\nPrograma 19.\nQue calcule la compra de 5 artículos")
A1 = float(input("Escriba el valor del primer articulo: "))
A2 = float(input("Escriba el valor del segundo articulo: "))
A3 = float(input("Escriba el valor del tercer articulo: "))
A4 = float(input("Escriba el valor del cuarto articulo: "))
A5 = float(input("Escriba el valor del quinto articulo: "))
(CSI, CNI) = compra_articulos()
print("El total de la compra sin impuesto es: ", round(CSI, 2))
print("El total de la compra con impuesto es: ", round(CNI, 2))

def cal_salario_neto():
    ss = sb * 0.08
    se = sb * 0.02
    i = sb * 0.15
    p = 100
    sn = sb - ss - se - i - p
    return (sn)
print("\nPrograma 20.\nQue calcule el salario neto de un empleado:")
sb = float(input("Ingrese el salario bruto del empleado: "))
(sn) = cal_salario_neto()
print("El salario neto a pagar es:", sn)

def cal_impuestos():
    if s <= 3000:
        i = s * 1.07
        print("Esta persona debe abonar impuestos:", i)
    else:
        print("No debe abonar impuestos")
        return (s)
print("\nPrograma 21.\nCalcular si una persona paga impuestos.")
s = float(input("Escriba el salario: "))
(s) = cal_impuestos()

def Cal_temperatura():
    if t < 20:
        if t < 10:
            print("Nivel azul")
        else:
            print("Nivel verde")
    else:
        if t < 30:
            print("Nivel naranja")
        else:
            print("Nivel rojo")
    return (t)
print("\nPrograma 22.\nQue Calcule la temperatura :")
t = float(input("Escriba la temperatura: "))
(t) = Cal_temperatura()

def cal_edad():
    if e >= 18:
        print('Eres adulto')
    elif e < 17:
        print('Eres menor de edad')
        return(e)
print("\nPrograma 23.\nPara calcular si es mayor o menor de edad:")
e = float(input("Escribir la edad: "))
(e) = cal_edad()

def Mayor_de_tres(n1, n2, n3):
    mayor = n1
    if n2 > mayor:
        mayor = n2
    if n3 > mayor:
        mayor = n3
    return mayor
print("\nPrograma 24\nPara calcular el mayor de 3 numeros:")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
mayor = Mayor_de_tres(n1, n2, n3)
print("El mayor número es:",mayor)

def cal_descuento():
    Des= PD / 100
    PP = P * Des
    PF = P - PP
    if  PF < 50:
        print("¡Oferta especial!")
        return(PF)
print("\nPrograma 25.\nPara calcular descuentos:")
P = float(input("Ingrese precio original del producto: "))
PD = float(input("Ingrese el porcentaje de descuento: "))
(PF) = cal_descuento()
print("El precio final del producto es:", PF)

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

def Num_p_n_cero():
    if V == 0:
        print('Es cero')
    elif V < 0:
        print('Es negativo')
    else:
        print('Es positivo')
        return(V)
print("\nPrograma 27.\nQue calcule si el numero es positivo o negativo o 0:")
V= float(input("Escribe el número: "))
(V) = Num_p_n_cero()
def calf_evalue():
    if clf >= 90:
        print("tu calificacion es A")
    elif clf  >= 80 and clf  <90:
        print("tu calificacion es B")
    if clf  >= 70 and clf  < 80:
        print("tu calificacion es C")
    elif clf  >= 60 and clf < 70:
        print("tu calificacion es D")
    if clf  < 60:
        print("tu calificacion es F")
        return(clf)
print("\nProgram 28.\nQue califique y evalue segun su puntuacion:")
clf = float(input("Ingrese la calificacion: "))
(clf) = calf_evalue()

def num_brk():
    for i in range(10):
        if i == 7:
            break
        print(i)
print("\nPrograma 29.\nfor del 1 al 10 que rompe en 7:")
(i) = num_brk()

def Num_impares():
    num = 1
    while num <= 50:
        print(num)
        num += 2
print("\nPrograma 30.\nImpresión de números impares:")
(num) = Num_impares()

def Impr_num_impares():
    value = 1
    while 0 <= 10:
        if value == 8:
            break
        print(value)
        value += 1
print("\nPrograma 31.\nImprimir Impares Hasta 7")
(value) = Impr_num_impares()

def Mostar_Num():
    valor = 1
    while valor < 11:
        if valor == 11:
            break
        print(valor)
        valor += 1
print("\nPrograma 32\nQue trata de mostrar 10 numeros:")
(value) = Mostar_Num()

def Tabla_de_Multiplicar():
    for i in range (1, 13):
        print("\nTabla de Multiplicar del :")
        print("=========================")
        for j in range (1, 13):
            r = i * j
            print(i, "x", j, "=" , r)
            print()
print("\nPrograma 33.\nTabla de multiplicar:")
(r) = Tabla_de_Multiplicar()

def num_par_impar():
    a = 1
    while a <= 16:
        if a % 2 == 1:
            print(a, "es impar")
        else:
            print(a, "es par")
        a += 1     
print("\nPrograma 34.\nImprimir Numeros par y impares:")
num_par_impar()

def Lista_nums():
    for Nums in range(1, 11):
        if Nums > 5:
            print(Nums, "es mayor a 5")
        elif Nums <= 0:
            print(Nums, "es menor a 5")
        else:
            print(Nums, "es menor o igual a 0")
        if Nums == 9:
            break
print("\nPrograma 35.\nLista de numeros del 1 al 10:")
Lista_nums()

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

def cal_mayor_de3():
    numeros = []
    contador = 0
    while contador < 3:
        numero = float(input("Escribir número: "))
        numeros.append(numero)
        contador += 1
    mayor = numeros[0]
    i = 1
    while i < 3:
        if numeros[i] > mayor:
            mayor = numeros[i]
        i += 1
    print("El número mayor es:", mayor)
print("\nPrograma 37.\nCalcule el mayor de 3 numeros:")
cal_mayor_de3()

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

def calcular_area_triangulo(base,altura):
    area = (base*altura) / 2
    return area
print("\nPrograma 39.\nCalcula el area de un triangulo:")
base = float(input("escriba la base: "))
altura = float(input("escribe la altura: "))
area = calcular_area_triangulo(base, altura)
print("el area del triangulo es" , area)
print("Fin del Programa")

def costo_compra_combustible(Litro):
    a = Litro * 0.98 * 1.07
    return a
print("\nPrograma 40.\nAgarrar Cualquier Programa y convertir a funcion:")
Litro = float(input("Valor de cantidad de litros: "))
ct = costo_compra_combustible(Litro)
print(ct)

print("\n\U0001f600 Fin Del Programa \U0001f600")