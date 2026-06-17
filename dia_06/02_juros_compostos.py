# %%

def juros_compostos(aporte: int, taxa: float, anos: int)-> float:
    """juros_compostos servem para calcular o retorno financeiro a partir de um aporte, deve-se considerrar um valor, a taxa de juros atual e o tempo em anos para calculo do valor a ser retornado

aporte: 
um número inteiro, que represente o valor em reais

taxa:
um número float entre 0 e 1 que represente o valor da taxa

anos:
um número inteiro >= 1 que represente o tempo que o investimento terá liquidez
"""
    return aporte*(1+taxa)**anos # ** = elevado


# %%

juros_compostos(1000, 0.13, 4) # na ordem da função definida, caso os nomes estejam derfinidos 
                               # (ex.: aporte=1000, taxa=0.13, anos=4) a ordem pode ser mudada 

# %%
juros_compostos(aporte = 1000, taxa = 0.13, anos = 5)


# %%
juros_compostos()