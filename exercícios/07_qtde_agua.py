# Altere o programa anterior para considerar a quantidade de garrafas de água

#%%
texto = """"escolha a sua água para comprar
(1) água mineral com gás - R$ 1.50
(2) água mineral sem gás - R$ 2.50
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0: 
    print("escolha entre 1 ou 2")

else:
    qtde = input("quantas garrafas?")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("sua conta deu R$" , valor_total)

    #%%
texto = """"escolha a sua água para comprar
(1) água mineral com gás - R$ 1.50
(2) água mineral sem gás - R$ 2.50
"""

opcao = input(texto)
qtde = int(input("Quantas garrafas? "))

if opcao == "1":
    valor = 1.5 * qtde
    print("sua conta deu R$" , valor)


elif opcao == "2":
    valor = 2.5 * qtde
    print("sua conta deu R$" , valor)

else:
    print("escolha um dado válido")
