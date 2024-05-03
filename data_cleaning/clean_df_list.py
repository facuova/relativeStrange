"""
Este módulo proporciona la función para filtrar y renombrar columnas de una lista
"""

def clean_df_list(lista_df):
    """
    Renombramos las columnas de la lista de dataframes y eliminamos la que no precisamos 
    Argumentos: 
        lista_df (list) : Lista con dataframes
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