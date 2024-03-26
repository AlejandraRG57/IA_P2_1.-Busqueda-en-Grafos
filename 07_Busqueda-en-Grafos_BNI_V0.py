#Alejandra Rodriguez Guevara 21310127 6E1
#La búsqueda en grafos consiste en recorrer o explorar un grafo, que es una estructura de datos compuesta por nodos (también llamados vértices) y las conexiones entre ellos (llamadas aristas).
#Hay varios algoritmos de búsqueda en grafos, cada uno con sus propias características y aplicaciones.

#Estos algoritmos se utilizan ampliamente en diversas aplicaciones, como encontrar el camino más corto entre dos nodos, 
#verificar la conectividad de un grafo, encontrar ciclos en un grafo y muchos otros problemas relacionados con grafos.

#El codigo presente es un ejemplo del algoritmo DFS(Depth-First Search -> Busqueda en Profundidad) el cual explicamos mas a profundidad atras.

def buscar_dfs(grafo, inicio, meta):
    def dfs_explorar(act_nodo, acum_camino): #Función de ayuda dfs_explorar explora todos los caminos recursivamente.
        if act_nodo == meta: #Si alcanzamos nuestra meta.
            caminos.append(acum_camino[:])
            return

        if act_nodo not in visitados:#Si el nodo no ha sido visitado, lo agregamos al conjunto de visitados.
            visitados.add(act_nodo)

            for vecino in grafo[act_nodo]: #Iteración sobre los vecinos del nodo actual.
                dfs_explorar(vecino, acum_camino + [vecino])

    visitados = set() #Inicialización de variables.
    caminos = []

    dfs_explorar(inicio, [inicio]) #Llamada inicial a la función dfs_explorar.

    return list(reversed(caminos[0])) if caminos else [] #Retornamos un único camino si existe.

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

camino = buscar_dfs(grafo, 'A', 'N') #Realizamos la búsqueda.
camino.reverse() #Invertimos el camino desde la meta para que esté en el orden correcto.

if camino:
    print("Se encontró un camino entre", 'A', "y", 'N') #Avisamos que si hay un camino entre el inicio y la meta.
    print("Camino encontrado:", camino) #Mostramos el camino tomado.
else:
    print("No se encontró un camino entre", 'A', "y", 'N')#Avisamos que no hay un camino entre el inicio y la meta.