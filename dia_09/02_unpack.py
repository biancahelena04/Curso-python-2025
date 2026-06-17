#%%

A = 1
B = 5


print(A)
print(B)

# %%

C = A
A = B
B = C

print(A)
print(B)
# %%

A, B = B, A
print(A)
print(B)
# %%

c, d = A, B #tupla # = B, A = A, B

#%%
a, b, *args = 1, 2, 3, 4
print(a,b, args)

a, *args, b = 1, 2, 3, 4
print(a,b, args)

*args, a, b = 1, 2, 3, 4
print(a,b, args)

#%%

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1, 2, 55, 77)

#%%

def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)


# %%

dados = {"nome":"teo", "sobrenome":"calvo"}
for i, j in dados.items():
    print(i,j)
# %%
