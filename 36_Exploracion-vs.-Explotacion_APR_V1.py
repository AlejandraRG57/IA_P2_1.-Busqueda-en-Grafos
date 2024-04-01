#Alejandra Rodriguez Guevara 21310127 6E1

#->"Explotación:" La explotación implica elegir las acciones que el agente considera óptimas en función de su conocimiento actual del entorno. 
#Cuando el agente ha acumulado suficiente información sobre el entorno, la explotación se vuelve más relevante, ya que el objetivo principal 
#es maximizar la recompensa a corto plazo seleccionando las acciones que parecen ser las mejores según el conocimiento actual del agente.

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() #Conjunto para almacenar nodos visitados.
    
    print(start) #Procesar el nodo actual.
    visited.add(start) #Marcamos el nodo como visitado.
    
    for neighbor in graph[start]: #Iteramos sobre los nodos adyacentes al nodo actual.
        if neighbor not in visited:
            dfs(graph, neighbor, visited) #Realizamos el DFS en el nodo adyacente.

graph = {            #Declaramos nuestro grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
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

start_node = 'A' #Nodo inicial para comenzar la exploración.

print("Explotación en profundidad desde el nodo inicial", start_node) #Llamamos a la función DFS para explorar el grafo desde el nodo inicial.
dfs(graph, start_node)