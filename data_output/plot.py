"""
    Creado por Facu
"""
import matplotlib.pyplot as plt

def grafico_output(df,lista_col,nombre):
    """
        Esta función crea un gráfico. 
        sumar como parametro "src" para especificar el noonbre del grafico

    """
    # Configuración del gráfico
    # Tamaño del gráfico en pulgadas (800x400 píxeles)
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico de Fuerza Relativa')
    plt.xlabel('Fecha')
    print(1)
    plt.plot(df['fecha'],df[lista_col], linestyle='-')
    plt.grid(True)
    
    # Ajustar diseño del gráfico
    plt.tight_layout()
    print(2)
    # Guardar el gráfico en un archivo de imagen
    plt.savefig(f'./data/final/{nombre}.png', dpi=300)
