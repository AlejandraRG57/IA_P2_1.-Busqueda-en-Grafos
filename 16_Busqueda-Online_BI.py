#Alejandra Rodriguez Guevara 21310127 6E1

#La búsqueda en línea es un método de búsqueda donde los resultados se van generando y evaluando a medida que avanza el proceso de búsqueda, 
#en lugar de generar todos los posibles resultados de antemano y luego seleccionar entre ellos.

from collections import defaultdict, deque  #Importamos las bibliotecas necesarias.

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)  #Inicializamos un diccionario predeterminado para almacenar las conexiones entre nodos.

    def agregar_conexion(self, origen, destino):
        self.grafo[origen].append(destino)  #Agregamos una conexión entre el nodo origen y el nodo destino.

    def buscar_bfs_online(self, inicio, objetivo, max_intentos):
        intentos = 0  #Inicializamos el contador de intentos en 0.
        
        while intentos < max_intentos:  #Comenzamos un bucle para realizar la búsqueda en línea hasta que se alcance el número máximo de intentos.
            visitados = set()  #Inicializamos un conjunto para almacenar los nodos visitados durante cada búsqueda.
            cola = deque([inicio])  #Inicializamos una cola con el nodo de inicio para realizar la búsqueda en amplitud.
            camino = defaultdict(list)  #Inicializamos un diccionario para almacenar los caminos encontrados hacia cada nodo durante la búsqueda.
            encontrado = False  #Inicializamos una bandera para indicar si se ha encontrado el nodo objetivo durante la búsqueda actual.
            
            while cola:  #Comenzamos un bucle para recorrer el grafo en anchura.
                nodo = cola.popleft()  #Extraemos el primer nodo de la cola.

                if nodo not in visitados:  #Verificamos si el nodo no ha sido visitado anteriormente.
                    visitados.add(nodo)  #Agregamos el nodo a los nodos visitados.

                    if nodo == objetivo:  #Verificamos si el nodo actual es el nodo objetivo.
                        encontrado = True  #Establecemos la bandera de encontrado como True.
                        break  #Salimos del bucle ya que se ha encontrado el nodo objetivo.

                    for vecino in self.grafo[nodo]:  #Iteramos sobre los vecinos del nodo actual.

                        if vecino not in visitados: #Verificamos si el vecino no ha sido visitado.
                            cola.append(vecino)  #Agregamos el vecino a la cola para explorarlo en la siguiente iteración.
                            camino[vecino] = camino[nodo] + [vecino]  #Almacenamos el camino hacia el vecino desde el nodo actual.
            
            if encontrado:  #Verificamos si se encontró el nodo objetivo durante la búsqueda actual.
                return True, camino[objetivo]  #Devolvemos True junto con el camino encontrado hacia el nodo objetivo.
                
            intentos += 1  #Incrementamos el contador de intentos.
        
        return False, None  #Devolvemos False si el nodo objetivo no se encuentra después de alcanzar el número máximo de intentos.

grafo = Grafo()  #Declaramos nuestras conexiones en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
grafo.agregar_conexion('A', 'B')  
grafo.agregar_conexion('A', 'E')
grafo.agregar_conexion('B', 'C')
grafo.agregar_conexion('C', 'F')
grafo.agregar_conexion('C', 'D')
grafo.agregar_conexion('D', 'I')
grafo.agregar_conexion('E', 'F')
grafo.agregar_conexion('E', 'G')
grafo.agregar_conexion('E', 'H')
grafo.agregar_conexion('G', 'J')
grafo.agregar_conexion('H', 'I')
grafo.agregar_conexion('H', 'J')
grafo.agregar_conexion('I', 'L')
grafo.agregar_conexion('J', 'M')
grafo.agregar_conexion('J', 'K')
grafo.agregar_conexion('K', 'L')
grafo.agregar_conexion('L', 'N')
grafo.agregar_conexion('M', 'N')

inicio = 'A'  #Nodo de inicio para la búsqueda.
objetivo = 'N'  #Nodo objetivo que se quiere encontrar.
max_intentos = 1  #Número máximo de intentos para la búsqueda en línea.

encontrado, camino = grafo.buscar_bfs_online(inicio, objetivo, max_intentos)  #Realizamos la búsqueda en línea utilizando el método buscar_bfs_online.

if encontrado:
    print(f"Se encontró un camino desde {inicio} hasta {objetivo}: {camino}")  #Avisamos que si hay un camino entre el inicio y la meta y mostramos el camino encontrado.
else:
    print(f"No se encontró un camino desde {inicio} hasta {objetivo} después de {max_intentos} intentos.")  #Avisamos que no hay un camino entre el inicio y la meta, y por cuantos intentos se busco.