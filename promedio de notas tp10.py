n1=int(input("Ingrese la primera nota >"))
n2=int(input("Ingrese la segunda nota >"))
n3=int(input("Ingrese la tercera nota >"))
prom=(n1+n2+n3)/3
prom=round(prom,2)
print()
if prom >= 7:
    print("Promocionado, el promedio fue:",prom)
elif prom >=4:
    print("Regular, el promedio fue:",prom)
else:
    print("Reprobado, el promedio fue:",prom)