"""
Este módulo proporciona funciones para transformar archivos XLSX en DataFrames.
"""

import pandas as pd
import openpyxl

def transform_xlsx(lista_xlsx):
    """
    Transformamos archivos XLSX  a dataframes y los almacena en una lista
    Argumentos: 
        lista_xlsx (list) : Lista con archivos XLSX
    return:
        lista de dataframes
    """
    df_list = []
    for file in lista_xlsx:
        libro = openpyxl.load_workbook(file)
        hoja = libro.active
        titulos = next(hoja.values)[0:]
        df = pd.DataFrame(hoja.values, columns=titulos)
        df = df.drop(0)
        df_list.append(df)

    return df_list