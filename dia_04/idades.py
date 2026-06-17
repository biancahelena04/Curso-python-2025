#%%

idades = []

while True:
    idade = input("entre com a idade:")
    if idade == "":
        break
    idades.append(int(idade))

print(idades)

print("media", sum(idades)/ len(idades))
print("min", min(idades))
print("max", max(idades))
print("qtde", len(idades)) 

print("media", sum(idades)/ len(idades))
print("min", min(idades))
print("max", max(idades))
print("qtde", len(idades)) 