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
print("\nPrograma 28.\nQue califique y evalue segun su puntuacion:")
clf = float(input("Ingrese la calificacion: "))
(clf) = calf_evalue()