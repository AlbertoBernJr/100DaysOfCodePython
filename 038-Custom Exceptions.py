#< Create a custom exception class >

"""
< aplicação simples que simula um sistema bancário, onde levantamos exceções personalizadas para 
lidar com erros de saldo insuficiente e limite de saque excedido. >
"""

#Exceção base para erros de negócio.
class ErroNegocio(Exception):
#Define uma nova classe de exceção chamada [ErroNegocio]
#A classe [ErroNegocio] herda de [Exception], que é a classe base para todas as exceções em 
    #Python

    pass
    """
    >[pass] = placeholder/marcador de lugar
    > quando você precisa definir uma estrutura (como uma classe, função ou bloco condicional) 
    mas ainda não quer ou precisa implementar o código dentro dela.
    >[pass] é usado porque a classe não precisa de nenhuma implementação adicional além de 
    herdar de [Exception]
    """

class SaldoInsuficienteError(ErroNegocio):
#Exceção para saldo insuficiente

    def __init__(self, mensagem):
    #define o método construtor [__init__] da classe
    #recebe um parâmetro [mensagem], que será a mensagem de erro associada à exceção

        super().__init__(mensagem)
        """
        Chama o construtor [__init__] da classe base [Exception] para garantir que a exceção seja 
        inicializada corretamente.
        """

class LimiteExcedidoError(ErroNegocio):
#Exceção para limite de saque excedido

    def __init__(self, mensagem):
        super().__init__(mensagem)

def sacar_dinheiro(saldo_atual, valor_saque, limite_saque):
#função para tenta realizar um saque.
    
    if valor_saque > saldo_atual:
        raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        #Levanta [SaldoInsuficienteError] se o saldo for insuficiente
        #[raise] = levante/ativa a exceção personalizada com uma mensagem específica

    if valor_saque > limite_saque:
        raise LimiteExcedidoError("Valor do saque excede o limite permitido.")
        #Levanta [LimiteExcedidoError] se o valor do saque exceder o limite
    return saldo_atual - valor_saque

#Exemplo de uso
try:
    saldo = 100  # Saldo atual
    saque = 122  # Valor do saque
    limite = 120  # Limite de saque

    # Tenta realizar o saque
    novo_saldo = sacar_dinheiro(saldo, saque, limite)
    print("Saque realizado com sucesso! Novo saldo:", novo_saldo)

except SaldoInsuficienteError as erro:
#armazena a exceção customizada na variável [erro]

    print("Erro de saldo:", erro)

except LimiteExcedidoError as erro:
    print("Erro de limite:", erro)

finally:
#sempre será exibido ao final do código
    print("Operação finalizada.")