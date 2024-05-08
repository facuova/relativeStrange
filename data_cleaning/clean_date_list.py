"""
    Esta función trasnforma los datos de la columa 'fecha' de una lista de DataFrames
"""

import pandas as pd

def convert_date_list(lista_df):
    """
    Esta funcion recorre una lista de DataFrames y en cada uno de ellos convierte el tipo 
    de datos en la columna 'fecha' transformándolos a tipo DateTime64 
    Argumentos: 
        Lista_df (lista): lista con dataframes
    Returns:
        lista_df (lista): lista con DataFrames con la columna 'fecha' en formato DateTime64
    """
    for df in lista_df:
        #Convertimos el formato de fechaHora a datetine
        df['fecha'] = pd.to_datetime(df['fecha'])
        
    return lista_df