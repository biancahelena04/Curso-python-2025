
#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
#%%

palavra = input("entre com uma palavra: ").lower()

count = 0

for letra in palavra:
    if letra == "a":
        count += 1

print(f"a palavra {palavra} possui {count} A.")
