#Alejandra Rodriguez Guevara 21310127 6E1

#La comprobación hacia adelante, también conocida como propagación de restricciones, es una técnica utilizada en problemas de satisfacción de restricciones
#para reducir el espacio de búsqueda y mejorar la eficiencia de los algoritmos de búsqueda. En el contexto de grafos y problemas de coloreo de grafos, 
#la comprobación hacia adelante puede ser utilizada para reducir el dominio de los colores disponibles para los vértices basándose en las restricciones impuestas por los vecinos.

#La restricción en este código es que ningún par de vértices adyacentes tiene que tener el mismo color.
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices  #Almacenamos los vértices del grafo.
        self.vecinos = {v: set() for v in vertices}  #Inicializamos el diccionario de vecinos para cada vértice.

    def agregar_arista(self, u, v):
        self.vecinos[u].add(v)  #Agregamos v a los vecinos de u.
        self.vecinos[v].add(u)  #Agregamos u a los vecinos de v.

def comprobacion_hacia_adelante(grafo, vertice, colores_disponibles, asignaciones):
    dominio_reducido = False
    
    for vecino in grafo.vecinos[vertice]: #Comprobamos si hay colores asignados a los vecinos y reduce el dominio de los colores disponibles.

        if vecino in asignaciones:
            color_vecino = asignaciones[vecino]

            if color_vecino in colores_disponibles:
                colores_disponibles.remove(color_vecino)
                dominio_reducido = True

    return dominio_reducido

def colorear_grafo(grafo, colores_disponibles):
    asignaciones = {}  #Diccionario para almacenar las asignaciones de colores a los vértices.
    
    for vertice in grafo.vertices: #Iteramos sobre cada vértice del grafo para asignarle un color.

        if vertice not in asignaciones:
            dominio_reducido = comprobacion_hacia_adelante(grafo, vertice, colores_disponibles, asignaciones) #Realizamos la comprobación hacia adelante para reducir el dominio de los colores disponibles.

            if not colores_disponibles:
                return None  #Regresamos none en caso de no ser posible colorear el grafo con los colores proporcionados.
            color = colores_disponibles[0]  #Tomamos el primer color disponible.
            asignaciones[vertice] = color  #Asignamos el color al vértice.
            
    return asignaciones

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'] #Declaramos nuestros vertices y aristas en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
aristas = [('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'I'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('G', 'J'), ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'M'), ('J', 'K'), ('K', 'L'), ('L', 'N'), ('M', 'N')]

grafo = Grafo(vertices) #Creamos el grafo y añadimos las aristas.
for u, v in aristas:
    grafo.agregar_arista(u, v)

colores_disponibles = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Morado', 'Rosa', 'Cyan', 'Cafe', 'Gris'] #Definimos los colores disponibles.

resultado_coloreo = colorear_grafo(grafo, colores_disponibles) #Intentamos colorear el grafo y almacenar el resultado.

if resultado_coloreo: #Verificamos si el grafo se puede colorear.
    print("El grafo puede ser coloreado de la siguiente manera:")  #Avisamos que si se pudo colorear el grafo.
    for vertice, color in sorted(resultado_coloreo.items()):
        print(f"{vertice}: {color}") #Mostramos cada vértice con su respectivo color.
else:
    print("No es posible colorear el grafo con los colores proporcionados.") #Avisamos que no se pudo colorear el grafo con el metodo utilizado.