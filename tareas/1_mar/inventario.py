# Actividad de Repaso Individual
# Variables, IF, Match-Case, While, Listas, For y Funciones

# Título: Práctica Integral de Python: Sistema de Gestión de Inventario 📦

# 🎯 Instrucciones:
# Crea un programa en Python que simule un pequeño inventario. El código debe cumplir con los siguientes requisitos:

# Entrada de Datos: Pide al usuario su nombre y guárdalo en una variable.
# Bienvenida: en una función mostrar_bienvenida() manda por parámetro el valor ingresado e imprimelo en un mensaje de bienvenida. Ejemplo: "Bienvenido a control de inventarios  Hugo Donald"
# Lista: Crea una lista llamada productos que ya contenga: "Laptop", "Mouse", "Teclado".
# Menú con Match-Case (si se tiene Python inferior a 3.10 usar if else): Usa un ciclo while para mostrar un menú. Usa match-case para las opciones:
# Caso 1: Mostrar la lista de productos usando un ciclo for y enumerate() o while y un contador para mostrar los productos de la siguiente manera:
# 1. Laptop
# 2. Mouse
# 3. Teclado
# etc.
# Caso 2: Agregar un producto nuevo a la lista usando .append().
# Caso 3: Eliminar un producto por su nombre usando .remove().
# Ejemplo: frutas.remove("pera")   # Elimina por valor
# Caso 4: Calcular estadísticas: mostrar cuántos productos hay (len()). Ejemplos en la presentación de "Listas y for" del día 17 de febrero
# Caso 5: Salir
# Control de Errores: Si el usuario intenta ingresar una opción inválida, usa un else o case _ para avisarle.

nombre = input('Escribe tu nombre: ')
productos = ['Laptop', 'Mouse', 'Teclado']
option = 0

def mostrar_bienvenida(nombre):
    print('Bienvenido a control de inventarios ', nombre)

def inventario():
    for index, producto in enumerate(productos):
                print(f'{index + 1}: {producto}')

mostrar_bienvenida(nombre)
while True:
    option = int(input(
        '\n Selecciona una opcion de las siguientes: \n' \
        '1. Mostrar la lista de productos \n' \
        '2. Agregar producto \n' \
        '3. Eliminar producto \n' \
        '4. Mostrar cantidad de productos \n' \
        '5. Salir \n'
    ))
    match option:
        case 1: 
            inventario()
        case 2: 
            nuevop = input('Escribe el nombre del producto que quieres agregar: \n')
            productos.append(nuevop)
            print('Producto agregado')
            print('El nuevo inventario es: \n')
            inventario()
        case 3:
            peliminado = input('Escribe el nombre del producto que quieres eliminar: \n')
            productos.remove(peliminado)
            print('Producto eliminado')
            print('El nuevo inventario es: \n')
            inventario()
        case 4: 
            print('La cantidad de productos en inventario es de: ', len(productos))
        case 5: break
        case _: print('Selecciona una opcion valida')