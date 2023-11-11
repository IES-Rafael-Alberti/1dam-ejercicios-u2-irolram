"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
def parimpar():


#Creamos variable para pedir el numero
    numero = int(input("Dame un numero: "))
    #verificamos si es par o impar
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

parimpar()

def main():
    numero = int(input("Dame un numero: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

if __name__ == "__main__":
    main()