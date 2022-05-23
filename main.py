import pickle


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return self.color + " " + self.ruedas + " " + self.puertas


coche = Vehiculo("Negro", "4", "5")
print(coche)
with open("coche.txt", "wb+") as file:
    pickle.dump(coche, file)

with open("coche.txt", "rb") as new_file:
    nuevo_coche = pickle.load(new_file)
    print(nuevo_coche)

