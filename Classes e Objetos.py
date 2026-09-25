
#classe pai

class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 #todo carro começa parado

    def acelerar(self,incremento):
        self.velocidade += incremento

    def frear(self,decremento):
        self.velocidade -= decremento


    def status(self):
        return(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")

class carro(veiculo):
        def __init__(self, marca, modelo, ano, potencia):
            #super() chama o construtor da classe pai
            super().__init__(marca, modelo, ano)
            self.potencia = potencia

            #acelerando
        def acelerar(self, incremento):

            self.velocidade += incremento + self.potencia

class bicicleta(veiculo):
                def __init__(self, marca, modelo, ano, tipo):
                    super().__init__(marca, modelo, ano)
                    self.tipo = tipo

                def status(self):
                    return  (f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h, Tipo: {self.tipo}")

                #Testando os objetos

meu_carro = carro("Toyota", "Corolla", 2020, 150)
bicicleta1 = bicicleta("Caloi", "Mountain Bike", 2021, "Montanha")

meu_carro.acelerar(20)
bicicleta1.acelerar(10)

print("Status do carro:")
print(meu_carro.status())
print("Status da bicicleta:")
print(bicicleta1.status())