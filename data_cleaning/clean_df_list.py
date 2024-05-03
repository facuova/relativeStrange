"""
Este módulo proporciona la función para filtrar y renombrar columnas de una lista
"""

def clean_df_list(lista_df):
    """
    Renombramos las columnas de la lista de dataframes y eliminamos la que no precisamos 
    Argumentos: 
        lista_df (list) : Lista con dataframes
    Return:
        lista con dataframes
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
    Renombramos las columnas dataframes y eliminamos la que no precisamos 
    Argumentos: 
        (df) : Dataframe
    Return:
        Dataframe
    """


    df.rename(columns={
        'Fecha':'fecha',
        'Venta':'cierre',
        }, inplace=True  
    )

    df = df.drop(columns=column_delete, axis=1, inplace=True)

    return df