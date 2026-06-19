
#Faça um programa que verifique se o item que a pessoa escolheu para comprar na 
# loja está na lista: laranja, cerveja, miojo, carvão, picanha.
#%%

itens = "laranja cerveja miojo carvão picanha" 

escolha = input("escolha um item: ").lower()

if escolha in itens:
    print("seu item escolhido existe na lista")

else:
    print("escolha um item válido")