#%%

conta =  0
texto = "Faça se pedido! Escolha uma base entre casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)"
texto2 = "Agora escolha o sabor entre: morango, creme ou chocolate"
texto3 = "Finalize com a cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)"
etapa = 1
while etapa != 4:
    if etapa == 1:
        opcao_base = input(texto)
        if opcao_base == "casquinha":
            conta = 1.00
            etapa = 2
        elif opcao_base == "cascão":
            conta = 2.50
            etapa = 2
        elif opcao_base == "cestinha":
            etapa = 2
            conta = 4.00
        else:
            print("escolha uma opção de base")

    if etapa == 2:
        opcao_sabor = input(texto2)
        if not (opcao_sabor == "morango" or opcao_sabor == "creme" or opcao_sabor == "chocolate"):
            print("escolha um sabor")
        else:
            etapa = 3

    if etapa == 3:
        opcao_cobertura = input(texto3)
        if opcao_cobertura == "caramelo":
            conta += 1.00 
            etapa = 4
        elif opcao_cobertura == "morango":
            conta += 2.50
            etapa = 4
        elif opcao_cobertura == "chocolate":
            conta += 4.00
            etapa = 4
        elif opcao_cobertura == "sem cobertura":
            conta += 0.00
            etapa = 4
        else:
            print("escolha uma opção de cobertura")

print("Sua conta deu:", conta)
# %%
