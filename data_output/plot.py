"""
    Este módulo cuenta con las funciones para realizar los gráficos que se encontrarán en ./data/output
"""
import matplotlib.pyplot as plt

def plot_close(df,columns,name):
    """
        Función para realizar gráfico de línea de los últimos 126 peridos(medio año) 
        Parámetros:
            df (dataframe) : DataFrame
            columns (str): Debe indicar las columnas a graficar
            name (str): Nombre de título y de archivo con el que queremos que se guarde
        Return:
            plot.png: Archivo .png con el gráfico realizado en 
    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title(f'Gráfico de {columns} de {name}')
    plt.xlabel('Fecha')
    plt.plot(df['fecha'],df[f'{columns}'], label=name, linestyle='-')
    plt.grid(True)
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].min(), df['fecha'].max())
    # Ajustar diseño del gráfico
    plt.tight_layout()
    
    # Guardar el gráfico en un archivo de imagen
    plt.savefig(f'./data/output/{name}_plot.png', dpi=300)


def plot_rs(df,col_name):
    """
        Función para realizar gráfico de línea de los últimos 126 peridos(medio año)
        Parámetros:
            df (dataframe) : DataFrame
            col_name (list): Lista con los nombres con las columnas a grafica
        Return:
            plot.png: Archivo .png con el gráfico realizado
    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico de fuerza relativa intramercado')
    plt.xlabel('Fecha')
    plt.plot(df['fecha'],df[col_name], label=col_name, linestyle='-')
    plt.grid(True)
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].min(), df['fecha'].max())
    # Ajustar diseño del gráfico
    plt.tight_layout()
    # Guardar el gráfico en un archivo de imagen
    plt.savefig('./data/output/rsi_plot.png', dpi=300)