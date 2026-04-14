# --- INICIO DEL CÓDIGO ---
usuario1 = {"nombre": "Alice", "siguiente": None}
usuario2 = {"nombre": "Bob",   "siguiente": None}
usuario3 = {"nombre": "Eve",   "siguiente": None}

# TAREA 1: Conecta a Alice con Bob, y a Bob con Eve.
# (Escribe las 2 líneas aquí)
usuario1['siguiente'] = usuario2
usuario2['siguiente'] = usuario3


# TAREA 2: Crea un usuario4 llamado "Mallory" y conéctalo al final de Eve.
# (Escribe las 2 líneas aquí)
usuario4 = {"nombre": "Mallory",   "siguiente": None}
usuario3['siguiente'] = usuario4

# TAREA 3: Haz el ciclo while para mostrar a los 4 en pantalla.
auxiliar = usuario1
while auxiliar is not None:
    print(f"Usuario:", {auxiliar["nombre"]})
    # (Escribe la línea del 'salto' aquí)
    auxiliar = auxiliar['siguiente']

print('Fin de la lista')