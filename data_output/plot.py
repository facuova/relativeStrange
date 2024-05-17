"""
    Creado por Facu
"""
import matplotlib.pyplot as plt

def grafico_output(df):
    """
        Esta función crea un gráfico
    """

    plt.figure(figsize=(10, 5))
    plt.plot(df['fecha'],df['USDB'], color='b', linestyle='-')
    plt.title('Gráfico de Precios')
    plt.xlabel('Fecha')
    plt.ylabel('USDB')
    plt.grid(True)
    plt.xticks(20)
    # Ajustar diseño del gráfico
    plt.tight_layout()
    # Guardar el gráfico en un archivo de imagen
    plt.savefig('./data/final/grafico_usd.png', dpi=300)