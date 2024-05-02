"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Areentina
"""

from data_cleaning.transform_xlsx import transform_xlsx
#Importamos los archivos  y lo agregamos a una lista

USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
BBAR_FILE_PATH = './data/quotes/bbar.xlsx'
BMA_FILE_PATH = './data/quotes/bma.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, BMA_FILE_PATH, BBAR_FILE_PATH]

#Aplicamos una función para transformar la lista con arcvhivos xlsx en una lista con dataframes
DF_LIST = transform_xlsx(XLSX_LIST)

print(DF_LIST)