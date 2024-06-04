"""
    Idea de análisis tomada de Pablo Paolucci. E-mail: rickdecardtw@gmail.com
    Proyecto para calcular la fuerza entre acciones y dólar blue en Argentina
    Fuente datos de acciones:  Invertir Online SA
    Fuentes datos de USD BLUE: Ambito.com
"""
import pandas as pd
from data_cleaning.transform_xlsx import transform_xlsx
from data_cleaning.clean_df_list import (clean_df_list, clean_df)
from data_cleaning.clean_float_list import convert_float_list
from data_cleaning.clean_date_list import convert_date_list
from data_cleaning.merge_dataframes import(merge_dataframes, merge_df_list)
from data_cleaning.filter_date_df import filter_date_df
from data_cleaning.rename_col_output import renamecol_ouput
from data_analysis.quotes_return import quotes_return
from data_analysis.base_hundred import base_hundred
from data_analysis.relative_strange import relative_strange
from data_output.plot import plot_close
from data_output.plot import plot_rs

#Imporo los archivos y los agrego a una lista
USD_BLUE_FILE_PATH = './data/quotes/usd_blue.xlsx'
ALUA_FILE_PATH = './data/quotes/alua.xlsx'
GGAL_FILE_PATH = './data/quotes/ggal.xlsx'
YPFD_FILE_PATH = './data/quotes/ypfd.xlsx'
EDN_FILE_PATH = './data/quotes/edn.xlsx'

XLSX_LIST = [USD_BLUE_FILE_PATH, ALUA_FILE_PATH, GGAL_FILE_PATH, YPFD_FILE_PATH, EDN_FILE_PATH]

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

print('Initial data cleaning ok')

#####
lista_prueba = ['usd','alua','ggal','ypfd','edn']
prueba = merge_df_list(df_list, on='fecha', how='left')
prueba[0] = prueba[0].dropna(subset='cierre_y')
prueba[1] = prueba[1].dropna(subset='cierre_y')
prueba[2] = prueba[2].dropna(subset='cierre_y')
prueba[3] = prueba[3].dropna(subset='cierre_y')

print(prueba)
quotes_return(prueba)
base_hundred(prueba)
relative_strange(prueba)

print(prueba)


with pd.ExcelWriter('./data/output/prueba.xlsx') as writer:
    prueba[1].to_excel(writer, sheet_name = 'rs_df', index=False)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(prueba[1]['fecha'],prueba[1]['X/USD'], linestyle='-')
plt.show()

#Ejecuto las funciones de data_analysis
#quotes_return(df_list)
#base_hundred(df_list)
#relative_strange(df_list)

print('Data analysis ok')

#Ejecuto la función para unir todo en un mismo dataframe
merged_df = merge_dataframes(df_list,on_column='fecha', suffixes=[None], how='left')

#Elimino los datos Nan y corrigo los indices
merged_df = merged_df.dropna().reset_index(drop=True)

print('Merge ok')

#Creo subset final filtrando columnas del merge. Renombro las columnas que se modificaron
#despúes del merge
rs_df = merged_df[['fecha','RS X/USD_1','RS X/USD_2', 'RS X/USD_3', 'RS X/USD_4', 'RS X/USD']]

#Creo una lista con los nombres de las columnas finales
RS_COL_NAME = ['USDB', 'ALUA/USDB', 'GGAL/USDB', 'YPFD/USDB', 'EDN/USDB']

#Renombro usando los indices de la lista anterior
rs_df = rs_df.rename(columns={
    'RS X/USD_1':RS_COL_NAME[0],
    'RS X/USD_2':RS_COL_NAME[1],
    'RS X/USD_3':RS_COL_NAME[2],
    'RS X/USD_4':RS_COL_NAME[3],
    'RS X/USD':RS_COL_NAME[4],
    })


usd_df = merged_df[['fecha','cierre_1','retorno_1']]
alua_df = merged_df[['fecha','cierre_2','retorno_2']]
bma_df = merged_df[['fecha','cierre_3','retorno_3']]
bbar_df = merged_df[['fecha','cierre_4','retorno_4']]
edn_df = merged_df[['fecha','cierre','retorno']]

#Creo una lista con los nombres de los activos utilizados
ASSET_NAME = ['USDB', 'ALUA', 'GGAL', 'YPFD', 'EDN']

#Creo una lista con los df de los activos utilizados
ASSET_LIST = [usd_df, alua_df, bma_df, bbar_df,edn_df]

ASSET_LIST = renamecol_ouput(ASSET_LIST,'cierre_','cierre')
ASSET_LIST = renamecol_ouput(ASSET_LIST,'retorno_','retorno')

print('Merge data cleaning ok')

#Salida de resultados en un archivo Excel
with pd.ExcelWriter('./data/output/rs_analysis.xlsx') as writer:
    rs_df.to_excel(writer, sheet_name = 'rs_df', index=False)
    ASSET_LIST[0].to_excel(writer, sheet_name = f'{ASSET_NAME[0]}', index=False)
    ASSET_LIST[1].to_excel(writer, sheet_name = f'{ASSET_NAME[1]}', index=False)
    ASSET_LIST[2].to_excel(writer, sheet_name = f'{ASSET_NAME[2]}',index=False)
    ASSET_LIST[3].to_excel(writer, sheet_name = f'{ASSET_NAME[3]}', index=False)
    ASSET_LIST[4].to_excel(writer, sheet_name = f'{ASSET_NAME[4]}', index=False)

print("Xlsx output ok")

#Saiida de gráfico de imagenes
plot_rs(rs_df.tail(126), RS_COL_NAME)
plot_close(ASSET_LIST[0].tail(250),'cierre',ASSET_NAME[0])
plot_close(ASSET_LIST[1].tail(250),'cierre',ASSET_NAME[1])
plot_close(ASSET_LIST[2].tail(250),'cierre',ASSET_NAME[2])
plot_close(ASSET_LIST[3].tail(250),'cierre',ASSET_NAME[3])
plot_close(ASSET_LIST[4].tail(250),'cierre',ASSET_NAME[4])

print("Png output ok")
