"""
    Esta función es la que cálcula la fuerza relativa entre los distintos activos
"""

def relative_strange(lista_df):
    """
        Esta función recorre una lista de DatFrames y crea la columan "X/USD/ 
        donde se genera el cálculo de fuerza relativa
        Parámetros:
            lista_df(list) : Lista de dataframes
        Returns:
            lista_df(List) : Lista de dataframes con columna nueva de 'RS X/USD'
    """
    for df in lista_df:
       
        df['X/USD'] = round(df['base_100_x'] / df['base_100_y'] * 100, 3)
        
    return lista_df