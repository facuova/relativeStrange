"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Argentina
"""

from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import clean_df_list
from data_cleaning.clean_df_list import clean_df
from data_cleaning.clean_float_list import convert_float_list
from data_cleaning.clean_date_list import convert_date_list

#Importamos los archivos  y lo agregamos a una lista
USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
BMA_FILE_PATH = './data/quotes/bma.xlsx'
BBAR_FILE_PATH = './data/quotes/bbar.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, BMA_FILE_PATH, BBAR_FILE_PATH]

#Hacemos una sublista para mantener el original
XLSX_SUBLIST = XLSX_LIST

#Aplicamos una función para transformar la lista con arcvhivos xlsx en una lista con dataframes
df_list = transform_xlsx(XLSX_SUBLIST)

#Aplico la funciones de data_cleaning
clean_df(df_list[0])
clean_df_list(df_list[1:])
convert_float_list(df_list)
convert_date_list(df_list)
