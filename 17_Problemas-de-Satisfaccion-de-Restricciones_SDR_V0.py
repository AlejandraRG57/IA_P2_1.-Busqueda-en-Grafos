#Alejandra Rodriguez Guevara 21310127 6E1

#Los Problemas de Satisfacción de Restricciones (CSP, por sus siglas en inglés) en grafos son una clase de problemas en la que se busca asignar valores a un conjunto de variables, 
#sujetas a ciertas restricciones, de modo que se satisfagan todas las restricciones. 
#En el contexto de los grafos, las variables pueden representar nodos del grafo y los valores asignados a estas variables pueden representar características, 
#colores, asignaciones, etc.


#Este es un ejemplo de un Problema de Satisfaccion de Restricciones usando el  metodo Búsqueda de Vuelta Atrás, en el siguiente capitulo lo explicare mas a fondo.
#La restricción en este codigo es que ningún par de vértices adyacentes tiene que tener el mismo color.
class Grafo: 
    def __init__(self, vertices): #Método de inicialización que crea un grafo con los vértices dados.
        self.vertices = vertices  #Almacenamos los vértices del grafo.
        self.vecinos = {v: set() for v in vertices}  #Inicializamos el diccionario de vecinos para cada vértice.

    def agregar_arista(self, u, v): #Método para agregar una arista entre dos vértices.
        self.vecinos[u].add(v)  #Agregamos v a los vecinos de u.
        self.vecinos[v].add(u)  #Agregamos u a los vecinos de v.


def colorear_grafo(grafo, colores): #Función para colorear el grafo utilizando el algoritmo de búsqueda con retroceso.
    solucion = {}  #Diccionario para almacenar la solución del coloreo.

    if colorear_vertice(grafo, list(grafo.vertices)[0], colores, solucion):     #Llamamos a la función recursiva para colorear el primer vértice del grafo.
        return solucion  # Devuelve la solución si es posible colorear el grafo.
    return None  # Devuelve None si no es posible colorear el grafo.

def colorear_vertice(grafo, vertice, colores, solucion): #Función recursiva para colorear un vértice y sus vecinos.
    
    if vertice in solucion: #Verificamos si el vértice ya está coloreado.
        return True  #Devolvemos True si el vértice ya está coloreado.

    for color in colores: #Iteramos sobre todos los colores disponibles.

        if all(color != solucion.get(vecino) for vecino in grafo.vecinos[vertice]): #Verificamos si ningún vecino del vértice actual tiene el mismo color.
            solucion[vertice] = color  #Asignamos el color al vértice actual.
            
            if all(colorear_vertice(grafo, vecino, colores, solucion) for vecino in grafo.vecinos[vertice]): #Llamamos recursivamente para colorear los vecinos del vértice actual.
                return True  #Devolvemos True si se pudo colorear el grafo.
            solucion.pop(vertice)  #Eliminamos el color del vértice actual si no se pudo colorear.
    return False  #Devolvemos False si no se pudo colorear el grafo.

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'] #Declaramos nuestros vertices y aristas en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
aristas = [('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'I'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('G', 'J'), ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'M'), ('J', 'K'), ('K', 'L'), ('L', 'N'), ('M', 'N')]

#Creamos el grafo y añadimos las aristas.
grafo = Grafo(vertices)
for u, v in aristas:
    grafo.agregar_arista(u, v)

colores_disponibles = ['Rojo', 'Verde', 'Azul'] #Definimos los colores disponibles.

resultado_coloreo = colorear_grafo(grafo, colores_disponibles) #Intentamos colorear el grafo y almacena el resultado.

if resultado_coloreo: #Verificamos si el grafo se puede colorear y mostramos el resultado.
    print("El grafo puede ser coloreado de la siguiente manera:") #Avisamos que si se pudo colorear el grafo.
    for vertice, color in sorted(resultado_coloreo.items()):
        print(f"{vertice}: {color}")  #Mostramos cada vértice con su respectivo color.
else:
    print("No es posible colorear el grafo con los colores proporcionados.")  #Avisamos que no se pudo colorear el grafo.