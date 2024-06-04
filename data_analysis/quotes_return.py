"""
   Esta función calcula los retornos/rendimiento diario de cada activo
"""
import numpy as np

def quotes_return (lista_df):
    """
        Esta función recorre una lista y calculará los retornos de los precios de cierre
        en cada  uno de los DataFrames
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes con columna nueva de 'retorno'
    """
    for df in lista_df:
        df['retorno_x'] = round(((np.log(df['cierre_x'] / df['cierre_x'].shift(1)))*100),3)
        df['retorno_y'] = round(((np.log(df['cierre_y'] / df['cierre_y'].shift(1)))*100),3)
        df = df.drop(0)
    
    return lista_df
