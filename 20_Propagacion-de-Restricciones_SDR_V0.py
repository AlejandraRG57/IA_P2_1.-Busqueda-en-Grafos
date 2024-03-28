#Alejandra Rodriguez Guevara 21310127 6E1

#La propagación de restricciones en grafos es una técnica que permite tomar decisiones informadas sobre qué colores pueden asignarse a los vértices, 
#basándose en las restricciones impuestas por la estructura del grafo y los colores ya asignados a los vértices adyacentes. 
#Esto facilita la búsqueda de una solución válida para el problema de coloreo del grafo.

#Ningún par de vértices adyacentes comparten el mismo color es la restricción de este código.
class Grafo:
    def __init__(self, vertices): #Constructor de la clase Grafo que inicializa los vértices y los vecinos de cada vértice.
        self.vertices = vertices  #Almacenamos los vértices del grafo.
        self.vecinos = {v: set() for v in vertices}  #Inicializamos el diccionario de vecinos para cada vértice.

    def agregar_arista(self, u, v): #Método para agregar una arista entre dos vértices.
        self.vecinos[u].add(v)  #Agregamos v a los vecinos de u.
        self.vecinos[v].add(u)  #Agregamos u a los vecinos de v.

def propagacion_restricciones(grafo, vertice, colores_disponibles, asignaciones): #Función para propagar restricciones de coloreo para un vértice dado.

    if vertice not in asignaciones:  #Verificamos si el vértice no ha sido asignado todavía.
        dominio_reducido = False  #Inicializamos el indicador de reducción de dominio a False.
        vecinos_coloreados = {asignaciones[v] for v in grafo.vecinos[vertice] if v in asignaciones}  #Obtenemos los colores de los vecinos ya coloreados.
        
        if vecinos_coloreados:  #Verificamos si hay vecinos coloreados.
            colores_disponibles_copy = colores_disponibles.copy()  #Realizamos una copia de la lista de colores disponibles.

            for color in colores_disponibles_copy:  #Iteramos sobre la copia de la lista de colores.

                if color in vecinos_coloreados:  #Verificamos si el color está presente en los vecinos coloreados.
                    colores_disponibles.remove(color)  #Eliminamos el color del dominio del vértice.
                    dominio_reducido = True  #Cambiamos el indicador de reducción de dominio a True.
        
        return dominio_reducido  #Devolvemos el indicador de reducción de dominio.
    return False  #Devolvemos False si el vértice ya ha sido asignado.

def colorear_grafo(grafo, colores_disponibles): #Función para colorear el grafo utilizando propagación de restricciones.
    asignaciones = {}  #Diccionario para almacenar las asignaciones de colores a los vértices.
    
    for vertice in grafo.vertices:  #Iteramos sobre todos los vértices del grafo.

        if vertice not in asignaciones:  #Verificamos si el vértice no ha sido asignado todavía.
            dominio_reducido = propagacion_restricciones(grafo, vertice, colores_disponibles, asignaciones)  #Realizamos la propagación de restricciones para el vértice.

            if not colores_disponibles:  #Verificamos si no quedan colores disponibles después de la propagación de restricciones.
                return None  #Devolvemos None si no es posible colorear el grafo con los colores proporcionados.
            color = colores_disponibles[0]  #Tomamos el primer color disponible después de la propagación de restricciones.
            asignaciones[vertice] = color  #Asignamos el color al vértice actual.
            
    if len(asignaciones) == len(grafo.vertices):  #Verificamos si todos los vértices están coloreados.
        return asignaciones  #Devolvemos las asignaciones si es posible colorear el grafo.
    else:
        return None  #Devolvemos None si no es posible colorear el grafo con los colores proporcionados.

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'] #Declaramos nuestros vertices y aristas en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
aristas = [('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'I'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('G', 'J'), ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'M'), ('J', 'K'), ('K', 'L'), ('L', 'N'), ('M', 'N')]

colores_disponibles = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Morado', 'Rosa', 'Cyan', 'Cafe', 'Gris'] #Definimos los colores disponibles.

grafo = Grafo(vertices) #Creamos el grafo y añadimos las aristas.
for u, v in aristas:
    grafo.agregar_arista(u, v)

# Coloreo del grafo utilizando la función colorear_grafo.
resultado_coloreo = colorear_grafo(grafo, colores_disponibles)

if resultado_coloreo: #Verificamos si el grafo se puede colorear.
    print("El grafo puede ser coloreado de la siguiente manera:")  #Avisamos que si se pudo colorear el grafo.
    for vertice, color in sorted(resultado_coloreo.items()):
        print(f"{vertice}: {color}") #Mostramos cada vértice con su respectivo color.
else:
    print("No es posible colorear el grafo con los colores proporcionados.") #Avisamos que no se pudo colorear el grafo con el metodo utilizado.