#Alejandra Rodriguez Guevara 21310127 6E1

#La búsqueda local con el algoritmo de mínimos conflictos es una técnica heurística utilizada para resolver problemas de optimización, como el coloreo de grafos. 
#El objetivo de esta técnica es encontrar una solución factible al problema minimizando el número de conflictos entre las restricciones del problema.

#Ningún par de vértices adyacentes comparten el mismo color es la restricción de este código.

import random #Importamos el módulo random para generar números aleatorios.

class Grafo:     #Definimos la clase Grafo.

    def __init__(self, vertices, aristas): #Inicializamos los vértices, aristas y el diccionario de colores.
        self.vertices = vertices
        self.aristas = aristas
        self.colores = {}

    def is_consistent(self, vertice, color, coloraciones): #Método para verificar si la asignación de un color a un vértice es consistente con las restricciones.
        for vecino in self.aristas[vertice]:

            if vecino in coloraciones and coloraciones[vecino] == color:
                return False
        return True

    def num_conflictos(self, vertice, color, coloraciones): #Método para contar el número de conflictos de un vértice con un color dado.
        conflictos = 0
        for vecino in self.aristas[vertice]:

            if vecino in coloraciones and coloraciones[vecino] == color:
                conflictos += 1
        return conflictos

    def minimos_conflictos(self, max_iter=1000): #Algoritmo de búsqueda local con mínimos conflictos para colorear el grafo.
        for vertice in self.vertices: 
            self.colores[vertice] = random.choice(['Rojo', 'Verde', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Blanco']) #Asignamos colores aleatorios a los vértices.

        for _ in range(max_iter): #Iteramos hasta alcanzar el número máximo de iteraciones.
            conflicto_vertices = [(vertice, self.num_conflictos(vertice, self.colores[vertice], self.colores)) for vertice in self.vertices if self.num_conflictos(vertice, self.colores[vertice], self.colores) > 0]

            if not conflicto_vertices: #En caso de no haber vértices en conflicto, se ha encontrado una solución.
                return self.colores

            vertice, _ = random.choice(conflicto_vertices) #Seleccionamos un vértice con conflicto al azar.
            color_actual = self.colores[vertice]
            min_conflictos = float('inf')
            mejor_color = color_actual

            for color in ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Blanco']: #Iteramos sobre los colores posibles para el vértice seleccionado.

                if color != color_actual and self.is_consistent(vertice, color, self.colores): #Si el color es diferente al actual y es consistente con las restricciones, evalúamos el número de conflictos.
                    num_conflictos = self.num_conflictos(vertice, color, self.colores)

                    if num_conflictos < min_conflictos: #Actualizamos el color del vértice si se encuentra uno que minimice el número de conflictos.
                        min_conflictos = num_conflictos
                        mejor_color = color

            self.colores[vertice] = mejor_color

        return "No se encontró una solución" #Si no se encuentra una solución dentro del número máximo de iteraciones, se devuelve un mensaje indicando que no se encontró una solución.

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
grafo = Grafo(vertices, aristas) #Creamos el objeto Grafo.

resultado = grafo.minimos_conflictos() #Coloreamos el grafo utilizando la búsqueda local con mínimos conflictos y mostramos los resultados.
print(resultado)