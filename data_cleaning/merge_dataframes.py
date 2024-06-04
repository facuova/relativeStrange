"""
    Esta función crea un DataFrame recorriendo una lista de DataFrames 
    uniendólos en base a una columna común.
"""

def merge_df_list(list_df, on, how='left'):
    """
    Esta función recorre una lista de Dataframes 

    Parámetros:
        list_df (list): Lista de DataFrames que se unirán.
        on (str): Nombre de la columna en la que se basará la unión. 
        how (str): Tipo de unión a realizar. Por defecto, 'left'.

    Returns:
        list_merge (list):  Lista con DataFrames unidos con el primer df de la lista inicial
    """
    if not list_df:
        return []

    # El primer DataFrame de la lista
    df0 = list_df[0]

    # Lista para almacenar los DataFrames combinados
    merged_dfs = []

    # Iterar sobre los DataFrames a partir del segundo
    for df in list_df[1:]:
        merged_df = df.merge(df0, on=on, how=how)
        merged_dfs.append(merged_df)
        
    return merged_dfs

def merge_dataframes(list_df, on_column='fecha', suffixes=None, how='left'):
    """
    Esta función recorre una lista de Dataframes y crea un DataFrame en base 
    a la columa en común 'fecha'

    Parámetros:
        list_df (list): Lista de DataFrames que se unirán.
        on_column (str): Nombre de la columna en la que se basará la unión. Por defecto, 'fecha'.
        suffixes (list): Sufijos para las columnas de cada DataFrame en caso de conflicto. Por defecto, None.
        how (str): Tipo de unión a realizar. Por defecto, 'left'.

    Returns:
        DataFrame: DataFrame resultante de la unión.
    """
    # Si no se especifican sufijos, se utilizan valores predeterminados
    if suffixes is None:
        suffixes = [''] * len(list_df)

    # Realizar la unión de los DataFrames
    merged_df = list_df[0]
    for i, df in enumerate(list_df[1:], start=2):
        merged_df = merged_df.merge(df, on=on_column, suffixes=(f'_{i-1}', f'_{i}'), how=how)
    
    return merged_df
