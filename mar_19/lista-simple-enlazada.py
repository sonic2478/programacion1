# 1. Creamos los agentes (nodos) por separado
nodo1 = {"nombre": "Ana",    "siguiente": None}
nodo2 = {"nombre": "Beto",   "siguiente": None}
nodo3 = {"nombre": "Laura",   "siguiente": None}

# 2. CONECTAMOS la cadena (esto es crear la lista enlazada)
nodo1["siguiente"] = nodo2  # Ana apunta a Beto
nodo2["siguiente"] = nodo3  # Beto apunta a Laura
# agente3 se queda en None porque nadie sigue después de él

# 3. Definimos la puerta de entrada
actual = nodo1

print("--- Recorriendo la lista ---")

while actual is not None:
    print(f"Agente encontrado: {actual['nombre']}")
    
    # EL SALTO: Movemos al nodo actual al diccionario que sigue
    actual = actual["siguiente"]

print("Fin de la lista.")