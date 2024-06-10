"""
     Función de limpieza de dataframes que se encuentra en una lista 
"""

def clean_nan_dflist(list_df,subdata):
     """
          Está función recorre una lista  con dataframes y borra los datos nan
          de una una columna específica de los df     
     """
     list_df_clean = []
    
     for df in list_df:
       df = df.dropna(subset=subdata)
       list_df_clean.append(df)

     return list_df_clean

