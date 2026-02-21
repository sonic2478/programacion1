calificacion = int(input('Dame tu calificacion del 1 al 10 '))
contador = 1
while calificacion != -1:
    calificacion = int(input('Dame tu calificacion del 1 al 10 '))
    if calificacion >= 6:
        contador = contador + 1

print('Hubo ', contador, ' calificaciones aprobatorias.')

