
#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
#%%

palavra = input("entre com uma palavra: ").lower()

count = 0

for letra in palavra:
    count += letra == "a"

print(f"a palavra {palavra} possui {count} A.")
