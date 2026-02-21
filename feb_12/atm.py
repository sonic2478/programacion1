saldo = 1000

while True:
    option = int(input('Selecciona una opcion: \n 1. Depositar \n 2. Retirar \n 3. Consultar saldo \n 4. Salir \n'))
    match option:
        case 1: 
            cantidad = int(input('Escribe el monto que quieres depositar: '))
            saldo = saldo + cantidad
            if saldo > 26000:
                print('Has alcanzado el tope de saldo en esta cuenta. \n Por favor contactanos para mejorar tu cuenta.')
                break
            print('Tu nuevo saldo es de ', saldo) 

        case 2: 
            cantidad = int(input('Escribe el monto que quieres retirar: '))
            if cantidad > saldo:
                print('La cantidad a retirar es mayor al saldo disponible. \n Tu saldo actual es de ', saldo)
            else:    
                saldo = saldo - cantidad
                print('Tu nuevo saldo es de ', saldo) 

        case 3: 
            print('Tu saldo es de ', saldo)

        case 4: 
            print('Sesion finalizada. Vuelva pronto')
            break

        case _: 
            print('Opcion no valida')

        

