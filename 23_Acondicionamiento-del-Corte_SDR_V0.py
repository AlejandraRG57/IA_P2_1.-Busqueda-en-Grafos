#Alejandra Rodriguez Guevara 21310127 6E1

#El "Acondicionamiento del Corte" es un término que se utiliza en el contexto de teoría de grafos y análisis de redes para referirse a un proceso que busca fortalecer 
#o mejorar la conectividad o estructura de un grafo al modificar sus aristas. Este proceso implica agregar o eliminar aristas selectivamente con el objetivo de mejorar 
#ciertas propiedades del grafo, como la conectividad entre sus componentes o la eficiencia de la red.

class Grafo:
    def __init__(self, vertices, aristas):
        self.vertices = vertices  #Almacenamos los vértices del grafo.
        self.aristas = aristas  #Almacenamos las aristas del grafo.
        self.visitado = {v: False for v in vertices}  #Un diccionario para realizar un seguimiento de los vértices visitados durante el recorrido DFS.
        self.componentes_conexos = []  #Lista para almacenar los componentes conexos encontrados.

    def DFS(self, vertice, componente_conexo_actual):
        self.visitado[vertice] = True  #Marcamos el vértice actual como visitado.
        componente_conexo_actual.append(vertice)  #Agregamos el vértice actual al componente conexo actual.
        for vecino in self.aristas[vertice]:  #Iteramos sobre los vecinos del vértice actual.

            if not self.visitado[vecino]: 
                self.DFS(vecino, componente_conexo_actual) #Llamada recursiva a DFS para explorar el vecino y sus vecinos.

    def encontrar_componentes_conexos(self): #Método para encontrar todos los componentes conexos en el grafo.
        for vertice in self.vertices:  #Iteramos sobre todos los vértices del grafo.

            if not self.visitado[vertice]:
                componente_conexo_actual = []  #Inicializamos un nuevo componente conexo vacío.
                self.DFS(vertice, componente_conexo_actual) #Llamamos a DFS para explorar todos los vértices conectados al vértice actual.
                self.componentes_conexos.append(componente_conexo_actual)  #Agregamos el componente conexo encontrado a la lista.

    def imprimir_componentes_conexos(self): #Método para imprimir los componentes conexos encontrados.
        for idx, componente in enumerate(self.componentes_conexos, start=1):  #Iteramos sobre todos los componentes conexos encontrados.
            print(f"Componente Conexo {idx}: {componente}")  #Imprimimos el componente conexo actual junto con su índice.

#Declaramos nuestros vertices y aristas en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
aristas = { 
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'I'],
    'E': ['A', 'F', 'G', 'H'],
    'F': ['C', 'E'],
    'G': ['E', 'J'],
    'H': ['E', 'I', 'J'],
    'I': ['D', 'H', 'L'],
    'J': ['G', 'H', 'K', 'M'],
    'K': ['J', 'L'],
    'L': ['I', 'K', 'N'],
    'M': ['J', 'N'],
    'N': ['L', 'M']
}

grafo = Grafo(vertices, aristas)  #Creamos un objeto Grafo.

grafo.encontrar_componentes_conexos()  #Llamamos al método para encontrar los componentes conexos del grafo.

grafo.imprimir_componentes_conexos()  #Llamamos al método para imprimir los componentes conexos encontrados.