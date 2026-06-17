#Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

#	O número x é primo
#ou
#	O número x não é primo
#%%
numero = input()
numero = int(numero)
primo = "sim"

for i in range(numero-1, 1, -1):
    if numero % i == 0:
        primo = "nao"
        break
     

if primo == "sim":
    print("O número", numero, "é primo")
else:
    print("O número", numero, "não é primo")
# %%
