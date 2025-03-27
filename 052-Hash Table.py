"""
Implementar uma tabela Hash

Uma tabela hash é uma estrutura de dados que associa chaves a 
valores, permitindo operações de inserção, busca e remoção 
eficientes.

A implementação básica de uma tabela hash envolve:
- Função Hash: Converte uma chave em um índice dentro dos limites 
da tabela.
- Tratamento de Colisões: Maneira de lidar com situações em que 
diferentes chaves resultam no mesmo índice.
"""

#utilizando endereçamento aberto com sondagem linear para 
# tratamento de colisões
class TabelaHash:
    def __init__(self, tamanho=10):
        """
        - Inicializa a tabela hash com um tamanho específico.
        - Define o tamanho da tabela (padrão de 10).
        """
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        #Cria uma lista (self.tabela) com o número especificado 
        # de posições, todas inicialmente definidas como None.

    def funcao_hash(self, chave):
        """
        - Calcula o índice para uma chave
        - Utiliza a função embutida hash do Python para 
            transformar a chave em um número inteiro.
        """
        return hash(chave) % self.tamanho
        #Aplica o operador módulo (%) para garantir que o índice 
        # resultante esteja dentro dos limites da tabela.

    def inserir(self, chave, valor):
        #Insere um par chave-valor na tabela

        indice = self.funcao_hash(chave)
        #Calcula o índice para a chave usando funcao_hash

        #Sondagem linear para encontrar um slot disponível
        while self.tabela[indice] is not None:
            if self.tabela[indice][0] == chave:
            #Se a posição calculada já estiver ocupada (colisão),
            #  utiliza sondagem linear: verifica sequencialmente 
            #   as próximas posições até encontrar um slot vazio.

                # Atualiza o valor se a chave já existir
                self.tabela[indice] = (chave, valor)
                return
            indice = (indice + 1) % self.tamanho

        self.tabela[indice] = (chave, valor)
        #Se a chave já existir na tabela, atualiza seu valor

    def buscar(self, chave):
        """
        -Busca o valor associado a uma chave
        -Calcula o índice da chave
        """
        indice = self.funcao_hash(chave)

        # Sondagem linear para encontrar a chave
        #Usa sondagem linear para localizar a chave, retornando o
        #  valor associado se encontrada
        while self.tabela[indice] is not None:
        #Retorna None se a chave não for encontrada.
            if self.tabela[indice][0] == chave:
                return self.tabela[indice][1]
            indice = (indice + 1) % self.tamanho

        return None  # Retorna None se a chave não for encontrada

    def remover(self, chave):
        """Remove um par chave-valor da tabela."""
        indice = self.funcao_hash(chave)

        #Sondagem linear para encontrar a chave
        #Usa sondagem linear para localizar a chave e, se 
        # encontrada, define a posição como None para removê-la.
        while self.tabela[indice] is not None:
            if self.tabela[indice][0] == chave:
                self.tabela[indice] = None
                return True
                #Retorna True se a remoção for bem-sucedida; caso
                #  contrário, retorna False.
            indice = (indice + 1) % self.tamanho

        return False  # Retorna False se a chave não for encontrada

# Exemplo de uso
tabela = TabelaHash()
tabela.inserir("nome", "Ricardo")
tabela.inserir("idade", 37)
print(tabela.buscar("nome"))  # Saída: Alice
print(tabela.buscar("idade"))  # Saída: 30
tabela.remover("nome")
print(tabela.buscar("nome"))  # Saída: None
