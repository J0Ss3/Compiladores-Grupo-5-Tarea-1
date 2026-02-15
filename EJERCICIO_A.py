import re
from datetime import datetime


""""
a.Validar un formato de fecha corto y uno largo, por 
ejemplo corto: YY-MM-DD; largo: “dia, DD" de "MM" de "YYYY”.
"""

def a():
    # Lee el archivo de entrada
    with open("Texto_Prueba_A.txt", "r", encoding="utf-8") as archivo:
        texto_obtenido = archivo.read()

        # Expresiones regulares para formatos de fecha
        formato_corto = r"\b\d{2}-\d{2}-\d{2}\b"
        formato_largo = r"\b(lunes|martes|miércoles|jueves|viernes|sábado|domingo),\s+\d{1,2}\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+de\s+\d{4}\b"


    # Buscar fechas en ambos formatos
    fechas_cortas = re.findall(formato_corto, texto_obtenido)
    fechas_largas = re.findall(formato_largo, texto_obtenido)

    # Validar y mostrar resultados
    print("Fechas en formato corto (YY-MM-DD):")
    for fecha in fechas_cortas:
        try:
            datetime.strptime(fecha, "%y-%m-%d")
            print(f"✓ {fecha} es una fecha válida.")
        except ValueError:
            print(f"✗ {fecha} no es una fecha válida.")

    print("\nFechas en formato largo (dia, DD de MM de YYYY):")
    for fecha in fechas_largas:
        try:
            datetime.strptime(fecha, "%d de %B de %Y")
            print(f"✓ {fecha} es una fecha válida.")
        except ValueError:
            print(f"✗ {fecha} no es una fecha válida.")