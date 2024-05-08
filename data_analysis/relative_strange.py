"""
    Acá esta la función
"""

def relative_strange(lista_df):
    """
        Acá está la función
    """
    for df in lista_df:
        df['RS X/USD'] = round(df['var base 100'] / lista_df[0]['var base 100'] * 100, 3)
    return lista_df