# Funciones primeros inputs
acum = 0

def suma(num1, num2):
    resultado = num1 + num2
    print('Tu resultado es: ', resultado)
    global acum
    acum = acum + resultado

def resta(num1, num2):
    resultado = num1 - num2
    print('Tu resultado es: ', resultado)
    global acum
    acum = acum + resultado    

def multi(num1, num2):
    resultado = num1 * num2
    print('Tu resultado es: ', resultado)
    global acum
    acum = acum + resultado

def division(num1, num2):
    if num2 == 0:
        print('Ingresa un numero mayor a 0.')
    else: 
        resultado = num1 / num2
        print('Tu resultado es: ', resultado)
        global acum
        acum = acum + resultado

# Funciones para segunda o posteriores vueltas
def postsuma(num):
    global acum
    resultado = acum + num
    print(resultado)
    acum = resultado

def postresta(num):
    global acum
    resultado = acum - num
    print(resultado)
    acum = resultado

def postmulti(num):
    global acum
    resultado = acum * num
    print(resultado)
    acum = resultado

def postdivision(num):
    global acum
    if num == 0:
        print('Ingresa un numero mayor a 0.')
    else: 
        resultado = acum / num
        print('Tu resultado es: ', resultado)
        acum = resultado

print('Bienvenido a la calculadora')
opcion = 0
contador = 0
while True:
    opcion = int(input('Selecciona tu operacion a realizar: \n' \
    '1. Suma \n' \
    '2. Resta \n' \
    '3. Multiplicacion \n' \
    '4. Division \n' \
    '5. Salir \n'))        
    match opcion:
        case 1: 
            if contador == 0:
                num1 = int(input('Dame el primer numero '))
                num2 = int(input('Dame el segundo numero '))
                suma(num1, num2)
            else:
                num = int(input('Dame el siguiente numero que quieres usar: '))
                postsuma(num)
        case 2: 
            if contador == 0:
                num1 = int(input('Dame el primer numero '))
                num2 = int(input('Dame el segundo numero '))
                resta(num1, num2)
            else:
                num = int(input('Dame el siguiente numero que quieres usar: '))
                postresta(num)
        case 3: 
            if contador == 0:
                num1 = int(input('Dame el primer numero '))
                num2 = int(input('Dame el segundo numero '))
                multi(num1, num2)
            else:
                num = int(input('Dame el siguiente numero que quieres usar: '))
                postmulti(num)
        case 4: 
            if contador == 0:
                num1 = int(input('Dame el primer numero '))
                num2 = int(input('Dame el segundo numero '))
                division(num1, num2)
            else:
                num = int(input('Dame el siguiente numero que quieres usar: '))
                postdivision(num)
        case 5: 
            break
        case _: print('Selecciona una opcion valida')
    contador = contador +1