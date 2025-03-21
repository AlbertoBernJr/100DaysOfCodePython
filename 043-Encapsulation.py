#Implement encapsulation in a class
"""
encapsulamento = tornar os atributos privados e fornecer métodos públicos para acessá-los e 
modificá-los de forma controlada
> atributos privados são prefixados com [ __ ] e métodos getters e setters.
"""

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
    #[__init__]: O construtor da classe, que inicializa os atributos [titular] e [saldo]
    #[titular]: parametro nome do titular da conta.
    #[saldo_inicial]: parametro para o Saldo inicial da conta (opcional, padrão é 0).

        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Método getter para o titular
    def get_titular(self):
        return self.__titular

    # Método setter para o titular
    def set_titular(self, novo_titular):
    #Altera o titular da conta

        if isinstance(novo_titular, str) and novo_titular.strip():
        #A função [ isinstance() ] retorna [ True ] se o objeto [ novo_titular ] for do 
        #   tipo especificado [ str ], e False caso contrário.
        #Verifica se é uma string não vazia
        # [ strip() ] remove espaços em branco (espaços, tabulações, quebras de linha)

    
            self.__titular = novo_titular
        else:
            print("Erro: O titular deve ser uma string não vazia.")

    # Método getter para o saldo
    def get_saldo(self):
    #Retorna o saldo atual da conta

        return self.__saldo

    def depositar(self, valor):
    #Realiza um depósito na conta.
    #[ valor ]: parametro do valor a ser depositado.

        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        #Realiza um saque na conta
        #[ valor ]: parametro do valor a ser sacado.

        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
            else:
                print("Erro: Saldo insuficiente.")
        else:
            print("Erro: O valor do saque deve ser positivo.")

    def verificar_saldo(self):
    #Exibe o saldo atual da conta.

        print(f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}")

# Criando uma conta bancária
conta = ContaBancaria(titular="João", saldo_inicial=1000)

# Acessando o titular e o saldo usando métodos getters
print("Titular:", conta.get_titular())  
print("Saldo inicial:", conta.get_saldo())

# Alterando o titular usando o método setter
conta.set_titular("Maria")
print("Novo titular:", conta.get_titular())

# Tentando alterar o titular para um valor inválido
conta.set_titular("")

# Realizando operações de depósito e saque
conta.depositar(500) 
conta.sacar(200)

# Verificando o saldo final
conta.verificar_saldo()