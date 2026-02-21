# class Clasefruta:
#     def init(self, fruta, verdura):
#         self.fruta = fruta
#         self.verdura = verdura
# misfrutas = grupo('Manzana', 'Zanahoria')
import random
numero_jugadores = int(input('Ingresa cuantas personas jugaran: '))
jugadores = []

for i in range(numero_jugadores):
    jugador = input('Jugador, escribe tu nombre: \n')
    jugadores.append(jugador)

print(jugadores)

for jugador in jugadores:
    dado = random.randint(1,6)
    print(jugador, ' saco: ', dado)
    
    while dado == 6:
        print('Felicidades, sacaste un 6. Tienes otra tirada \n')
        dado = random.randint(1,6)
        print(jugador, ' saco: ', dado)