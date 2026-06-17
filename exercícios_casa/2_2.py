

#FORMAS DE FAZER O PAR OU IMPAR

#%%
numero = input()
numero = int(numero)

resto = numero % 2 

if resto == 0:
    print("par")
else:
    print("impar")




    
# %%


def par_impar(numero: int):
    if numero % 2 == 0:
        print("par")
    else:
        print("ímpar")

numero = input("entre com um número")
numero = int(numero)

par_impar(numero)




#%%
def par_impar(numero: int):
        if numero % 2 == 0:
            return "par"

        else:
            return "ímpar"

numero = input("entre com um número")
numero = int(numero)

resultado = par_impar(numero)
print(numero, "é", resultado)

