# %%

# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma = 0           # valor final

qtde_entradas = 4  # contador de entradas

for i in range(qtde_entradas): #range(0, 4)
    altura = input("entre com uma altura:")
    altura = float(altura)
    soma += altura

print ("soma das alturas = ", soma)
# %%
