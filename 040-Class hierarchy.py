#Create a class hierarchy for different shapes (circle, square)

class Carro:
    def __init__(self, marca, modelo):
        #[__init__(self,)]= construtor da classe [carro]
        #[marca] = parametro marca do carro (ex: Ford, Toyota)
        #[modelo] = parametro modelo do carro (ex: Mustang, Corolla)

        self.marca = marca
        self.modelo = modelo
        self.ligado = False  #estado inicial do carro (desligado)

    def iniciar(self):
        #Liga o carro

        if self.ligado:
        #se o estado do carro for [ligado]

            print(f"{self.marca} {self.modelo} já está ligado.")
        else:
        #se o estado do carro não for [ligado]

            self.ligado = True
            print(f"{self.marca} {self.modelo} ligado.")

    def parar(self):
    #Desliga o carro

        if not self.ligado:
        #se o estado do carro já não estiver [ligado]

            print(f"{self.marca} {self.modelo} já está desligado.")
        else:
        #se o estado do carro for [ligado]

            self.ligado = False
            print(f"{self.marca} {self.modelo} desligado.")

    def status(self):
    #exibe o status atual do carro

        estado = "ligado" if self.ligado else "desligado"
        #determinando o valor da variável [estado]

        print(f"{self.marca} {self.modelo} está {estado}.")

#-------------------------------------------------------------------------------
# Criando um objeto da classe Carro
meu_carro = Carro(marca="Ford", modelo="Mustang")

# Verificando o status inicial
meu_carro.status()  # Saída: Ford Mustang está desligado.

# Ligando o carro
meu_carro.iniciar()

# Tentando ligar novamente
meu_carro.iniciar()

# Verificando o status
meu_carro.status()

# Desligando o carro
meu_carro.parar()

# Tentando desligar novamente
meu_carro.parar()

# Verificando o status final
meu_carro.status()