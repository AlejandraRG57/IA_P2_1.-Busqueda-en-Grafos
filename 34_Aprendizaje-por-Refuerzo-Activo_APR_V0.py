#Alejandra Rodriguez Guevara 21310127 6E1

#El aprendizaje por refuerzo activo implica que un agente interactúe con un entorno y tome decisiones con el objetivo de maximizar su recompensa a largo plazo. 
#En el contexto de grafos, esto implica que un agente debe tomar decisiones sobre qué nodos visitar o qué aristas recorrer con el objetivo de maximizar alguna 
#medida de utilidad o recompensa.

import networkx as nx  #Importamos las librerias necesarias.
import random

def calculate_reward(G, node): #Función para calcular la recompensa de visitar un nodo en el grafo.
    return len(list(G.neighbors(node))) #La recompensa es la cantidad de vecinos del nodo.

def select_action(G, current_node): #Algoritmo de selección de acciónbasado en aprendizaje por refuerzo activo.
    neighbors = list(G.neighbors(current_node)) #Seleccionamos un vecino aleatorio como acción.
    return random.choice(neighbors) if neighbors else None

def active_reinforcement_learning(G, start_node, num_steps): #Aprendizaje por refuerzo activo para encontrar un camino en el grafo.
    current_node = start_node
    path = [current_node]

    for _ in range(num_steps):
        action = select_action(G, current_node)  #Seleccionamos la acción.

        if action is None:
            break #Si no hay vecinos disponibles, terminamos el aprendizaje.
        reward = calculate_reward(G, action) #Calculamos la recompensa.
        current_node = action #Nos movemos al siguiente nodo.
        path.append(current_node)
    return path

G = nx.Graph() #Creamos un grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
G.add_edges_from([('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'I'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('G', 'J'), ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'M'), ('J', 'K'), ('K', 'L'), ('L', 'N'), ('M', 'N')])

#Parámetros de aprendizaje
start_node = 'A' #Nodo inicial.
num_steps = 7 #Número máximo de pasos permitidos en el camino.
path = active_reinforcement_learning(G, start_node, num_steps) #Realizamos el aprendizaje por refuerzo activo para encontrar un camino en el grafo.

if path: #Imprimimos el camino encontrado.
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se pudo encontrar un camino válido.")

#Este codigo utiliza el aprendizaje por refuerzo activo al permitir que un agente tome acciones en un grafo y reciba recompensas basadas en dichas acciones.