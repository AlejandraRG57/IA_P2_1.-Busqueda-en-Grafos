#Alejandra Rodriguez Guevara 21310127 6E1
#Búsqueda en Profundidad o DFS, por sus siglas en inglés, Depth-First Search.

#DFS se utiliza cuando se desea explorar profundamente en un árbol o grafo, y la longitud del camino no es una consideración importante,
# o cuando se necesita encontrar una solución rápida, aunque no necesariamente la óptima.

def DFS(grafo, inicio, meta):
    explorado = set()  # Conjunto para mantener los nodos visitados
    monton = [inicio]   # Pila para almacenar los nodos a explorar

    while monton:
        nodo = monton.pop()  # Sacamos el último nodo de la pila
        if nodo == meta:
            print(nodo)
            return meta
        if nodo not in explorado:
            explorado.add(nodo)  # Marcamos el nodo como visitado
            print(nodo)
            # Agregamos los nodos vecinos no visitados a la pila
            monton.extend(grafo[nodo] - explorado)
    return None

grafo = {            #Declaramos nuestro grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
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


meta_found = DFS(grafo, 'A', 'N')  # Buscamos el nodo objetivo 'N' desde el nodo inicial 'A'
if meta_found:
    print("¡Nodo 'N' encontrado!") #Avisamos que el nodo fue encontrado.
else:
    print("¡Nodo 'N' no encontrado!") #Avisamos que no se pudo llegar al nodo pedido.
