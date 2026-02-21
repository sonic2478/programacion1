Algoritmo area_rectangulo	
	base <- 0
	ESCRIBIR 'Dame la medida de la base de un rectangulo: '
	LEER base
	altura <- 0
	ESCRIBIR 'Dame la medida de la altura de un rectangulo: '
	LEER altura
	perimetro <- (base * 2) + (altura * 2)
	area <- base * altura
	ESCRIBIR 'El perimetro del rectangulo es de ', perimetro, ' y su area es de ', area
FinAlgoritmo