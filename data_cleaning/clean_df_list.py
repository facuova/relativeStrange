"""
    Este módulo proporciona la función para filtrar y renombrar columnas de una lista
    y de un DataFrame
"""

def clean_df_list(lista_df):
    """
        Esta función recorre una lista de DataFrames. Renombra las columnas y elimina las 
        que no precisamos 
        Argumentos: 
            ista_df (list) : Lista con dataframes
        Return:
            lista_df(list): lista con DataFrames con columnas renombradas y filtradas
    """
    for df in lista_df:
        df.rename(
            columns={
                'fechaHora': 'fecha',
                'ultimoPrecio': 'cierre',
            },
            inplace=True,
        )
        columns_delete = ['apertura','maximo','minimo','montoOperado','volumenNominal','cantidadOperaciones']
        df.drop(columns=columns_delete, inplace=True)

    return lista_df


column_delete = ['Compra']

def clean_df(df):
    """
    Renombramos las columnas de un DataFrames y elimina la columna que no preciso 
    Argumentos: 
        (df) : Dataframe
    Return:
        (df): Dataframe con columnas renombradas y filtrada
    """
    df.rename(columns={
        'Fecha':'fecha',
        'Venta':'cierre',
        }, inplace=True  
    )

    df = df.drop(columns=column_delete, axis=1, inplace=True)

    return df

def filer_df_list_merge(list_df):
    
    for df in list_df:
        columns_delete = [
            'cierre_x',
            'cierre_y',
            'retorno_x',
            'retorno_y',
            'calculo_x',
            'calculo_y',
            'base_100_x',
            'base_100_y']
        df.drop(columns=columns_delete, inplace=True)
    return list_df