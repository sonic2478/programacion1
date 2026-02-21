# Pedir 3 calificaciones y sacar el promedio.
# Si es mayor a 90, imprime "Felicidades, tu promedio es:" y el promedio.
# Sino, solo imprime el promedio

qualy1= int(input("Dame una calificacion de 0 a 100 "))
qualy2= int(input("Dame una segunda calificacion de 0 a 100 "))
qualy3= int(input("Dame una tercera calificacion de 0 a 100 "))
promedio = int((qualy1 + qualy2 + qualy3) / 3)
if promedio > 90:
    print("Felicidades, tu promedio es: ", promedio)

else:
    print(promedio)