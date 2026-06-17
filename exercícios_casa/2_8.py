

#Refaça o exercício 2.4 utilizando for e listas para receber as notas dos alunos

#%%

#Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

#Média: x
#Menor: y
#Maior: z


#%%
notas = []
# count = 0
for count in range(0, 4):
    nota = float(input("insira a nota"))
    notas.append(float(nota))
    # count += 1
media = (sum (notas)/len(notas))
minima = min(notas)
maxima = max(notas)

print("média:", media, "máxima:", maxima, "minima:", minima) 
