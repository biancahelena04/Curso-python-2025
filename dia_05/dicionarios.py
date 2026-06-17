#%%

lista = [2, 132, "téo", ["ds", "da", "de"], True]

lista[2]

#%%

# dicionário = pares de chave/valor

dados_teo = {"sobrenome":"Calvo", "nome":"Téo", "filhos":True, "formacao":["estatística", "bigdata datascience"], 
             "cargos":[{"nome":"ds jr", "empresa":"tapps"}, 
                       { "nome":"ds pl", "empresa":"sas"}, 
                       {"nome":"ds sr", "empresa":"boticario"}, 
                       {"nome":"ds espec", "empresa":"via varejo"}]}

print(dados_teo)

dados_teo["nome"]

dados_teo["formacao"][-1]

dados_teo["cargos"][-1]["empresa"]

# %%
dados_teo["estado civil"] = "casado"

#%%

print(dados_teo)
#%%
dados_teo.keys()

# %%
print("valores:", dados_teo.values())
print("chaves:", dados_teo.keys())
print("itens:", dados_teo.items())

# %%
for i in [1,2,3,4,65,34,"téo"]:
    print(i)

#%%
for i in dados_teo:
    print(i, "->", dados_teo[i])

#%%
for i in dados_teo.items():
    print(i)

# %%
for chave, valor in dados_teo.items():
    print(chave, "->", valor)