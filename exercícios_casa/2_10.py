#Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...

#Exiba o número da sequência cuja posição foi informada:
#	A posição x corresponde ao número y


# %%

# Fn = posicao
# n = numero
# fibonacci = Fn = Fn-1 + Fn-2



# %%

def fibonacci(posicao) -> int: # 2 | 0 | 1
    if posicao == 0: # false | true | false
        return 0 # return 0
    if posicao == 1: # false | | true
        return 1
    return fibonacci(posicao-1) + fibonacci(posicao-2) # fib(2-1) + fib(2-2) | fib(2-1) + 0 |  1 + 0 

fibonacci(70)