"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Argentina
"""

from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import clean_df_list

#Importamos los archivos  y lo agregamos a una lista

USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
BBAR_FILE_PATH = './data/quotes/bbar.xlsx'
BMA_FILE_PATH = './data/quotes/bma.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, BMA_FILE_PATH, BBAR_FILE_PATH]

#Hacemos una sublista para mantener el original
XLSX_SUBLIST = XLSX_LIST

#Aplicamos una función para transformar la lista con arcvhivos xlsx en una lista con dataframes
DF_LIST = transform_xlsx(XLSX_SUBLIST)
#Armamos un subset del usd, para mantener el original y modificar el subset
DF_USDB = DF_LIST[0]

#Cambiamos los nombres de la columa del DF_USDB que se descargó,
# de una fuente de datos distinta a la de las acciones.
DF_USDB.rename(columns={
    'Fecha': 'fecha', 
    'Venta': 'cierre'
    }, 
    inplace=True
    )

DF_USDB.drop("Compra", axis=1, inplace=True)


DF_LIST.pop(0)

clean_df_list(DF_LIST)

print(DF_USDB)
print(DF_LIST)