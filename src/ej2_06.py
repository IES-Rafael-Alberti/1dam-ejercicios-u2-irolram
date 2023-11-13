"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
def estar_en_grupo(nombre, sexo):

    
    if (sexo.upper() == "M" and nombre.lower() < "m") or (sexo == "H" and nombre.lower() > "n"):
        return "A"
    else:
        return "B"

def main():
    nombre = input("Escribe tu nombre: \n")
    sexo = input("Escribe M si eres mujer y H si eres hombre: \n")

    grupo = estar_en_grupo(nombre, sexo)

    if grupo == "A":
        print(f"{nombre} pertenece al grupo A")
    else:
        print(f"{nombre} pertenece al grupo B")

if __name__ == "__main__":
    main()