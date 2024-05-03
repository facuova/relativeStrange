"""
    Esta función sirve para corregir el tipo de datos de los dataframe en una lista 
    de dataframes
"""

def convert_float_list (lista_df):
    """
    Cada columa cierre tiene datos str que serán trasnformados a float para hacer cálculos
    Argumentos: 
        Lista_df (lista): lista con dataframes
    Return:
        lista con dataframes
    """
    for df in lista_df:
        df['cierre'] = df['cierre'].astype(float)
    return lista_df