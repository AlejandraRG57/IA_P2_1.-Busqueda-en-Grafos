#Alejandra Rodriguez Guevara 21310127 6E1
#La Búsqueda en Profundidad Iterativa es una técnica que combina la búsqueda en profundidad con la búsqueda en anchura. 

#En lugar de establecer un límite de profundidad estático como en la búsqueda en profundidad limitada, 
#este incrementa progresivamente el límite de profundidad con cada iteración hasta encontrar la solución. 
#Esto permite realizar una búsqueda profunda sin el riesgo de quedarse atrapado en ramas infinitas o muy profundas del árbol de búsqueda.

def BPI(grafo, inicio, meta):
    profundidad_maxima = 0 #Inicializamos la profundidad máxima en 0.
    while True: #Declaramos un bucle infinito hasta encontrar una solución.
        resultado = dfs_limitado_iterativo(grafo, inicio, meta, profundidad_maxima) #Realizamos una búsqueda en profundidad limitada con la profundidad máxima actual.
        if resultado is not None: #Si se encuentra un camino, devolvemos el resultado.
            return resultado
        profundidad_maxima += 1 #Incrementamos la profundidad máxima para la próxima iteración

def dfs_limitado_iterativo(grafo, inicio, meta, profundidad_maxima): #Función para realizar una Búsqueda en Profundidad con un límite de profundidad recibido.
    visitados = set() #Conjunto para mantener los nodos visitados.
    return dfs_recursivo_limitado_iterativo(grafo, inicio, meta, visitados, profundidad_maxima) #Llama a la función recursiva que realiza la Búsqueda en Profundidad limitada pero con profund max variable por cada iteracion.

def dfs_recursivo_limitado_iterativo(grafo, nodo, meta, visitados, profundidad_maxima): #Función recursiva que realiza la Búsqueda en Profundidad limitada con la profundidad maxima variable.
    if nodo == meta: #Si el nodo actual es la meta, devuelve el camino hasta este nodo.
        return [nodo]
    if profundidad_maxima == 0: #Si se alcanza el límite de profundidad, devuelve None.
        return None
    if nodo not in visitados: #Si el nodo no ha sido visitado, marca el nodo como visitado.
        visitados.add(nodo)
        for vecino in grafo[nodo]: #Explora los vecinos del nodo actual.
            camino = dfs_recursivo_limitado_iterativo(grafo, vecino, meta, visitados, profundidad_maxima - 1) #Realiza una llamada recursiva con profundidad máxima reducida.
            if camino is not None: #Si se encuentra un camino, devuelve el camino encontrado.
                return [nodo] + camino
    return None #Si no se encuentra ni solo un camino, devuelve None.


grafo = {           #Declaramos nuestro grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
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

camino = BPI(grafo, inicio, meta) #Realiza la Búsqueda en Profundidad Iterativa para encontrar el camino desde el nodo inicial a la meta.
if camino:
    print("Camino encontrado:", camino) #Avisamos que el nodo fue encontrado y el camino que se tomo.
else:
    print("No se encontró un camino.") #Avisamos que no se pudo llegar al nodo pedido.