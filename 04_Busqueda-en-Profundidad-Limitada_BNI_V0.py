#Alejandra Rodriguez Guevara 21310127 6E1
#Búsqueda en Profundidad Limitada, es una variante del algoritmo de búsqueda en profundidad.  

#Establece un límite de la profundidad máxima que puede alcanzar durante la exploración del árbol o grafo.
#Esto se hace para evitar que el algoritmo se pierda en ramas infinitas o muy profundas del árbol de búsqueda.

def DFS_limitado(grafo, inicio, meta, limite_profundidad): #Definimos una función dfs_limitado que toma como entrada el grafo, el nodo de inicio, el nodo meta y el límite de profundidad.
    visitados = set()   #Creamos un conjunto para almacenar los nodos visitados.
    return DFS_recursivo_limitado(grafo, inicio, meta, visitados, limite_profundidad) #Inicializamos un conjunto para almacenar los nodos visitados y llamamos a la función recursiva dfs_recursivo_limitado.

def DFS_recursivo_limitado(grafo, nodo, meta, visitados, limite_profundidad):
    if nodo == meta:
        return [nodo] #Si el nodo actual es igual al meta, devolvemos un camino que solo contiene el nodo actual.
    if limite_profundidad == 0:
        return None #Si alcanzamos el límite de profundidad, retornamos None.
    if nodo not in visitados: #Verificamos si el nodo actual no ha sido visitado.
        visitados.add(nodo) #Añadimos el nodo actual al conjunto de nodos visitados.
        for vecino in grafo[nodo]: #Iteramos sobre los vecinos del nodo actual en el grafo.
            camino = DFS_recursivo_limitado(grafo, vecino, meta, visitados, limite_profundidad - 1) #Llamamos recursivamente a la función con el vecino como nuevo nodo actual y reducimos el límite de profundidad.
            if camino is not None: #Si encontramos un camino válido, lo devolvemos.
                return [nodo] + camino 
    return None #Si no encontramos un camino válido, retornamos None.

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
limite_profundidad = 6 #Definimos un limite de profundidad para la busqueda.

camino = DFS_limitado(grafo, inicio, meta, limite_profundidad) #Buscamos el nodo meta 'N' desde el nodo inicial 'A' con la profundidad maxima especificada.
if camino:
    print("Camino encontrado:", camino) #Avisamos que el nodo fue encontrado y el camino que se tomo.
else:
    print("No se encontró un camino dentro del límite de profundidad.") #Avisamos que no se pudo llegar al nodo pedido con la profundidad maxima dada.