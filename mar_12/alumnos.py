
alumnos = []

def inscripcion(nombre,edad,carrera):
    alumno = {
        'nombre': nombre,
        'edad': edad,
        'carrera': carrera
    }
    alumnos.append(alumno)

while True:
    option = int(input('Selecciona una opcion \n' \
    '1. Agregar alumno \n' \
    '2. Salir \n'))
    match option:
        case 1: 
            nombre = input('Dame tu nombre: ')
            edad = input('Dame tu edad: ')
            carrera = input('Dame tu carrera: ')
            inscripcion(nombre,edad,carrera)
        case 2:
            break

for alumno in alumnos:
    for i,e in alumno.items():
        print(i,e)

 