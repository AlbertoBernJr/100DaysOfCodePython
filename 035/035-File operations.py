#Calculate the average of numbers in a text file

# Abrindo o arquivo para leitura
with open("035/calc1.txt", "r", encoding="utf-8") as arquivo:
# Lendo todas as linhas do arquivo
# [with]: garante que o arquivo seja fechado automaticamente após o uso
# [encoding="utf-8"]: Define a codificação do arquivo
# [open("arquivo.txt", "r")]: Abre o arquivo [calc1.txt], que está dentro da pasta [035] no modo leitura ["r"].
    
    linhas = arquivo.readlines()
    # Lê todas as linhas do arquivo
    # [readlines()] = ler todas as linhas do arquivo em uma lista

    
    numeros = [float(linha.strip()) for linha in linhas]
    # Convertendo as linhas para números (float)
    # [linha.strip()] = Remove espaços em branco e quebras de linha [\n] de cada linha

    # Calculando a média
    if numeros:  # Verifica se a lista não está vazia
        media = sum(numeros) / len(numeros)
        # [sum] = soma todos os valores da lista [numeros]
        # [len] = conta quantos valores tem dentro da lista [numeros]

        print(f"A média dos números no arquivo calc1 é: {media}")

    else:
        print("O arquivo está vazio.")

#------------------- arquivo calc2 --------------------
with open("035/calc2.txt", "r", encoding="utf-8") as arquivo:
    linha = arquivo.readline().strip()  
    # Lê a única linha do arquivo 

    numeros = [float(numero) for numero in linha.split(",")]  
    # le cada número e separa os números em partes sempre que encontrar [,]

    media = sum(numeros) / len(numeros)
    print(f"A média dos números do arquivo calc2 é: {media}")