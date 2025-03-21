#Use class decorators

"""
[decoradores] = são uma forma de modificar ou estender o comportamento de funções ou 
métodos sem alterar seu código diretamente.
- podem ser usados para modificar métodos, propriedades ou até a própria classe
"""
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    
    @property
    #O decorador [ @property ] transforma o método [saldo] em uma propriedade, permitindo 
    # acessá-lo como [ conta.saldo ] ->  permite acessar o valor de [ __saldo ] como se fosse
    #  um atributo público, sem precisar chamar o método como uma função.

    def saldo(self):
    #Getter para o saldo

        return self.__saldo

    @saldo.setter
    #[ @saldo.setter ] = define um método para alterar o valor de [ __saldo ]

    def saldo(self, valor):
    #Setter para o saldo
    
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Erro: O saldo não pode ser negativo.")

# Usando a classe
conta = ContaBancaria(titular="João", saldo_inicial=1000)
print("Saldo inicial:", conta.saldo)  # retorna o valor de [ __saldo ] (propriedade)

conta.saldo = 1500  # Altera o saldo usando o setter
print("Novo saldo:", conta.saldo)

conta.saldo = -500  # Tentativa de definir saldo negativo
print("Saldo após tentativa inválida:", conta.saldo)