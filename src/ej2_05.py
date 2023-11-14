"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales 
o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

def tributar(edad, ingresosAlMes):

    return edad >= 16 and ingresosAlMes >= 1000

def main():
    edad = int(input("Escribe tú edad: \n"))
    ingresosAlMes = int(input("Escriba sus ingresos: \n"))

    if tributar(edad, ingresosAlMes):
        print("Usted puede tributar")
    else:
        print("Usted no puede tributar")

if __name__ == "__main__":
    main()





















"""
def mayorDedad():
    mayorEdad = int(input("Escribe tú edad: \n"))
    
    if mayorEdad < 16:
        print("Usted no puede tributar")
    else:
        print("Usted puede tributar")

def ingresos():
    dinero = int(input("Escriba sus ingresos: \n"))

    if dinero < 1000:
        print("Usted no puede tributar")
    else:
        print("Usted puede tributar")


def main():



"""