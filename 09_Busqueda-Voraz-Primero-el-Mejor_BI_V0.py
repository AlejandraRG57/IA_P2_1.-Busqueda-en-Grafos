#Alejandra Rodriguez Guevara 21310127 6E1
#Algoritmo de Búsqueda Voraz (Greedy Best-First Search) GBFS

#Se centra en explorar los nodos que parecen más prometedores según una función heurística.
#Se utiliza una función de evaluación para determinar qué nodo se expande primero.

import heapq

def GBFS(grafo, inicio, meta, heuristica):
    frontera = [(heuristica(inicio, meta), inicio)]  #Inicializamos la frontera con el nodo inicial y su valor heurístico
    visitados = set()  #Inicializamos un conjunto de nodos visitados

    distancia = 0  # Inicializamos la distancia acumulada
    
    while frontera:
        _, nodo_actual = heapq.heappop(frontera)  #Extraemos el nodo con menor valor heurístico de la frontera
        
        if nodo_actual == meta:  #Si el nodo actual es el nodo objetivo, se ha encontrado el camino
            return True, distancia
        
        visitados.add(nodo_actual)  #Agregamos el nodo actual a los nodos visitados
        
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                heapq.heappush(frontera, (heuristica(vecino, meta), vecino))  #Agregamos los vecinos a la frontera con sus valores heurísticos
                distancia += distancia_entre_nodos[nodo_actual][vecino]  # Sumamos la distancia al vecino
    
    return False, distancia  #Si se recorre todo el grafo y no se encuentra el nodo objetivo, devuelve False

#Función de heurística simple: distancia en línea recta entre dos nodos
def heuristica_dist_linea_recta(nodo, objetivo):
    return distancia_entre_nodos[nodo][objetivo]

grafo = {         #Declaramos nuestro grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
    'A': {'B', 'E'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'F'},
    'D': {'C', 'I'},
    'E': {'A', 'F', 'G', 'H'},
    'F': {'C', 'E'},
    'G': {'E', 'J'},
    'H': {'E', 'I', 'J'},
    'I': {'D', 'H', 'L'},
    'J': {'G', 'H', 'K', 'M'},
    'K': {'J', 'L'},
    'L': {'I', 'K', 'N'},
    'M': {'J', 'N'},
    'N': {'L', 'M'}
}

coordenadas = {         #Declaramos nuestras coordenadas de nuestro grafo en base a la imagen "00.3_Mapa-de-Busqueda_Imagen-Referencia.png".
        'A': (0, 6), 
        'B': (1, 4), 
        'C': (0, 3), 
        'D': (2, 0),
        'E': (2, 5), 
        'F': (2, 2), 
        'G': (5, 6), 
        'H': (4, 3),
        'I': (4, 1), 
        'J': (6, 5), 
        'K': (7, 3), 
        'L': (6, 0),
        'M': (8, 6), 
        'N': (9, 4)
}
    

#Función para calcular la distancia euclidiana entre dos nodos
def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


#Calculamos la distancia entre cada par de nodos y almacenamos el resultado
distancia_entre_nodos = {}
for nodo1 in coordenadas:
    distancia_entre_nodos[nodo1] = {}
    for nodo2 in coordenadas:
        distancia_entre_nodos[nodo1][nodo2] = distancia_euclidiana(coordenadas[nodo1], coordenadas[nodo2])

#Nodo de inicio y nodo objetivo
inicio = 'A'
meta = 'N'

# Llamamos a la función de búsqueda voraz primero el mejor
encontrado, distancia = GBFS(grafo, inicio, meta, heuristica_dist_linea_recta)

#Llamamos a la función de búsqueda voraz primero el mejor
if encontrado:
    print("Se encontró un camino entre", inicio, "y", meta)
    print("Distancia entre", inicio, "y", meta, "es:", distancia)
else:
    print("No se encontró un camino entre", inicio, "y", meta)