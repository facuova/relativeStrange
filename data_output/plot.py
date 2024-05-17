"""
    Creado por Facu
"""
import matplotlib.pyplot as plt

def grafico_output(df):
    """
        Esta función crea un gráfico. 
        sumar como parametro "src" para especificar el noonbre del grafico

    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico de Fuerza Relativa')
    plt.xlabel('Fecha')
    plt.plot(df['fecha'],df[['USDB','ALUA/USDB','BMA/USDB','BBAR/USDB']], linestyle='-')
    plt.grid(True)
    
    # Ajustar diseño del gráfico
    plt.tight_layout()
    # Guardar el gráfico en un archivo de imagen
    plt.savefig('./data/final/grafico_usd.png', dpi=300)
