"""
<<<<<<< HEAD
   Esta función calcula los retornos/rendimiento diario de cada activo
=======
   Esta función  calcula los retornos 
>>>>>>> data_analysis
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
        df['retorno'] = round(((np.log(df['cierre'] / df['cierre'].shift(1)))*100),3)

    return lista_df
