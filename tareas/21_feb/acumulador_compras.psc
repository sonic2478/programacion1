Algoritmo acumulador_compras
	confirmacion <- 1
	precio <- 0
	cuenta <- 0
	productos <- 0
	MIENTRAS confirmacion == 1 Hacer
		ESCRIBIR 'Dame el precio del producto: '
		LEER precio
		cuenta <- cuenta + precio
		productos <- productos + 1
		ESCRIBIR 'Desea ingresar otro producto? (Conteste 1 para si y 0 para no)'
		LEER confirmacion
	FinMientras
	ESCRIBIR 'EL total a pagar es de ', cuenta, ' y el total de productos fue de ', productos
FinAlgoritmo
