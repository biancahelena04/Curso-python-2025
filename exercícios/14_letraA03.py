
#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
#%%

palavra = input("entre com uma palavra: ").lower()

#usando método das strings
count = palavra.count("a")

print(f"a palavra {palavra} possui {count} A.")
