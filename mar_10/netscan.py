
servidor = ['Servidor']
laptop = ['Laptop']
impresora = ['Impresora']

netmap = [
    servidor,
    laptop,
    impresora
]

puerto = 0
option = 0
while puerto != -1:
    option = int(input('Selecciona el dispositivo a escanear: \n' \
    '1. Servidor \n' \
    '2. Laptop \n' \
    '3. Impresora \n'))
    match option:
        case 1:
            puerto = int(input('Inserta el puerto escaneado: '))
            if puerto == -1:
                break
            else:    
                servidor.append(puerto)
                print('Puerto guardado')
        case 2:
            puerto = int(input('Inserta el puerto escaneado: '))
            if puerto == -1:
                break
            else:    
                laptop.append(puerto)
                print('Puerto guardado')

        case 3:
            puerto = int(input('Inserta el puerto escaneado: '))
            if puerto == -1:
                break
            else:    
                impresora.append(puerto)
                print('Puerto guardado')

        case _:
            print('Selecciona una opcion valida')
print('Los puertos escaneados fueron:')

for map in netmap:
    for e in map:
        print(e)