"""
"""
def base_hundred (lista_df):
    """    
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes  
    """
    for i, df in enumerate(lista_df):
        if i == 0:
            df['Var base 100'] = 100.00
        else:
            df['Var base 100'] = df['retorno'] + 100
 
    return lista_df
