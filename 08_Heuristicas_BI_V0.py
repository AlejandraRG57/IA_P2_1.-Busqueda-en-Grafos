#Alejandra Rodriguez Guevara 21310127 6E1
#La función heurística en el contexto de búsqueda informada, es donde estamos interesados en estimar la distancia entre dos nodos en un grafo.

import math #Importamos la libreria math.
def heuristico(nodo_actual, meta):#Definimos la función heurística para el grafo.
    
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
    
    #Obtenemos las coordenadas del nodo actual y del nodo meta.
    x1, y1 = coordenadas[nodo_actual]
    x2, y2 = coordenadas[meta]
    
    #Calculamos la distancia entre las coordenadas.
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #distancia euclidiana.
    #distancia = abs(x2 - x1) + abs(y2 - y1) #distancia Manhattan.
    
    return distancia

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

if __name__ == "__main__":
    nodo_actual = 'A'  #Definimos el nodo actual y el nodo meta.
    meta = 'N'

    valor_h = heuristico(nodo_actual, meta)  #Calculamos la heurística para el nodo actual.
    print("Valor heurístico para el nodo actual:", valor_h)