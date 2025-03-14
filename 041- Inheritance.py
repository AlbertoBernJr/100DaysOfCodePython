#Implement inheritance between classes

# Classe base para animais
class Animal:
    def __init__(self, nome):
        #[__init__(self)] = Construtor da classe Animal.
        #[nome] = parametro nome do animal.

        self.nome = nome

    def fazer_som(self):
        #Método abstrato para fazer som

        raise NotImplementedError("Subclasses devem implementar este método.")
        #ativa a exceção [NotImplementedError] e mostra a frase..

    def mover(self):
        #método abstrato para mover-se

        raise NotImplementedError("Subclasses devem implementar este método.")

#classe para cachorros
class Cachorro(Animal):
    def fazer_som(self):
    #Cachorro faz 'Au Au'

        return f"{self.nome} diz: Au Au!"

    def mover(self):
    #Cachorro corre

        return f"{self.nome} está correndo."

#classe para gatos
class Gato(Animal):
#herda métodos da classe [animal] dentro dos [ (..)]

    def fazer_som(self):
    #Gato faz 'Miau'

        return f"{self.nome} diz: Miau!"

    def mover(self):
    #Gato anda silenciosamente

        return f"{self.nome} está andando silenciosamente."
    
#------------------------------------------------------------------------------------
# Criando objetos das classes Cachorro e Gato
rex = Cachorro(nome="Rex")
mia = Gato(nome="Mia")

# Exibindo comportamentos dos animais
print(rex.fazer_som())
print(rex.mover())

print(mia.fazer_som())  
print(mia.mover())