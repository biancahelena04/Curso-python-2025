#%%

txt = "hello\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:  #"w" escreve novos arquivos e "a" adiciona texto com o que já foi escrito
        open_file.write(txt)