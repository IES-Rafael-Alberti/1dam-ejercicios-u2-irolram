"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""
def division():
    #Guardamos dividendo y divisor en dos variables distintas
    dividendo = float(input("introduce el dividendo: "))
    divisor = float(input("introduce el divisor: "))
    #Verificamos que se cumplen las condiciones
    if divisor == 0:
        print("Error")
    else: 
    #Le damos una variable a resultado para dividir
        resultado = dividendo / divisor
        print(f"El resultado de la division es: {resultado}")
#Llamamos a la funcion
division()