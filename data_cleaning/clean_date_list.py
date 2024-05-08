"""
Esta función trasnforma los datos de la columna de la columa fecha de una lista de df
"""

import pandas as pd

def convert_date_list(lista_df):
    """
    Cada columa fecha tiene datos que serán trasnformados a formato datetime64 para 
    Argumentos: 
        Lista_df (lista): lista con dataframes
    Returns:
        lista con dataframes
    """
    for df in lista_df:
        #Convertimos el formato de fechaHora a datetine
        df['fecha'] = pd.to_datetime(df['fecha'])       

        df.drop_duplicates(subset='fecha')
        
    return lista_df