"""
    Creado por Facu
"""

def renamecol_ouput(lista_df,strin,strout):
    """
        Esta función recorre una lista de dataframes y en cada uno de ellos, renombra las columnas
        por medio de una función split()
        sumar como parametro "src" para especificar el noonbre del grafico
    """
    for i, df in enumerate(lista_df):
        #Buscar la columna que empieza con "cierre_" y renombrarla a "cierre"
        for col in df.columns:
            if col.startswith(strin):
                df.rename(columns={col: strout}, inplace=True)
                break  # Solo renombramos la primera coincidencia
    
    return lista_df
