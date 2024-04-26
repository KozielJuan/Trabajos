import os
os.system("cls")
nombre = input("Ingrese su nombre >").lower()
genero = input("Ingrese su genero (F o M) >").lower()
print()
if genero == "m":
    if nombre >="n":
        print("Grupo A")
    elif nombre <"n":
        print("Grupo B")
    else:
        print("Error")
elif genero == "f":
    if nombre <= "m":
        print("Grupo A")
    elif nombre > "m":
        print("Grupo B")
    else:
        print("Error: Escribi bien tu nombre")
else:
    print("M o F")
print()
