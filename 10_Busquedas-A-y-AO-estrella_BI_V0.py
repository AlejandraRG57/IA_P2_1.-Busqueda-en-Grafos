#Alejandra Rodriguez Guevara 21310127 6E1

#La búsqueda A* es una técnica de búsqueda informada que utiliza tanto el costo real desde el nodo inicial hasta el nodo actual (denotado como g),
#como una estimación heurística del costo desde el nodo actual hasta el nodo objetivo (denotado como h), 
#para determinar qué nodo explorar a continuación. La idea es minimizar la suma de estos dos valores, es decir, f = g + h.

import heapq

def A_estrella(grafo, inicio, meta, heuristica):
    frontera = [(0, inicio)]  #Inicializamos la frontera con el nodo inicial y su costo actual.
    heapq.heapify(frontera)  #Convertimos la lista en una cola de prioridad.
    visitados = set()  #Inicializamos un conjunto de nodos visitados.
    padres = {}  #Diccionario para rastrear los padres de los nodos.
    costos = {nodo: float('inf') for nodo in grafo}  #Inicializamos los costos con infinito para todos los nodos.
    costos[inicio] = 0  #El costo desde el nodo inicial hasta él mismo es 0.
    
    while frontera:
        _, nodo_actual = heapq.heappop(frontera)  #Extraemos el nodo con menor costo de la frontera.
        
        if nodo_actual == meta:  #Si el nodo actual es el nodo objetivo, se ha encontrado el camino.
            camino = reconstruir_camino(padres, meta)
            return camino
        
        visitados.add(nodo_actual)  #Agregamos el nodo actual a los nodos visitados.
        
        for vecino in grafo[nodo_actual]:
            costo_nuevo = costos[nodo_actual] + grafo[nodo_actual][vecino]  #Calculamos el nuevo costo desde el nodo inicial al vecino.
            
            if vecino not in visitados and costo_nuevo < costos[vecino]:
                costos[vecino] = costo_nuevo
                heapq.heappush(frontera, (costo_nuevo + heuristica(vecino, meta), vecino))  #Agregamos el vecino a la frontera con su costo estimado total.
                padres[vecino] = nodo_actual  #Actualizamos el padre del vecino.
    
    return None  #Si se recorre todo el grafo y no se encuentra el nodo objetivo, devuelve None.

def reconstruir_camino(padres, meta): #Sirve pra guardar el camino encontrado en la variable camino.
    camino = [meta]
    while meta in padres:
        meta = padres[meta]
        camino.append(meta)
    return list(reversed(camino))

grafo = {            #Declaramos nuestro grafo en base a la imagen "00.4_Mapa-de-Busqueda_Imagen-Referencia.png" y les asugnamos costos por su separacion.
    'A': {'B':3, 'E':3},
    'B': {'A':3, 'C':2},
    'C': {'B':2, 'D':5, 'F':3},
    'D': {'C':5, 'I':3},
    'E': {'A':3, 'F':3, 'G':4, 'H':4},
    'F': {'C':3, 'E':3},
    'G': {'E':4, 'J':2},
    'H': {'E':4, 'I':2, 'J':4},
    'I': {'D':3, 'H':2, 'L':3},
    'J': {'G':2, 'H':4, 'K':3, 'M':3},
    'K': {'J':3, 'L':4},
    'L': {'I':3, 'K':4, 'N':7},
    'M': {'J':3, 'N':3},
    'N': {'L':7, 'M':3}
}

def heuristica_dist_linea_recta(nodo, objetivo): 
    return abs(ord(objetivo) - ord(nodo))  #Distancia en línea recta entre las coordenadas de los nodos.

inicio = 'A' #Declaramos un nodo de inicio.
meta = 'N' #Declaramos un nodo de meta.

camino = A_estrella(grafo, inicio, meta, heuristica_dist_linea_recta) #Llamamos a la función de búsqueda A*.

if camino:
    print("Se encontró un camino entre", inicio, "y", meta) #Avisamos que si hay un camino entre el inicio y la meta.
    print("Camino encontrado:", camino) #Mostramos el camino encontrado.
else:
    print("No se encontró un camino entre", inicio, "y", meta) #Avisamos que no hay un camino entre el inicio y la meta.