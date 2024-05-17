"""
Proyecto para calcular fuerza relativa entre acciones y dólar en Argentina
"""
import pandas as pd
import matplotlib.pyplot as plt
from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import (clean_df_list, clean_df)
from data_cleaning.clean_float_list import convert_float_list
from data_cleaning.clean_date_list import convert_date_list
from data_cleaning.merge_dataframes import merge_dataframes
from data_cleaning.filter_date_df import filter_date_df
from data_analysis.quotes_return import quotes_return
from data_analysis.base_hundred import base_hundred
from data_analysis.relative_strange import relative_strange
#from data_output.plot import grafico_output

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

#Creo subset final del merge y renombro las columnas que se modificaron despúes del merg
rs_df = merged_df[['fecha','RS X/USD_1','RS X/USD_2', 'RS X/USD_3', 'RS X/USD_4']]

rs_df = rs_df.rename(columns={
    'RS X/USD_1':'USDB',
    'RS X/USD_2':'ALUA/USDB',
    'RS X/USD_3':'BMA/USDB',
    'RS X/USD_4':'BBAR/USDB',
    })

usd_df = merged_df[['fecha','cierre_1','retorno_1']]
alua_df = merged_df[['fecha','cierre_2','retorno_2']]
bma_df = merged_df[['fecha','cierre_3','retorno_3']]
bbar_df = merged_df[['fecha','cierre_3','retorno_3']]

#Salida de resultados en un archivo Excel
with pd.ExcelWriter('./data/final/rs_analysis.xlsx') as writer: 
    rs_df.to_excel(writer, sheet_name='rs_df', index=False)
    usd_df.to_excel(writer, sheet_name='USD', index=False)
    alua_df.to_excel(writer, sheet_name='ALUA', index=False)
    bma_df.to_excel(writer, sheet_name='BMA', index=False)
    bbar_df.to_excel(writer, sheet_name='BBAR', index=False)

#grafico_output(rs_df)
    
plt.figure(figsize=(10, 5))
plt.title('Gráfico de Precios')
plt.xlabel('Fecha')
plt.ylabel('USDB')
plt.plot(rs_df['fecha'],rs_df[['USDB','ALUA/USDB','BMA/USDB','BBAR/USDB']], linestyle='-')
plt.grid(True)

# Ajustar diseño del gráfico
plt.tight_layout()
# Guardar el gráfico en un archivo de imagen
plt.savefig('./data/final/grafico_usd.png', dpi=300)
