import matplotlib.pyplot as plt
import pandas as pd

def func1(value1:int,value2:int) -> int:
    
    """
    Função que retorna o quadrado ou a raiz quadrada de value1 dependendo do valor em value2
    """
    
    if value1 > value2:
        return value1**2
    elif value2 > value1:
        return value1**0.5
    else:
        return value1
    
def plot_topo(data):
    
    if not isinstance(data,pd.core.frame.DataFrame):
        raise TypeError(f'data deve ser do tipo pd.core.frame.DataFrame. Tipo recebido {type(data)}.')
    
    """
    recebe um dataframe e plota o mapa de contornos.
    params:
        data: dataframe contendo os valores para plotagem
    """
        
    f, ax = plt.subplots(1,1)
    ax.contourf(data,32,origin='upper')
    ax.set_yticklabels(data.index)
    ax.set_xticklabels(data.columns,rotation=90)
    plt.show()