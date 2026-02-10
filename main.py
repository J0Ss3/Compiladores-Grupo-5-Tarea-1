""""
# Integrantes del Grupo

## Grupo #5
- Diego Fernando Rubio Godoy
- Idalia Ivón Zelaya Cruz
- José Francisco Vargas Carrasco
- Michael Hernan Archaga Nuñez
- Sara Nicolle Salinas Ramos
"""

import EJERCICIO_A,EJERCICIO_B,EJERCICIO_C,EJERCICIO_D,EJERCICIO_E


def mostrar_menu():
    
    print("Seleccione una opción:")
    print()
    print("  A. Validar formatos de fecha (corto y largo)")
    print("  B. Reemplazar palabras en texto")
    print("  C. Extraer archivos por extensión")
    print("  D. Validar nombre de usuario")
    print("  E. Validar si una contraseña es segura")
    print()
    print("  X. Salir del programa")
    print()

def main():
    """Función principal con el menú interactivo"""
    
    while True:
        mostrar_menu()
        
        opcion = input("Ingrese su opción: ").strip().upper()
        
        if opcion == 'A':
            EJERCICIO_A.a()
        elif opcion == 'B':
            EJERCICIO_B.b()
        elif opcion == 'C':
            EJERCICIO_C.c()
        elif opcion == 'D':
            EJERCICIO_D.d()
        elif opcion == 'E':
            EJERCICIO_E.e()

        elif opcion == 'X':
            print("  Saliendo\n")
            break
        else:
            print("\n✗ Opción no válida. Por favor seleccione A, B, C, D, E o X \n")


main()
