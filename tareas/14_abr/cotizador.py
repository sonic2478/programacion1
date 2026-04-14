pv = {
    'nombre': 'Puerto Vallarta',
    'costo_base': 7500
}
nv = {
    'nombre': 'Nuevo Vallarta',
    'costo_base': 7000
}
manz = {
    'nombre': 'Manzanillo',
    'costo_base': 8000
}
destinos = [
    pv,
    nv,
    manz
]
destinos_disponibles = []

def calcular_equipaje(maleta):
    if maleta < 10:
        return 0
    if maleta >= 10 and maleta <= 20:
        return 200
    if maleta > 20:
        return 500
    
def cotizacion():
    print(f'      --- ESTA ES TU COTIZACION--- \n'
                f'Viaje a {objetivo}, Costo ${costo} \n'
                f'Equipaje $ {equipaje} \n'
                f'--------------------------------------- \n'
                f'TOTAL A PAGAR: {costo + equipaje} \n'
                f'---------------------------------------')
    

presupuesto = int(input('Dime cual es tu presupuesto para el viaje: '))

for destino in destinos:
    if destino['costo_base'] < presupuesto:
        destinos_disponibles.append(destino)
if len(destinos_disponibles) == 0:
    print('Presuspuesto insuficiente para viajar')
else:
    for destino in destinos_disponibles:
        for i,e in destino.items():
            print(e)
viaje = int(input('Selecciona que numero de viaje quieres: ')) - 1
costo = destinos_disponibles[viaje]['costo_base']
objetivo = destinos_disponibles[viaje]['nombre']
option = int(input('Selecciona si deseas agregar equipaje: \n' \
'1. Si \n' \
'2. No \n'))
match option:
    case 1: 
        maleta = int(input('Inserta el peso de tu maleta: '))
        equipaje = calcular_equipaje(maleta)
        cotizacion()

    case 2: 
        equipaje = 0
        cotizacion()