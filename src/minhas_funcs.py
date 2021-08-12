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