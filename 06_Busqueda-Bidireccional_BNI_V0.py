#Alejandra Rodriguez Guevara 21310127 6E1
#Es un tipo de algoritmo de búsqueda que opera desde dos puntos al mismo tiempo, buscando una solución en ambos sentidos y convergiendo hacia el medio. 

#El algoritmo de Búsqueda Bidireccional sigue una estrategia en la que se inicia la búsqueda desde el estado inicial y el estado meta simultáneamente. 
#Luego, explora de manera alternativa los sucesores de cada estado en cada extremo, hasta que las dos búsquedas se encuentran en algún punto intermedio.

def buscar_bidireccional(grafo, inicio, meta):
    frontera_inicio = [frozenset([inicio])] #Inicializamos la frontera desde el inicio con el nodo inicial.
    frontera_meta = [frozenset([meta])] #Inicializamos la frontera desde la meta con el nodo meta.

    visitados_inicio = set() #Conjunto de nodos visitados desde el inicio.
    visitados_meta = set() #Conjunto de nodos visitados desde la meta.

    padres_inicio = {frontera_inicio[0]: None} #Diccionario para rastrear el camino desde el inicio.
    padres_meta = {frontera_meta[0]: None} #Diccionario para rastrear el camino desde la meta.

    while frontera_inicio and frontera_meta: #Bucle principal de búsqueda bidireccional.
        nodo_actual_inicio = frontera_inicio.pop(0) #Toma el primer nodo de la frontera desde el inicio.

        if nodo_actual_inicio in frontera_meta or nodo_actual_inicio in visitados_meta:#Si el nodo actual desde el inicio está en la frontera desde la meta o ha sido visitado desde la meta.
            return reconstruir_camino(nodo_actual_inicio, padres_inicio, padres_meta) #Devuelve el camino encontrado.

        visitados_inicio.add(nodo_actual_inicio) #Agregamos el nodo actual desde el inicio a los visitados.

        for vecino in grafo[list(nodo_actual_inicio)[0]]: #Para cada vecino del nodo actual desde el inicio.
            if vecino not in visitados_inicio and vecino not in visitados_meta:
                frontera_inicio.append(frozenset([vecino])) #Agregamos el vecino a la frontera desde el inicio.
                padres_inicio[frozenset([vecino])] = list(nodo_actual_inicio)[0] #Actualizamos el padre del vecino.

        nodo_actual_meta = frontera_meta.pop(0) #Tomamos el primer nodo de la frontera desde la meta.

        if nodo_actual_meta in visitados_inicio or list(nodo_actual_meta)[0] in visitados_inicio: #Si el nodo actual desde la meta está en los visitados desde el inicio o en la frontera desde el inicio.
            return reconstruir_camino(nodo_actual_meta, padres_inicio, padres_meta) #Devolvemos el camino encontrado.

        visitados_meta.add(nodo_actual_meta) #Agregamos el nodo actual desde la meta a los visitados.

        for vecino in grafo[list(nodo_actual_meta)[0]]: #Para cada vecino del nodo actual desde la meta.
            if vecino not in visitados_meta:
                frontera_meta.append(frozenset([vecino])) #Agregamos el vecino a la frontera desde la meta.
                padres_meta[frozenset([vecino])] = list(nodo_actual_meta)[0] #Actualizamos el padre del vecino.

    return False  #No se encontró un camino entre el inicio y la meta.

def reconstruir_camino(nodo, padres_inicio, padres_meta):
    camino_inicio = [] #Inicializamos una lista para almacenar el camino desde el inicio.
    camino_meta = [] #Inicializamos una lista para almacenar el camino desde la meta.

    while nodo in padres_inicio: #Mientras haya nodos en los padres desde el inicio.
        camino_inicio.append(list(nodo)[0]) #Agregamos el nodo al camino desde el inicio.
        nodo = padres_inicio[nodo] #Actualizamos el nodo al padre del nodo actual.

    while nodo in padres_meta: #Mientras haya nodos en los padres desde la meta.
        camino_meta.append(list(nodo)[0]) #Agregamos el nodo al camino desde la meta.
        nodo = padres_meta[nodo] #Actualizamos el nodo al padre del nodo actual.

    camino_meta.reverse() #Invertimos el camino desde la meta para que esté en el orden correcto.
    camino = camino_inicio + camino_meta #Combinamos los caminos desde el inicio y desde la meta.

    return camino #Devolvemos el camino completo.

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

inicio = 'A' #Declaramos un nodo de inicio.
meta = 'N' #Declaramos un nodo de meta.

camino = buscar_bidireccional(grafo, inicio, meta) #Buscamos el camino entre el inicio y la meta

if camino:
    print("Se encontró un camino entre", inicio, "y", meta) #Avisamos que si hay un camino entre el inicio y la meta.
    print("Punto medio encontrado:", camino) #Mostramos el punto medio entre ambos caminos.
else:
    print("No se encontró un camino entre", inicio, "y", meta) #Avisamos que no hay un camino entre el inicio y la meta.