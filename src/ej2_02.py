"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def verificar_contra(contra_guardada, contra_usuario):
    contra_usuario = contra_usuario.lower()
    contra_guardada = contra_guardada
    if contra_guardada == contra_usuario:
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")

contra_guardada = "contraseña"
contra_usuario = input("introduzca la contraseña: ")
verificar_contra(contra_guardada, contra_usuario)

