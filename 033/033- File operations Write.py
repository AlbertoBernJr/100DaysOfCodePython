# Write data to a text file

with open("033/texto.txt", "w", encoding="utf-8") as arquivo:
# abre o arquivo no modo escrita ["w"]
# [with] = Garante que o arquivo seja fechado automaticamente após o uso
# reescreve todo o arquivo = substitui as informações anteriores

    arquivo.write("Olá, mundo!\n")  # Escreve uma linha
    arquivo.write("Python é incrível.\n")  # Escreve outra linha
#------------------------------------------------------------------------

with open("033/texto.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  
    #Lê todas as linhas do arquivo

    for linha in linhas:
    # exibirá cada linha do arquivo
        print(linha, end="")