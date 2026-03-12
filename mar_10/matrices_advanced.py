def renderizar(mapa):
    for fila in mapa:
        print(' '.join(fila))

def constructora(fila,columna):
    mapa[fila][columna] = '🏠'

def plantadora(fila,columna):
    mapa[fila][columna] = '🌲'

def oleada(fila,columna):
    mapa[fila][columna] = '💧'



mapa = [
    ['🟩','🟩','🟩','🟩','🟩'], 
    ['🟩','🟩','🟩','🟩','🟩'],
    ['🟩','🟩','🟩','🟩','🟩'],
    ['🟩','🟩','🟩','🟩','🟩'],
    ['🟩','🟩','🟩','🟩','🟩'],
]
while True:
        option = int(input('Elige una opcion: \n' \
        '1. Casa \n' \
        '2. Pino \n' \
        '3. Ola \n' \
        '4. Salir \n'))
        match option:
            case 1: 
                fila = int(input('Indica en que fila quieres construir tu casa (fila)'))
                columna = int(input('Indica en que columna quieres construir tu casa (columna)'))
                ubi = constructora(fila,columna)
                renderizar(mapa)

            case 2:
                fila = int(input('Indica en que fila quieres construir tu casa (fila)'))
                columna = int(input('Indica en que columna quieres construir tu casa (columna)'))
                ubi = plantadora(fila,columna)
                renderizar(mapa)
            case 3:
                fila = int(input('Indica en que fila quieres construir tu casa (fila)'))
                columna = int(input('Indica en que columna quieres construir tu casa (columna)'))
                ubi = oleada(fila,columna)
                renderizar(mapa)
            
            case 4: 
                break
            case _: 
                print('Elige una opcion valida')

renderizar(mapa)
