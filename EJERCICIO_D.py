""""
d.Validar un nombre de usuario que debe tener entre 8 y 12 caracteres 
y solo puede contener letras, números, guiones bajos o guiones alto.  
"""

import re

def d():
    lista_usuarios = "fadf, cAmpo82, hola-1234, astroNauta0, FuenTe_roja, Estudiante789, 12345, Mostaza_07, Barco_azul5, aleMeza"

    expresion = r"\b[a-zA-Z0-9_-]{8,12}\b"

    arreglo_usuarios = re.findall(expresion, lista_usuarios)

    if arreglo_usuarios:
        print("Nombres de usuario validos:")
        print(arreglo_usuarios)
    else:
        print("No se encontró ningun usuario valido.")
