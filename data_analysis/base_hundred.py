"""
    Esta función crea el 1° cálculo para calcular la fuerza relativa
"""
def base_hundred (lista_df):
    """    
        Esta función recorre una lista de DataFrames y en cada uno de ellos
        crea la columna 'var base 100' 
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de DataFrames con columna 'var base 100'
    """
    for df in (lista_df):

        df['calculo'] = df['retorno']

        df.fillna({'calculo':100}, inplace=True)
        
        df['var base 100'] = df['calculo'].cumsum()

    return lista_df
    
  