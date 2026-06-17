# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

#%%
texto = """"escolha a sua água para comprar
(1) água mineral com gás 
(2) água mineral sem gás
"""

opcao = input(texto)

conta = 0

if opcao == "1":
    conta= 1.50

elif opcao == "2":
    conta = 2.50

if conta == 0:
    print("escolha entre 1 ou 2")

else:
    print("sua conta deu R$" , conta)