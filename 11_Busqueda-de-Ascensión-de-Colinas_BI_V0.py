#Alejandra Rodriguez Guevara 21310127 6E1
#La Búsqueda de Ascensión de Colinas (Hill Climbing) es un algoritmo de búsqueda local que se utiliza para encontrar un máximo local en una función.

#En el contexto de la búsqueda de caminos en grafos, puede utilizarse para encontrar un camino que maximice alguna función de evaluación local, 
#como la distancia entre nodos, el costo total del camino, mejor posicion y valor, etc.

import random #Importación del módulo random que nos sirve para elegir filas y columas aleatoriamente.

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

def hill_climbing(max_iter, rows_range, columns_range): #Función de escalada de colina que busca la mejor posición y valor en el grafo.
    best_value = float('-inf') #Mejor valor inicializado como negativo infinito.
    best_position = None #Mejor posición inicializada como None. 

    for _ in range(max_iter): #Ciclo de iteración para buscar la mejor posición y valor.
        row = random.choice(rows_range) #Elegimos aleatoriamente una fila y columna del rango especificado.
        column = random.choice(columns_range)
        actual_position = (row, column) #Evaluamos el valor en la posición actual.
        actual_value = objective(actual_position) 

        if actual_value > best_value: #Si el valor actual es mejor que el mejor valor encontrado hasta el momento,
            best_value = actual_value #actualizamos el mejor valor y la mejor posición.
            best_position = actual_position

    return best_position, best_value #Devolvemos la mejor posición y el mejor valor encontrados.

rows_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #Filas en nuestro grafo
columns_range = ['1', '2', '3', '4', '5', '6'] #Columnas en nuestro grafo
max_iter = 1000   #Número máximo de iteraciones.
best_position, best_value = hill_climbing(max_iter, rows_range, columns_range) #Llamamos a la función de escalada de colina para encontrar la mejor posición y valor.

print(f"La mejor posición encontrada es {best_position} con un valor de {best_value}.") #Imprimimos la mejor posición y valor encontrados.


