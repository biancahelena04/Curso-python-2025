#Construa um programa que realiza o sorteio de um número entre 1 e 15.
#
#O usuário terá 3 chances de acertar o valor.
#
#A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
#
#Caso o usuário acerte, dê os parabéns.


# numero_sorteio = 7
# for i in range(3):
#     numero_usuario = int(input("entre com um número "))
#     if not 1 <=  numero_usuario <= 15: # igual a if numero_usuario < 1 or numero_usuario > 15
#         continue

#     if numero_sorteio == numero_usuario:
#         print("parabéns!")
#         break

#     elif numero_usuario > numero_sorteio:
#         print("número muito alto!")

#     else:
#         print("número muito baixo")

# else:
#     print("suas tentativas acabaram")



# numero_sorteio = 7
# for i in range(3):
  
#     while True:
#         try:
#             numero_usuario = int(input("entre com um número "))
        
#         except ValueError as err:
#             print("valor inválido!")
#             continue
        
#         if 1 <= numero_usuario <= 15: # igual a if numero_usuario < 1 or numero_usuario > 15
#             break
        
#         print("o valor deve ser entre 1 e 15")

#     if numero_sorteio == numero_usuario:
#         print("parabéns!")
#         break

#     elif numero_usuario > numero_sorteio:
#         print("número muito alto!")

#     else:
#         print("número muito baixo")

# else:
#     print("suas tentativas acabaram")

# import random

# def get_input():
#     while True:
#         try:
#             numero_usuario = int(input("entre com um número "))
        
#         except ValueError as err:
#             print("valor inválido!")
#             continue
        
#         if 1 <= numero_usuario <= 15: # igual a if numero_usuario < 1 or numero_usuario > 15
#             return numero_usuario
        
#         print("o valor deve ser entre 1 e 15")



# numero_sorteio = random.randint(1,15)

# for i in range(3):

#     numero_usuario  = get_input()

#     if numero_sorteio == numero_usuario:
#         print("parabéns!")
#         break

#     elif numero_usuario > numero_sorteio:
#         print("número muito alto!")

#     else:
#         print("número muito baixo")

# else:
#     print("suas tentativas acabaram")

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("entre com um número "))
        
        except ValueError as err:
            print("valor inválido!")
            continue
        
        if 1 <= numero_usuario <= 15: # igual a if numero_usuario < 1 or numero_usuario > 15
            return numero_usuario
        
        print("o valor deve ser entre 1 e 15")


def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("parabéns!")
        return True
     
    elif usuario > sorteio:
        print("número muito alto!")
        return False

    else:
        print("número muito baixo")
        return False


numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario  = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break
   
else:
    print("suas tentativas acabaram")

