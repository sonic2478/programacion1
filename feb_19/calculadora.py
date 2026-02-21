
def suma(num1, num2):
    resultado = num1 + num2
    print('Tu resultado es: ', resultado)

def resta(num1, num2):
    resultado = num1 - num2
    print('Tu resultado es: ', resultado)


def multi(num1, num2):
    resultado = num1 * num2
    print('Tu resultado es: ', resultado)

def division(num1, num2):
    if num2 == 0:
        print('Ingresa un numero mayor a 0.')
    else: 
        resultado = num1 / num2
        print('Tu resultado es: ', resultado)

print('Bienvenido a la calculadora')
opcion = 0

while opcion != 5:
    opcion = int(input('Selecciona una opcion para tus dos numeros: \n' \
    '1. Suma \n' \
    '2. Resta \n' \
    '3. Multiplicacion \n' \
    '4. Division \n'))        
    match opcion:
        case 1: 
            num1 = int(input('Dame el primer numero '))
            num2 = int(input('Dame el segundo numero '))
            suma(num1, num2)
        case 2: 
            num1 = int(input('Dame el primer numero '))
            num2 = int(input('Dame el segundo numero '))
            resta(num1, num2)
        case 3: 
            num1 = int(input('Dame el primer numero '))
            num2 = int(input('Dame el segundo numero '))
            multi(num1, num2)
        case 4: 
            num1 = int(input('Dame el primer numero '))
            num2 = int(input('Dame el segundo numero '))
            division(num1, num2)
        case _: print('Selecciona una opcion valida')        