"""
    Creado por Facu
"""
import matplotlib.pyplot as plt

def plot_close(df,name_col,asset_name):
    """
        Esta función crea un gráfico. 
        sumar como parametro "src" para especificar el noonbre del grafico

    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title(f'Gráfico de {name_col} de {asset_name}')
    plt.xlabel('Fecha')
    plt.plot(df['fecha'],df[f'{name_col}'], label=asset_name, linestyle='-')
    plt.grid(True)
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].min(), df['fecha'].max())
    # Ajustar diseño del gráfico
    plt.tight_layout()
    
    # Guardar el gráfico en un archivo de imagen
    plt.savefig(f'./data/final/{asset_name}_plot.png', dpi=300)

def plot_rs(df,rs_col_name):
    """
        Esta función crea un gráfico. 
        sumar como parametro "src" para especificar el noonbre del grafico

    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico de fuerza relativa intramercado')
    plt.xlabel('Fecha')
    plt.plot(df['fecha'],df[rs_col_name], label=rs_col_name, linestyle='-')
    plt.grid(True)
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].min(), df['fecha'].max())
    # Ajustar diseño del gráfico
    plt.tight_layout()
    # Guardar el gráfico en un archivo de imagen
    plt.savefig('./data/final/rsi_plot.png', dpi=300)