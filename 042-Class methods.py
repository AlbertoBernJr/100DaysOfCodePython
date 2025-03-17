#Criar uma classe para uma conta de banco com métodos de deposito e saque

class ContaBancaria:
    #metodo construtor
    def __init__(self, titular, saldo_inicial=0):
        #[__init__]: O construtor da classe, que inicializa os atributos [titular] e [saldo]
        #[titular]: parametro nome do titular da conta.
        #[saldo_inicial]: parametro para o Saldo inicial da conta (opcional, padrão é 0).


        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        #método para realizar um depósito na conta.
        #[valor]: parametro do Valor a ser depositado.

        if valor > 0:
        #se o numero do [valor] for positivo

            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
        #se o numero do [valor] for negativo

            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
    #Realiza um saque na conta.
    #[valor]: parametro do Valor a ser sacado.

        if valor > 0:
        #se o valor saque for positivo

            if self.saldo >= valor:
            #o saldo deve ser maior/igual ao valor do saque

                self.saldo -= valor
                #será descontado o valor do saque do saldo 

                print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
            else:
            #se o valor saque for maior que o saldo

                print("Erro: Saldo insuficiente.")
        else:
        #se o valor saque for negativo

            print("Erro: O valor do saque deve ser positivo.")

    def verificar_saldo(self):
    #Exibe o saldo atual da conta

        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

# Criando uma conta bancária
conta = ContaBancaria(titular="João", saldo_inicial=1000)

# Verificando o saldo inicial
conta.verificar_saldo()

# Realizando um depósito
conta.depositar(500)

# Realizando um saque
conta.sacar(200)

# Tentando sacar um valor maior que o saldo
conta.sacar(2000)

# Tentando depositar um valor negativo
conta.depositar(-100)

# Verificando o saldo final
conta.verificar_saldo()