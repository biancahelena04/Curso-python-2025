#%%
# uma maneira de definir listas
idades = [28, 42, 43, 35, 28, 26, 38]

print(idades)

# %%

banana = ["banana", "amarela", "fruta", 1, 14, True]
print(banana)

#%%
type(banana)

#%%

# cor
print(banana[1])

# tipo
print(banana[2])

print(banana[0])

#%%
idades = [28, 42, 43, 35, 28, 26, 38, 42, 50, 100, 67]

print("soma idades", sum(idades))

print("qtde idades", len(idades))

print("média idades=", sum(idades)/ len(idades))

print("idade mínima=", min(idades))

print("idade máxima", max(idades))

#%%

banana = ["banana", 
          "amarela", 
          "fruta", 
          True,
          ["doce", "azeda", "amarga"], 
          ["maçã", "nanica", "prata"], 
          ["limão", "abacaxi", "morango"]]

print("tamanho:", len(banana))

print(banana[6][0])


#%%

tamanho = len(banana)
pos = tamanho - 1
frutas = banana[pos]

banana[pos][len(frutas)-1]

#%%
banana[-1][-2]

#%%
banana = ["banana", 
          "amarela", 
          "fruta", 
          True,
          ["doce", "azeda", "amarga"], 
          ["maçã", "nanica", "prata"], 
          ["limão", "abacaxi", "morango"]]

banana[0:4]
# dois últimos sabores
banana[4][1:3]

#%%
banana[4][-2:]
banana[0:4]
banana["start" : "stop" ]

#%%
tipos = banana[5]
tipos[::-1] 
# start: stop: step