"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    import pandas as pd
    import re
    
    ruta = "./files/input/clusters_report.txt"

    with open(ruta, "r", encoding="utf-8") as file: 
        text = file.read()

    # Expresión regular corregida para extraer correctamente los datos
    pattern = r"(\d+)\s+(\d+)\s+([\d,]+)\s%\s+(.+?)(?=\n\s*\d|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)

    # Procesar los datos extraídos
    data = []
    for match in matches:
        cluster = int(match[0])  # Número de cluster
        cantidad = int(match[1])  # Cantidad de palabras clave
        porcentaje = float(match[2].replace(",", "."))  # Convertir porcentaje a float
        palabras_clave = " ".join(match[3].split()).replace(" ,", ",")  # Limpiar espacios
        palabras_clave = palabras_clave.rstrip(".")  # Eliminar punto final si existe

        data.append([cluster, cantidad, porcentaje, palabras_clave])

    # Crear DataFrame sin establecer 'cluster' como índice
    df = pd.DataFrame(data, columns=["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])

    return df

# Ejecutar la función y mostrar el resultado
print(pregunta_01())