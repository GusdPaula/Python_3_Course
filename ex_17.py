class Brand:
    def __init__(self, name):
        self.name = name
        self.cars = []


    def insert_car(self, car_name):
        self.cars.append(car_name)
    
    
    def __str__(self) -> str:
        return self.name + '\n' + str(self.cars)


class Engine:
    def __init__(self, name):
        self.name = name
        self.cars = []
    

    def insert_car(self, car_name):
        self.cars.append(car_name)
    

    def __str__(self):
        return self.name + "\n" + str(self.cars)


class Car:
    def __init__(self, name, brand, engine):
        self.name = name
        self.brand = brand
        self.engine = engine

        brand.insert_car(name)
        engine.insert_car(name)


    def __str__(self) -> str:
        return "Car name: " + self.name + "\n"\
                "Brand: " + self.brand.name + "\n"\
                "Engine: " + self.engine.name


fiat = Brand("Fiat")
v100 = Engine("V100")
palio = Car("Palio", fiat, v100)

print(palio)
print(v100)
print(fiat)


# Correct 
###########################################################
# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)