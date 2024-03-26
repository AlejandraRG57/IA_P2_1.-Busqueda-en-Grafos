#Alejandra Rodriguez Guevara 21310127 6E1
#Búsqueda en Anchura de Costo Uniforme o UCS, por sus siglas en inglés, Uniform Cost Search.

#Es una variante del BFS que se utiliza para encontrar el camino de costo mínimo entre un nodo de inicio y un nodo objetivo en un grafo ponderado.
#UCS tiene en cuenta los costos asociados a cada borde y elige el camino de menor costo en lugar de simplemente expandir nodos en el orden en que se descubren.

import heapq

def UCS(grafo, inicio, meta): #Definimos una función llamada UCS que realiza la búsqueda del UCS en un grafo dado, comenzando desde un nodo inicio y buscando un nodo meta.
    fila = [(0, inicio)]  #Cola de prioridad para nodos a expandir, (costo acumulado, nodo).
    explorado = set()  #Conjunto para mantener nodos explorados.
    costo_acumulado = {inicio: 0}  #Diccionario para mantener el costo acumulado mínimo conocido hasta el momento para cada nodo.

    while fila: #Comenzamos un bucle while que se ejecutará mientras la cola de prioridad "fila" no esté vacía.
        costo_actual, nodo_actual = heapq.heappop(fila)  #Extraemos nodo con menor costo acumulado.
        if nodo_actual == meta: #Comprobamos si el nodo actual es el nodo de destino deseado.
            return costo_acumulado  #Devolvemos los costos acumulados mínimos conocidos hasta el momento.

        if nodo_actual not in explorado: #Comprobamos si el nodo actual no ha sido explorado previamente.
            explorado.add(nodo_actual)  #Marcamos el nodo como explorado.

            # Exploramos nodos vecinos
            for vecino, precio in grafo[nodo_actual].items(): 
                nuevo_costo = costo_actual + precio #Calculamos el nuevo costo acumulado sumando el costo acumulado actual y el precio del arco desde el nodo actual hasta el vecino.
                if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]: #Verificamos si el vecino no está en costo_acumulado o si el nuevo costo acumulado es menor que el costo acumulado anteriormente conocido para el vecino.
                    costo_acumulado[vecino] = nuevo_costo #Actualizamos el costo acumulado mínimo conocido para el vecino con el nuevo costo acumulado.
                    heapq.heappush(fila, (nuevo_costo, vecino))  #Agregamos nodo vecino a la cola de prioridad con su nuevo costo acumulado.

    return None #No se encontró un camino desde el nodo de inicio hasta el nodo objetivo.

grafo = {            #Declaramos nuestro grafo en base a la imagen "00.4_Mapa-de-Busqueda_Imagen-Referencia.png" y les asignamos costos por su separacion.
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

meta_found = UCS(grafo, 'A', 'N') #Iniciamos la búsqueda en grafo desde el nodo 'A' y buscamos el nodo 'N'.
if meta_found:
    print("Costo mínimo desde 'A' hasta 'N' es:", meta_found['N']) #Si se encontro la meta revelamos cual fue el menor coste posible para llegar a dicha meta.
else:
    print("No hay camino desde 'A' hasta 'N' ") #Avisamos si no se pudo llegar al nodo pedido.
