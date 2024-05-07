"""
"""
def base_hundred (lista_df):
    """    
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes  
    """
    for df in lista_df:
        df['Var base 100'] = df['retorno'] + 100
 
    return lista_df
