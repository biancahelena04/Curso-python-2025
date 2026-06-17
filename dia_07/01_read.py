
#%%

class ArquivoDaBianca: 
    caminho_do_arquivo = None
    arquivo = None

    def __init__(self, caminho):
        self.caminho_do_arquivo = caminho
        self.arquivo = open(caminho)
    
    def close(self):
        self.arquivo.close()
        


arquivo = ArquivoDaBianca(r"C:\Users\bianc\OneDrive\Área de Trabalho\Curso-python-2025\dia_07\historia.txt")
arquivo.close()

print(arquivo.caminho_do_arquivo)


#%%
nome_arquivo = r"C:\Users\bianc\OneDrive\Área de Trabalho\Curso-python-2025\dia_07\historia.txt"

# abre arquivo em formato de leitura
file = open(nome_arquivo)


# lê os dados do arquivo
conteudo = file.read()

print(conteudo)

# fecha o arquivo
file.close()

#É POSSIVEL QUE VC SE ESUQÇA DE FECHAR O ARQUIVO

#%%

nome_arquivo = r"C:\Users\bianc\OneDrive\Área de Trabalho\Curso-python-2025\dia_07\historia.txt"



with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)


# %%
nome_arquivo = r"C:\Users\bianc\OneDrive\Área de Trabalho\Curso-python-2025\dia_07\historia.txt"


def func2(): 
    nome_arquivo = None
    print(nome_arquivo)

def func():
    print(nome_arquivo)



func2()
func()
# %%
class bianca:

    def __enter__(self):
        print("abriu")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechou")
        pass

with bianca() as _:
    print("dentro do with")