import os
os.system("cls")
print()
edad=int(input("Ingrese su edad >"))
if edad >= 16:
    ingr=int(input("Ingrese sus ingresos mensuales >"))
    print()
    if ingr >= 1000:
        print("El usuario ingresado debe Tributar")
    else:
        print("El usuario ingresado no debe Tributar")
else:
    print()
    print("El usuario no debe Tributar ya que es menor de 16 años")
print()