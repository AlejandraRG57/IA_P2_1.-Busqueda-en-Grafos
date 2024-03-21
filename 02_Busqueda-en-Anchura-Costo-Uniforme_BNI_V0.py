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

grafo = {            #Declaramos nuestro grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png" y les damos a todos un peso de 1.
    'A': {'B':1, 'E':1},
    'B': {'A':1, 'C':1},
    'C': {'B':1, 'D':1, 'F':1},
    'D': {'C':1, 'I':1},
    'E': {'A':1, 'F':1, 'G':1, 'H':1},
    'F': {'C':1, 'E':1},
    'G': {'E':1, 'J':1},
    'H': {'E':1, 'I':1, 'J':1},
    'I': {'D':1, 'H':1, 'L':1},
    'J': {'G':1, 'H':1, 'K':1, 'M':1},
    'K': {'J':1, 'L':1},
    'L': {'I':1, 'K':1, 'N':1},
    'M': {'J':1, 'N':1},
    'N': {'L':1, 'M':1}
}

meta_found = UCS(grafo, 'A', 'N') #Iniciamos la búsqueda en grafo desde el nodo 'A' y buscamos el nodo 'N'.
if meta_found:
    print("Costo mínimo desde 'A' hasta 'N' es:", meta_found['N']) #Si se encontro la meta revelamos cual fue el menor coste posible para llegar a dicha meta.
else:
    print("No hay camino desde 'A' hasta 'N' ") #Avisamos si no se pudo llegar al nodo pedido.
