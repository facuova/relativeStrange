"""
    Esta función filtra datos
"""

def filter_date_df(lista_df):
    """
        Esta fimco+pm fopñtra datps
    """
    df1 = lista_df[0]
    otros_df = lista_df[1:]

    fechas_unicas = set()
    for df in otros_df:
        fechas_unicas.update(df['fecha'])
    
    mascara_fechas = df1['fecha'].isin(fechas_unicas)

    df_filtrado = df1[mascara_fechas]

    lista_df[0] = df_filtrado

    lista_df[0] = lista_df[0].drop_duplicates(subset='fecha')

    lista_df[0] = lista_df[0].reset_index(drop=True)

    

    return lista_df
