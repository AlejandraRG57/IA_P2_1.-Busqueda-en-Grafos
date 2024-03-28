
#Alejandra Rodriguez Guevara 21310127 6E1

#La búsqueda Tabú es una técnica de optimización combinatoria que se basa en el concepto de memoria a corto plazo para evitar ciclos repetitivos y escapar de óptimos locales.
#En este enfoque, se mantienen en memoria ciertos movimientos recientes como "tabúes", lo que impide que el algoritmo vuelva a realizar esos movimientos en las siguientes iteraciones.

import random
def objective(position): #Definimos la función objetivo la cual asigna un valor a cada posición en el grafo.
   
    coords = {         #Declaramos nuestras coordenadas de nuestro grafo en base a la imagen "00.3_Mapa-de-Busqueda_Imagen-Referencia.png", dandole un valor arbitrario a cada coordenada.
        ('0', '6'): 0.0, # 'A'
        ('1', '4'): 0.3, # 'B'
        ('0', '3'): 0.2, # 'C'
        ('2', '0'): 0.5, # 'D'
        ('2', '5'): 0.3, # 'E'
        ('2', '2'): 0.3, # 'F'
        ('5', '6'): 0.4, # 'G'
        ('4', '3'): 0.2, # 'H'
        ('4', '1'): 0.2, # 'I'
        ('6', '5'): 0.4, # 'J'
        ('7', '3'): 0.3, # 'K'
        ('6', '0'): 0.3, # 'L'
        ('8', '6'): 0.3, # 'M'
        ('9', '4'): 0.7  # 'N'
    }
    return coords.get(position, 0.0) #Devolvemos el valor de la posición en caso de existir en el diccionario, de lo contrario, devuelve 0.0.

def tabu_search(max_iter, rows_range, columns_range, tabu_list_size):
    tabu_list = []  #Inicializamos la lista tabú como vacía.

    current_position = (random.choice(rows_range), random.choice(columns_range))    #Inicializamos la posición actual de manera aleatoria.
    current_value = objective(current_position)

    best_tabu_position = current_position  #Almacenamos la mejor posición encontrada hasta ahora.
    best_tabu_value = current_value  #Almacenamos el valor asociado a la mejor posición.

    for _ in range(max_iter):
        neighbors = []  #Inicializamos la lista de vecinos.

        for row in rows_range: 
            for column in columns_range:
                if (row, column) != current_position:
                    neighbors.append((row, column))     #Inicializamos la posición actual de manera aleatoria

        if not neighbors:
            break  #Si no hay vecinos disponibles, terminamos el algoritmo.

        random.shuffle(neighbors)  #Barajeamos aleatoriamente la lista de vecinos.
        best_neighbor = None
        best_neighbor_value = float('-inf')
        for neighbor in neighbors:
            if neighbor not in tabu_list: #Evalúamos cada vecino potencial y elegimos el mejor vecino que no esté en la lista tabú.
                neighbor_value = objective(neighbor)
                if neighbor_value > best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        if best_neighbor is None:   #Si encontramos un vecino que no esté en la lista tabú, elegimos el mejor vecino disponible
            for neighbor in neighbors:
                neighbor_value = objective(neighbor)
                if neighbor_value > best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        current_position = best_neighbor   #Actualizamos la posición actual y la lista tabú.
        tabu_list.append(current_position)

        if len(tabu_list) > tabu_list_size: #Si nuestra lista tabú excede su tamaño máximo, eliminamos el elemento más antiguo.
            tabu_list.pop(0)

        if best_neighbor_value > best_tabu_value: #Si el valor del vecino es mejor que el mejor valor encontrado hasta ahora, actualizamos la mejor posición y valor.
            best_tabu_position = best_neighbor
            best_tabu_value = best_neighbor_value

    return best_tabu_position, best_tabu_value

rows_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #Filas en nuestro grafo
columns_range = ['1', '2', '3', '4', '5', '6'] #Columnas en nuestro grafo
max_iter = 1000   #Número máximo de iteraciones.
tabu_list_size = 7 #Tamaño maximo de nustra lista tabu

#Llamamos a la función tabu_search con los parámetros dados y almacenamos los resultados en best_tabu_position y best_tabu_value
best_tabu_position, best_tabu_value = tabu_search(max_iter, rows_range, columns_range, tabu_list_size)

#Imprimimos un mensaje que indica la mejor posición encontrada y su valor asociado.
print(f"La mejor posición encontrada mediante busqueda tabu es {best_tabu_position} con un valor de {best_tabu_value}.")
