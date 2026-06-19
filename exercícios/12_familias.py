
#%%
#Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("insira seu nome completo")
nome = nome.lower()

if 'calvo' in nome:
    print("essa pessoa é calvo")

else:
    print("essa pessoa não é calvo")

#%%
#Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("entre com seu nome completo: ")
nome = nome.lower()

if 'calvo' in nome.split(" "):
    print("essa pessoa é calvo")

if 'silva' in nome.split(" "):
    print("essa pessoa é silva")

if 'silva' not in nome and 'calvo' not in nome:
    print("essa pessoa não é calvo nem silva")