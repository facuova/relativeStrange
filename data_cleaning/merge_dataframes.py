"""
    Esta módulo incluirá 2 funciones. La primera la que servira para contar con todas
    las cotizaciones juntas para hacer el analisis con el dolar como base.
    Y la otra función que unirá cada dataframe con la cotizacion del USD
"""
def merge_dataframes(list_df, on_column='fecha', suffixes=None, how='left'):
    """
    Une una lista de DataFrames en base a una columna común.

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
