

#%%
def soma(a: float, b: float, c:float):
    return a + b + c

def media(a: float, b: float, c=0):  # c=0 é opcional, argumentos opcionais devem vir sempre no final
    return soma(a, b, c) / 2

a = float(input("entre com valor de a"))
b = float(input("entre com valor de b"))
c = float(input("entre com valor de c"))

print("média:", media(a,b))





# %%
def soma(valores:list):
    return sum(valores)

def media(valores):  # c=0 é opcional, argumentos opcionais devem vir sempre no final
    return sum(valores) / len(valores)

a = float(input("entre com valor de a"))
b = float(input("entre com valor de b"))
c = float(input("entre com valor de c"))

print("média:", media([a,b,c]))





# %%
def soma(a:float, b: float, *args)->float:
    valores= [a,b]+list(args)
    return sum(valores)

def media(a:float, b: float, *args):  
    return soma(a, b, *args) / (len(args)+2)

a = float(input("entre com valor de a"))
b = float(input("entre com valor de b"))
c = float(input("entre com valor de c"))

print("média:", media(a,b,c))




#%%
a = [1,2,3]
b = [1,2,3] 
c = [1,2,3]

a+b+c