#Alejandra Rodriguez Guevara 21310127 6E1

#->"Exploración:" Esta estrategia implica probar nuevas acciones con el objetivo de descubrir información sobre el entorno y mejorar 
#el conocimiento del agente sobre las posibles recompensas asociadas con diferentes acciones. La exploración es crucial al principio
#del proceso de aprendizaje, cuando el agente tiene un conocimiento limitado sobre el entorno. Sin exploración, el agente podría 
#quedarse estancado en una política subóptima y nunca descubrir mejores acciones.

from collections import deque

def bfs(graph, start):
    visited = set() #Conjunto para almacenar nodos visitados.
    queue = deque([start]) #Cola para mantener los nodos que se deben visitar.
    visited.add(start) #Marcamos el nodo inicial como visitado.
    
    while queue:
        node = queue.popleft() #Tomamos el primer nodo de la cola.
        print(node) #Imprimimos el nodo.
        
        for neighbor in graph[node]: #Iteramos sobre los nodos adyacentes al nodo actual.
            if neighbor not in visited:
                visited.add(neighbor) #Marcamos el nodo como visitado.
                queue.append(neighbor) #Agregamos el nodo a la cola para visitarlo posteriormente.


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

print("Exploración desde el nodo inicial", start_node) #Llamamos a la función BFS para explorar el grafo desde el nodo inicial.
bfs(graph, start_node)