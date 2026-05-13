original = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def renderizar(original):
    for fila in original:
        print((fila))


fila = int(input('Dame la fila que deseas modificar: \n'))
columna = int(input('Dame la columna que deseas modificar: \n'))
caracter = int(input('Dame un numero del 1 al 9 con el que deseas modificar la matriz: \n'))

original[fila][columna] = caracter

renderizar(original)

