""""
e.Validar si una contraseña es segura. Una contraseña segura debe
tener al menos 8 caracteres, una letra mayúscula, una letra
minúscula, un número y un carácter especial.
"""

import re

def e():
        while(True): 
            try: 
                # Entrada
                texto= input("Ingrese la contraseña o contraseñas a analizar: ")

                #Proceso:

                #Expresión Regular para validar una contraseña segura
                expresion = r"(?=\S{8,})(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[!@#$%^&*(),.?\":{}|<>])\S+"
            

                coincidencias= re.findall(expresion,texto)

                # Salidas
                if coincidencias:
                    print("Contraseña Seguras: ")
                    print(coincidencias)
                    try:
                        with open("Salidas_E.txt", "w",encoding="utf-8") as archivo:
                            archivo.write(str(coincidencias)+ "\n")
                    except Exception as e_file:
                        print(f"Error al escribir el archivo: {e_file}")        

                else:
                    print("No se encontraron coincidencias")
                    try:        
                        with open("Salidas_E.txt", "w",encoding="utf-8") as archivo:
                            archivo.write(str("No se encontraron coincidencias\n"))
                    except Exception as e_file:
                        print(f"Error al escribir el archivo: {e_file}")
            


            except KeyboardInterrupt:
                print("\nInterrupción del usuario. Saliendo del programa...")
                break  # Sale del while y termina la función
            except Exception as e_input:
                print(f"Ocurrió un error inesperado: {e_input}")

