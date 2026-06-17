# tuplas: listas que nào podem ser alteradas

#%%
dados_teo = [32, 1, "casado", "dev golang"]
dados_teo

#%%
dados_teo.append("2500,00")
dados_teo[0]= 28
dados_teo

# %%

# tupla_teo = 32, 1, "casado", "dev golang"
tupla_teo = (32, 1, "casado", "dev golang")

print(type(tupla_teo))
print(tupla_teo)
# %%
tupla_teo[0] = 28 # não suporta edições