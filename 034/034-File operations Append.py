with open("034/texto.txt", "a", encoding="utf-8") as arquivo:
# Abrindo o arquivo em modo append ['a'] - adiciona mais palavras ao arquivo sem apagar as anteriores
    
    arquivo.write("\nAgora estou adicionando mais texto.")
#-------------------------------------------------------------------

with open("034/texto.txt", "r", encoding="utf-8") as arquivo:
# [with]: garante que o arquivo seja fechado automaticamente após o uso
# [encoding="utf-8"]: Define a codificação do arquivo
# [open("arquivo.txt", "r")]: Abre o arquivo [python.txt], que está dentro da pasta [032] no modo leitura ["r"]. 

    
    linhas = arquivo.readlines()  
    # Lê todas as linhas do arquivo
    # [readlines()] = ler todas as linhas do arquivo em uma lista

    for linha in linhas:
    # loop [for] = processa cada linha

        print(linha, end="")  
        # Exibe cada linha
        """ [end=""] =  Evita que o [print()] adicione uma nova linha extra,
        já que cada linha do arquivo já termina com [\n]. """