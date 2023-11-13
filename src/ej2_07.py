"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""


nombre = input("Ingrese su nombre: ")
nombre_minusculas = nombre.lower()

print("Nombre en minúsculas:", nombre_minusculas)

nombre1 = "Juan"
nombre2 = input("Ingrese otro nombre: ")

if nombre1.lower() == nombre2.lower():
    print("Los nombres son iguales (ignorando mayúsculas/minúsculas).")
else:
    print("Los nombres son diferentes.")