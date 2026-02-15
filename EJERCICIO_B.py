""""
b.Reemplazar palabras identificando otra palabra para cambiarla en
una oracion/parrafo. Por ejemplo cambiar “el” por “en”.
"""
import re




def generar_archivo_salida(resultados, archivo_salida='Salida_A.txt'):
    total = sum(len(v) for v in resultados.values())
    
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        if total > 0:
            f.write(f'Total encontradas: {total}\n\n')
            
            for cat, items in [('Cortas válidas', resultados['cortas_validas']),
                               ('Cortas inválidas', resultados['cortas_invalidas']),
                               ('Largas válidas', resultados['largas_validas']),
                               ('Largas inválidas', resultados['largas_invalidas'])]:
                f.write(f'{cat.upper()}: {len(items)}\n')
                for item in items:
                    f.write(f'  {item["fecha"]}\n')
                f.write('\n')
        else:
            f.write('No se encontraron fechas.')






def b():
    #Lee el archivo de entrada
    with open("Texto_Prueba_B.txt", "r", encoding="utf-8") as archivo:
        texto_obtenido = archivo.read()


    # Busca ocurrencias 
    ocurrencias = re.findall(r"\b(el|El)\b", texto_obtenido)

    #Crea archivo de salida
    with open("Salida_B.txt", "w", encoding="utf-8") as salida:

        if ocurrencias:
            cantidad_palabras = len(ocurrencias)
            
            print("Cantidad palabras encontradas:", cantidad_palabras)
            print("Ocurrencias encontradas:", ocurrencias)
            
            salida.write("Cantidad encontrada: " + str(cantidad_palabras) + "\n\n")
            salida.write("Ocurrencias encontradas:\n")
            for palabra in ocurrencias:
                salida.write(palabra + "\n")

            # Reemplaza la palabra
            resultado = re.sub(r"\b(el|El)\b", "en", texto_obtenido)

            print("\nTexto modificado:\n")
            print(resultado)

            salida.write("Texto modificado:\n")
            salida.write(resultado)

        else:
            print("No se encontraron coincidencias.")
            salida.write("No se encontraron coincidencias.")

        
    
