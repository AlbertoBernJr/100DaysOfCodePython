# Handle exceptions for file not found

arq = ["037/texto1.txt", "037/texto2.txt", "037/texto3.txt"]
#lista [arq] com o nome dos arquivos de texto

for arquivo in arq:
#A variável [arquivo] se tornará cada valor da lista [arq]
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
        #tentará abrir o arquivo [arquivo] no modo leitura/read [r]

            conteudo = f.read()
            print(f"Conteúdo de {arquivo}:\n{conteudo}")
            print(f"-----------------")
    except FileNotFoundError:
    #se o arquivo não existir, a exceção [FileNotFoundError] será ativada

        print(f"Erro: O arquivo {arquivo} não foi encontrado.\n")