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

        df['calculo_x'] = df['retorno_x']
        df['calculo_y'] = df['retorno_y']

        df.fillna({'calculo_x':100}, inplace=True)
        df.fillna({'calculo_y':100}, inplace=True)

        df['base_100_x'] = df['calculo_x'].cumsum()
        df['base_100_y'] = df['calculo_y'].cumsum()
    
    return lista_df
    
  