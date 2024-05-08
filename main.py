"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Argentina
"""
import pandas as pd
from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import clean_df_list
from data_cleaning.clean_df_list import clean_df
from data_cleaning.clean_float_list import convert_float_list
from data_cleaning.clean_date_list import convert_date_list
from data_cleaning.merge_dataframes import merge_dataframes
from data_cleaning.filter_date_df import filter_date_df
from data_analysis.quotes_return import quotes_return
from data_analysis.base_hundred import base_hundred
from data_analysis.relative_strange import relative_strange

#Imporo los archivos y los agrego a una lista
USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
BMA_FILE_PATH = './data/quotes/bma.xlsx'
BBAR_FILE_PATH = './data/quotes/bbar.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, BMA_FILE_PATH, BBAR_FILE_PATH]

#Creo una sublista para mantener el original
XLSX_SUBLIST = XLSX_LIST

#Ejecuto la función para transformar la lista con archivos XLSX en una lista con DF
df_list = transform_xlsx(XLSX_SUBLIST)

#Ejecuto las funciones de data_cleaning
clean_df(df_list[0])
clean_df_list(df_list[1:])
convert_float_list(df_list)
convert_date_list(df_list)
filter_date_df(df_list)

#Ejecuto las funciones de data_analysis
quotes_return(df_list)
base_hundred(df_list)
relative_strange(df_list)

#Ejecuto la función para unir todo en un mismo dataframe
merged_df = merge_dataframes(df_list,on_column='fecha', suffixes=[None], how='left')

#Elimino los datos Nan y corrigo los indices
merged_df = merged_df.dropna().reset_index(drop=True)

rs_df = merged_df[['fecha','RS X/USD_1','RS X/USD_2', 'RS X/USD_3', 'RS X/USD_4']]


#Salida de resultados en un archivo Excel
with pd.ExcelWriter('C:/Users/Facu/Desktop/Prueba rs.xlsx') as writer: 
    rs_df.to_excel(writer, sheet_name='rs_df')
    df_list[0].to_excel(writer, sheet_name='USD')
#Creo subset del merge y renombro las columnas que se modificaron despúes del merge
#df_qoutes = merged_df.rename(columns={
#    'cierre_1':'usdb',
#    'cierre_2':'alua',
#    'cierre_3':'bma',
#    'cierre_4':'bbar',
#    })

#relative_strange = merged_df[[
#    'fecha',
#    'Var base 100_1',
#    'Var base 100_2',
#    'Var base 100_3',
#    'Var base 100_4']]

#print(relative_strange)
