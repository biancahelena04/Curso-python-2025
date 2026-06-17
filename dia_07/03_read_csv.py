

#%%
arquivos = "data.csv"

with open(arquivos) as file:
    lines = file.readlines()
print(lines)

for l in lines:
    print(l)

#%%

dados = dict()

chaves = lines[0].strip("\n").split(";") #strip tira o elemento, split "pula" ele e usa como separador
for c in chaves:
    dados[c] = []

print(dados)

#%%
for l in lines[1:]:
   valores = l.strip("\n").split(";")
   for i in range(len(valores)):
       dados[chaves[i]].append(valores[i])

dados

#%%
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/ len(idades)
media






#%%
nome = "Téo Calvo"
nome.split(" ")