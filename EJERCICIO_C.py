"""
c.Extraer los nombres de archivos de un tipo de formato en una ruta de
directorio, por ejemplo: C:\Documentos, archivos txt.
"""
import re
import os

def c():
    print('--- Ejecutando Inciso C: Extracción de archivos .txt ---')
    
    ruta = input("Introducir la ruta de la carpeta (ejemplo C:\\Users\\Desktop): ")

    try:
        archivos_en_carpeta = os.listdir(ruta)
        
        patron = r'^.*\.txt$'
        lista_txt = []
    
        for nombre in archivos_en_carpeta:
            if re.match(patron, nombre, re.IGNORECASE):
                lista_txt.append(nombre)
       
        if lista_txt:
            print("\nArchivos encontrados (Arreglo):")
            print(lista_txt) 
        else:
            print("\nNo se encontró ninguna ocurrencia de archivos .txt.")

    except FileNotFoundError:
        print("Error: La ruta no existe. Verifica que esté bien escrita.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


c()
