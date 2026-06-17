# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

número= input ("entre com um número inteiro para calcular a raíz quadrada:")
número = int(número)
raíz = número ** (1/2) # numero ** 0.5
raíz = round(raíz, 4)
print("raíz quadrada de" , número, "é:", raíz)
