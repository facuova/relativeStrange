"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Argentina
"""

from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import clean_df_list
from data_cleaning.clean_float_list import convert_float_list
from data_cleaning.clean_date_list import convert_date_list

#Importamos los archivos  y lo agregamos a una lista

USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
BBAR_FILE_PATH = './data/quotes/bbar.xlsx'
BMA_FILE_PATH = './data/quotes/bma.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, BMA_FILE_PATH, BBAR_FILE_PATH]

#Hacemos una sublista para mantener el original
XLSX_SUBLIST = XLSX_LIST

#Aplicamos una función para transformar la lista con arcvhivos xlsx en una lista con dataframes
df_list = transform_xlsx(XLSX_SUBLIST)

#Armamos un subset del usd, para mantener el original y modificar el subset
df_usdb = df_list[0]

#Cambiamos los nombres de la columa del DF_USDB que se descargó
# de una fuente de datos distinta a la de las acciones.
df_usdb.rename(columns={
    'Fecha': 'fecha', 
    'Venta': 'cierre'
    },
    inplace=True
    )
#Elimino la columna que no voy a utilizar
df_usdb.drop("Compra", axis=1, inplace=True)

#Como tengo DF_USDB por separado. Lo suelto de la lista de df
df_list.pop(0)

#Aplico la funcion de filtrado y renombre de columnas

clean_df_list(df_list)
convert_float_list(df_list)
convert_date_list(df_list)

print(df_list[0])
