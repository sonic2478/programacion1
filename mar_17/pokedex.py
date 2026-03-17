
pokedex = []

def agregar(nombre,tipo,nivel):
    pokemon = {
        'nombre': nombre,
        'tipo': tipo,
        'nivel': nivel
    }
    pokedex.append(pokemon)
    print('Pokemon agregado')

def mostrar_pokedex():
    for p in pokedex:
        for i,e in p.items():
            print(i,e)

def eliminar_pokemon(nombre):
    pokedex.remove(nombre)

while True:
    option = int(input('Elige una opcion: \n' \
    '1. Ingresar pokemon \n' \
    '2. Mostrar Pokedex \n' \
    '3. Eliminar pokemon \n' \
    '4. Salir \n'))
    match option:
        case 1:
            nombre = input('Dame el nombre del pokemon que capturaste: ') 
            tipo = input('Dame el tipo de pokemon que capturaste: ') 
            nivel = input('Dame el nivel del pokemon que capturaste: ') 
            agregar(nombre,tipo,nivel)

        case 2:
            mostrar_pokedex()

        case 3:
            nombre = input('Dame el nombre del pokemon que deseas eliminar: ') 
            for p in pokedex:
                if nombre == p['nombre']:
                    pokedex.remove(p)
                    print('Pokemon eliminado')
                else:
                    print('Pokemon no encontrado')
        case 4:
            break

        case _: 
            print('Opcion no valida')





