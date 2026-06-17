#%%

lista = [1, 1, 1, 2, 3, 2, 4, 1, 5, 7, 4, 3, 1,]

numero = input("escolha um número:")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1
print("quantidade de", numero, ":", contador)
