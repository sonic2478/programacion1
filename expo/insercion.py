def insertion_sort(arr):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i] # El valor que vamos a insertar
        j = i - 1
        
        # Movemos los elementos mayores que la 'key' hacia la derecha
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insertamos la 'key' en su hueco exacto
        arr[j + 1] = key
        
    return arr

# Datos de prueba sincronizados con el simulador
data = [71, 12, 45, 3, 19, 8]
print(f"Lista original: {data}")
print(f"Lista ordenada: {insertion_sort(data)}")