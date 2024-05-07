"""
   Esta función recibe una lista con dataframes y calcula los retornos en cada df
"""
import numpy as np

def quotes_return (lista_df):
    """
        Esta función tomará una lista y calculará los retornos de los precios de cierre
        en cada df
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes con columna nueva de retornos 
    """
    for df in lista_df:
        df['retorno'] = round(((np.log(df['cierre'] / df['cierre'].shift(1)))*100),3)

    return lista_df
