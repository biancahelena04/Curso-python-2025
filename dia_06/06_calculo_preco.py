#%%

def calc_imp(preco:float, tx_base:float, **kwargs):  # kwargs é uma maneira de adicionar parâmetros nomeados de forma indefinido, de qtd indefinida, de tamanho indefinido, dentro da minha função
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%

calc_imp(100, 0.03, municipal=0.01, estadual=0.005, nacional=0.001)

#%%

impostos_gerais = {"municipal":0.01, "estadual":0.005, "nacional":0.001}
calc_imp(100, 0.03, **impostos_gerais, internacional=0.0001) # = calc_imp(100, 0.03, municipal=0.01, estadual=0.005, nacional=0.001)
# oséé
