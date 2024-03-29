#Alejandra Rodriguez Guevara 21310127 6E1

#"Salto atrás dirigido por conflictos" (Backtracking Directed by Conflicts o CBM en inglés).

#Este algoritmo mejora el algoritmo básico de salto atrás (backtracking) al utilizar heurísticas que seleccionan qué variable asignar en cada paso y en qué orden.
#Aunque no es un término tan común, la idea general es utilizar una estrategia de selección de variables y valores que se base en conflictos anteriores para intentar 
#evitarlos en futuras asignaciones.

#Ningún par de vértices adyacentes comparten el mismo color es la restricción de este código.
class Grafo: #Definimos la clase Grafo.
    
    def __init__(self, vertices, aristas): #Inicializamos los vértices, aristas y el diccionario de colores.
        self.vertices = vertices
        self.aristas = aristas
        self.colores = {}

    def is_consistent(self, vertice, color, coloraciones): #Método para verificar si la asignación de un color a un vértice es consistente con las restricciones.
        for vecino in self.aristas[vertice]:

            if vecino in coloraciones and coloraciones[vecino] == color:
                return False
        return True

    def backtracking_search(self, coloraciones): #Algoritmo de salto atrás dirigido por conflictos para colorear el grafo.
        if len(coloraciones) == len(self.vertices):
            return coloraciones
        vertice = self.select_unassigned_variable(coloraciones)

        for color in self.order_domain_values(vertice, coloraciones):

            if self.is_consistent(vertice, color, coloraciones):
                coloraciones[vertice] = color
                result = self.backtracking_search(coloraciones)

                if result is not None:
                    return result
                del coloraciones[vertice]
        return None

    def select_unassigned_variable(self, coloraciones): #Método para seleccionar un vértice sin asignar.
        for vertice in self.vertices:

            if vertice not in coloraciones:
                return vertice

    def order_domain_values(self, vertice, coloraciones): #Método para ordenar los colores disponibles para un vértice.
        colores_disponibles = set(range(len(self.vertices)))
        for vecino in self.aristas[vertice]:

            if vecino in coloraciones:
                colores_disponibles.discard(coloraciones[vecino])
        return colores_disponibles

    def colorear_grafo(self): #Método para colorear el grafo utilizando el algoritmo de salto atrás dirigido por conflictos.
        coloraciones = self.backtracking_search({})
        if coloraciones is None:
            return "No se encontró una solución"
        else:
            return {vertice: self.nombre_color(color) for vertice, color in coloraciones.items()}

    def nombre_color(self, color): #Método para asignar nombres a los colores.
        nombres = {0: 'Rojo', 1: 'Verde', 2: 'Azul', 3: 'Amarillo', 4: 'Naranja', 5: 'Violeta', 6: 'Blanco'}
        return nombres.get(color, 'Desconocido')

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

resultado = grafo.colorear_grafo() #Coloreamos el grafo e imprimimos el resultado.
print(resultado)