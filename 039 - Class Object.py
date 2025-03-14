# Create a class for a simple car with methods like start and stop

class Carro:
    def __init__(self, marca, modelo): 
    #[__init__] = O construtor da classe inicializa os atributos [marca], [modelo] e [ligado]
    #[marca] Marca do carro (ex: Ford, Toyota).
    #[modelo] Modelo do carro (ex: Mustang, Corolla).
    
        self.marca = marca #armazena a marca do carro
        self.modelo = modelo #armazena o modelo do carro
        self.ligado = False  #estado inicial do carro (desligado)

    def iniciar(self):
    #Liga o carro

        if self.ligado:
        #Se o carro já estiver ligado, exibe uma mensagem informando
            print(f"{self.marca} {self.modelo} já está ligado.")

        else:
        #Liga o carro, alterando o atributo [ligado] para [True]
            self.ligado = True
            print(f"{self.marca} {self.modelo} ligado.")

    def parar(self):
    #Desliga o carro.

        if not self.ligado:
        #Se o carro já estiver desligado, exibe uma mensagem informando isso
            print(f"{self.marca} {self.modelo} já está desligado.")

        else:
        #altera o atributo [ligado] para [False]
            self.ligado = False
            print(f"{self.marca} {self.modelo} desligado.")

    def status(self):
    #Exibe o status atual do carro - ligado ou desligado

        estado = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} está {estado}.")

#----------------------------------------------------------------------------------------
# Criando um objeto da classe Carro
meu_carro = Carro(marca="Ford", modelo="Mustang")

# Verificando o status inicial
meu_carro.status()  # Saída: Ford Mustang está desligado.

# Ligando o carro
meu_carro.iniciar()  # Saída: Ford Mustang ligado.

# Tentando ligar novamente
meu_carro.iniciar()  # Saída: Ford Mustang já está ligado.

# Verificando o status
meu_carro.status()  # Saída: Ford Mustang está ligado.

# Desligando o carro
meu_carro.parar()  # Saída: Ford Mustang desligado.

# Tentando desligar novamente
meu_carro.parar()  # Saída: Ford Mustang já está desligado.

# Verificando o status final
meu_carro.status()  # Saída: Ford Mustang está desligado.