#Alejandra Rodriguez Guevara 21310127 6E1

#La búsqueda de política en grafos es un área importante en el campo de la inteligencia artificial y la teoría de juegos. 
#Consiste en encontrar la mejor política de decisión en un grafo, donde cada nodo representa un estado y cada borde 
#representa una acción que puede llevar de un estado a otro.

class Grafo:
    def __init__(self): #Inicializamos el grafo con un diccionario vacío para ahi poder almacenar los vértices y sus vecinos.
        self.vertices = {}

    def agregar_vertice(self, vertice): #Método para agregar un nuevo vértice al grafo si no existe todavia.
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice_origen, vertice_destino): #Método para agregar una arista entre dos vértices.
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origen].append(vertice_destino)

    def dfs(self, vertice, visitados=None): #Implementamos el algoritmo de búsqueda en profundidad (DFS).
        if visitados is None: #Si no se proporciona un conjunto de vértices visitados, se crea uno vacío.
            visitados = set()
        visitados.add(vertice) #Agregamos el vértice actual a los visitados.
        print(vertice)

        for vecino in self.vertices[vertice]: #Recorremos todos los vecinos del vértice actual.

            if vecino not in visitados: #Si el vecino no ha sido visitado, realizamos una llamada recursiva a DFS.
                self.dfs(vecino, visitados)

    def buscar_politica(self, vertice_inicial): #Método para buscar la política de búsqueda utilizando DFS desde un vértice inicial.
        print("Política de búsqueda DFS:")
        self.dfs(vertice_inicial)

if __name__ == "__main__":
    grafo = Grafo() #Creamos un grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".

    #Agregamos los vértices al grafo.
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_vertice("F")
    grafo.agregar_vertice("G")
    grafo.agregar_vertice("H")
    grafo.agregar_vertice("I")
    grafo.agregar_vertice("J")
    grafo.agregar_vertice("K")
    grafo.agregar_vertice("L")
    grafo.agregar_vertice("M")
    grafo.agregar_vertice("N")

    #Agregamos las aristas al grafo.
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "E")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("C", "F")
    grafo.agregar_arista('C', 'D')
    grafo.agregar_arista('D', 'I')
    grafo.agregar_arista('E', 'F')
    grafo.agregar_arista('E', 'G')
    grafo.agregar_arista('E', 'H')
    grafo.agregar_arista('G', 'J')
    grafo.agregar_arista('H', 'I')
    grafo.agregar_arista('I', 'L')
    grafo.agregar_arista('J', 'M')
    grafo.agregar_arista('J', 'K')
    grafo.agregar_arista('K', 'L')
    grafo.agregar_arista('L', 'N')
    grafo.agregar_arista('M', 'N')

    #Buscamos la política de búsqueda DFS desde el vértice "A".
    grafo.buscar_politica("A")