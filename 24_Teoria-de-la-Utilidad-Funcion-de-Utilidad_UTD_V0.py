#Alejandra Rodriguez Guevara 21310127 6E1

#En el contexto de los grafos, la "teoría de la utilidad" puede ser aplicada para asignar "utilidades" a las aristas o a los caminos entre nodos. 
#La utilidad en este contexto podría representar diferentes medidas, como la distancia más corta/larga, el costo maximo/minimo, el tiempo maximo/mínimo 
#o cualquier otra métrica relevante según el problema que se esté abordando.

class Grafo:

    def __init__(self, vertices, aristas): #Inicializamos los vértices y las aristas.
        self.vertices = vertices
        self.aristas = aristas

    def obtener_peso(self, u, v): #Método para obtener el peso de una arista entre dos vértices.
        return self.aristas[u][v]

    def calcular_utilidad_camino(self, camino): #Método para calcular la utilidad de un camino.
        utilidad = 0
        for i in range(len(camino) - 1): #Iteramos sobre los vértices del camino.
            utilidad += self.obtener_peso(camino[i], camino[i+1]) #Sumamos el peso de cada arista.
        return utilidad

    def encontrar_camino_optimo(self, origen, destino): #Método para encontrar el camino óptimo entre dos vértices.
        visitados = set()  #Conjunto de vértices visitados.
        camino_actual = [origen]  #Lista que representa el camino actual.
        caminos = []  #Lista para almacenar todos los caminos posibles.

        def dfs(v): #Función de búsqueda en profundidad para encontrar todos los caminos posibles. 
            if v == destino: #Si se llega al destino, agregar el camino actual a la lista de caminos.
                caminos.append(list(camino_actual))
            else:
                for vecino in self.aristas[v]: #Exploramos los vértices vecinos no visitados.

                    if vecino not in visitados: #Marcamos a el vecino como visitado y lo agregamos al camino actual.
                        visitados.add(vecino)
                        camino_actual.append(vecino)
                        dfs(vecino) #Desmarcamos a el vecino y lo eliminamos del camino actual para probar otros caminos.
                        camino_actual.pop()
                        visitados.remove(vecino)

        dfs(origen) #Llamamos a la función DFS para encontrar todos los caminos posibles.
        utilidades = [(camino, self.calcular_utilidad_camino(camino)) for camino in caminos] #Calculamos la utilidad de cada camino encontrado.
        return max(utilidades, key=lambda x: x[1]) #Devolvemos el camino óptimo con la mayor utilidad.

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
aristas = {            #Declaramos nuestros vertices y aristas en base a la imagen "00.4_Mapa-de-Busqueda_Imagen-Referencia.png" y les asignamos costos por su separacion.
    'A': {'B':3, 'E':3},
    'B': {'A':3, 'C':2},
    'C': {'B':2, 'D':5, 'F':3},
    'D': {'C':5, 'I':3},
    'E': {'A':3, 'F':3, 'G':4, 'H':4},
    'F': {'C':3, 'E':3},
    'G': {'E':4, 'J':2},
    'H': {'E':4, 'I':2, 'J':4},
    'I': {'D':3, 'H':2, 'L':3},
    'J': {'G':2, 'H':4, 'K':3, 'M':3},
    'K': {'J':3, 'L':4},
    'L': {'I':3, 'K':4, 'N':7},
    'M': {'J':3, 'N':3},
    'N': {'L':7, 'M':3}
}

grafo = Grafo(vertices, aristas) #Creamos una instancia del objeto Grafo

origen = 'A'
destino = 'N'
camino_optimo, utilidad_optima = grafo.encontrar_camino_optimo(origen, destino) #Encontramos el camino óptimo y su utilidad

print("El camino óptimo de", origen, "a", destino, "es:", camino_optimo) #Imprimir los resultados.
print("La utilidad óptima es:", utilidad_optima)