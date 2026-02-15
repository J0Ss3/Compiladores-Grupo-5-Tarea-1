""""
d.Extraer los nombres de archivos de un tipo de formato en una ruta de
directorio, por ejemplo: C:\Documentos, archivos txt.
"""

import re

def d():
    lista_usuarios = "CaroRod12, cAmpo82, hola-1234, astroNauta0, FuenTe_roja, Estudiante789, 12345, Mostaza_07, Barco_azul5, aleMeza"

    expresion = r"\b[a-zA-Z0-9_-]{8,12}\b"

    arreglo_usuarios = re.findall(expresion, lista_usuarios)

    if arreglo_usuarios:
        print("Nombres de usuario validos:")
        print(arreglo_usuarios)
    else:
        print("No se encontró ningun usuario valido.")

d()
