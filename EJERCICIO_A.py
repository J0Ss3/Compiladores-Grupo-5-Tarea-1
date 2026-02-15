import re
from datetime import datetime


""""
a.Validar un formato de fecha corto y uno largo, por 
ejemplo corto: YY-MM-DD; largo: “dia, DD" de "MM" de "YYYY”.
"""
import re
from datetime import datetime

def validar_fecha_corta(fecha):
    """Valida formato corto: YY-MM-DD"""
    try:
        yy, mm, dd = fecha.split('-')
        año = int(yy) + 2000
        mes = int(mm)
        dia = int(dd)
        fecha_obj = datetime(año, mes, dia)
        meses_nombres = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        return True, f'{dia} de {meses_nombres[mes-1]} de {año}'
    except (ValueError, IndexError):
        return False, 'Fecha inválida'

def validar_fecha_larga(fecha):
    """Valida formato largo: "dia, DD de MM de YYYY" """
    dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
             'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    
    patron = r'^(lunes|martes|miércoles|jueves|viernes|sábado|domingo),\s+(\d{1,2})\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+de\s+(\d{4})$'
    match = re.match(patron, fecha.lower())
    
    if not match:
        return False, 'Formato incorrecto'
    
    try:
        dia_nombre = match.group(1)
        dia = int(match.group(2))
        mes_nombre = match.group(3)
        año = int(match.group(4))
        mes_num = meses.index(mes_nombre) + 1
        fecha_obj = datetime(año, mes_num, dia)
        dias_python = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        dia_semana_correcto = dias_python[fecha_obj.weekday()]
        
        if dia_nombre != dia_semana_correcto:
            return False, f'Día de semana incorrecto (debería ser {dia_semana_correcto})'
        return True, 'Válida'
    except (ValueError, IndexError):
        return False, 'Error de validación'

def buscar_y_validar_fechas(texto):
    """Busca y valida todas las fechas en el texto"""
    formato_corto = r"\b\d{2}-\d{2}-\d{2}\b"
    formato_largo = r"\b(lunes|martes|miércoles|jueves|viernes|sábado|domingo),\s+\d{1,2}\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+de\s+\d{4}\b"
    
    resultados = {
        'cortas_validas': [],
        'cortas_invalidas': [],
        'largas_validas': [],
        'largas_invalidas': []
    }
    
    # Buscar fechas cortas
    for match in re.finditer(formato_corto, texto):
        fecha = match.group()
        es_valida, interpretacion = validar_fecha_corta(fecha)
        info = {'fecha': fecha, 'posicion': match.start(), 'interpretacion': interpretacion}
        
        if es_valida:
            resultados['cortas_validas'].append(info)
        else:
            resultados['cortas_invalidas'].append(info)
    
    # Buscar fechas largas
    for match in re.finditer(formato_largo, texto, re.IGNORECASE):
        fecha = match.group()
        es_valida, mensaje = validar_fecha_larga(fecha)
        info = {'fecha': fecha, 'posicion': match.start(), 'mensaje': mensaje}
        
        if es_valida:
            resultados['largas_validas'].append(info)
        else:
            resultados['largas_invalidas'].append(info)
    
    return resultados

def generar_archivo_salida(resultados, archivo_salida='Salida_A.txt'):
    """Genera el archivo de salida con los resultados"""
    total = sum(len(v) for v in resultados.values())
    
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        if total > 0:
            f.write(f'Total encontradas: {total}\n\n')
            
            f.write(f'FECHAS CORTAS VÁLIDAS: {len(resultados["cortas_validas"])}\n')
            for item in resultados['cortas_validas']:
                f.write(f'  {item["fecha"]} → {item["interpretacion"]}\n')
            f.write('\n')
            
            f.write(f'FECHAS CORTAS INVÁLIDAS: {len(resultados["cortas_invalidas"])}\n')
            for item in resultados['cortas_invalidas']:
                f.write(f'  {item["fecha"]} → {item["interpretacion"]}\n')
            f.write('\n')
            
            f.write(f'FECHAS LARGAS VÁLIDAS: {len(resultados["largas_validas"])}\n')
            for item in resultados['largas_validas']:
                f.write(f'  {item["fecha"]}\n')
            f.write('\n')
            
            f.write(f'FECHAS LARGAS INVÁLIDAS: {len(resultados["largas_invalidas"])}\n')
            for item in resultados['largas_invalidas']:
                f.write(f'  {item["fecha"]} → {item["mensaje"]}\n')
        else:
            f.write('No se encontraron fechas.')

def a():
    print('Procesando archivo...\n')
    
    try:
        # Lee el archivo de entrada
        with open("Texto_Prueba_A.txt", "r", encoding="utf-8") as archivo:
            texto_obtenido = archivo.read()
        
        # Buscar y validar fechas
        resultados = buscar_y_validar_fechas(texto_obtenido)
        
        # Generar archivo de salida
        generar_archivo_salida(resultados)
        
        # Mostrar resumen en consola
        total = sum(len(v) for v in resultados.values())
        
        if total > 0:
            print(f'Total de fechas encontradas: {total}')
            print(f'  Cortas válidas: {len(resultados["cortas_validas"])}')
            print(f'  Cortas inválidas: {len(resultados["cortas_invalidas"])}')
            print(f'  Largas válidas: {len(resultados["largas_validas"])}')
            print(f'  Largas inválidas: {len(resultados["largas_invalidas"])}')
        else:
            print('No se encontraron fechas.')
        
        print('\n✓ Archivo "Salida_A.txt" generado.')
        
    except FileNotFoundError:
        print('✗ Error: No se encontró "Texto_Prueba_A.txt"')
    except Exception as e:
        print(f'✗ Error: {e}')

