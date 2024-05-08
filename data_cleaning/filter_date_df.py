"""
    Esta función filtra datos soolo en el 1° DataFrame de la lista
    daado que tiene más fechas que la que necesitamos para el análisis
"""

def filter_date_df(lista_df):
    """
        Esta fimción filtra datos de fechas. Eliminando los que no se comparte 
        con los otros DataFrames.
        Parámetros:
            lista_df(list) : Lista de DataFrames
        Returns:
            lista_df(List) : Lista de DataFrames con columna 'fecha' filtrada
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
