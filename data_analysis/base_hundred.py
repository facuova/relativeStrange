"""
"""
def base_hundred (lista_df):
    """    
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes  
    """
    for df in (lista_df):
        df['calculo'] = df['retorno']
        df.fillna({'calculo':100}, inplace=True)
        df['var base 100'] = df['calculo'].cumsum()
    return lista_df
    
  