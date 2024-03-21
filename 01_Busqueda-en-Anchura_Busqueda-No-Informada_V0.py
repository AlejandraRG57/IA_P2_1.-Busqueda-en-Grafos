#Alejandra Rodriguez Guevara 21310127 6E1
#Búsqueda en anchura o BFS por sus siglas en inglés, Breadth-First Search.

#Es un algoritmo utilizado para recorrer o buscar en estructuras de datos como árboles o grafos. 
#La característica principal de BFS es que explora todos los nodos vecinos de un nodo antes de pasar a los nodos vecinos de sus vecinos.

from collections import deque

def BFS(grafo, inicio, meta):
    fila = deque([inicio])  #Cola para almacenar los nodos a visitar.
    explorado = set()  #Conjunto para mantener los nodos explorado.

    while fila: 
        nodo = fila.popleft()  #Sacamos el primer nodo de la cola.
        if nodo == meta:  #Verificamos si encontramos el nodo deseado.
            return meta #Devolvemos el nodo meta.
        if nodo not in explorado: #Entramos a el if si el nodo elegido no ha sido viditado.
            print(nodo)  #Imprimimos el nodo.
            explorado.add(nodo)  #Marcamos el nodo como visitado.
            fila.extend(grafo[nodo] - explorado)#Agregamos los nodos vecinos no visitados a la cola.
    return None

grafo = {            #Declaramos nuestro grafo en base a la imagen "00.1_Mapa-de-Busqueda_Imagen-Referencia.png".
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

meta_found = BFS(grafo, 'A', 'N')  #Iniciamos la búsqueda en grafo desde el nodo 'A' y buscamos el nodo 'N'.
if meta_found:
    print("El nodo 'N' ha sido encontrado.") #Avisamos si el nodo fue encontrado.
else:
    print("El nodo 'N' no ha sido encontrado.") #Avisamos si no se pudo llegar al nodo pedido.
