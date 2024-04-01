#Alejandra Rodriguez Guevara 21310127 6E1

#El aprendizaje por refuerzo pasivo es un enfoque en el que un agente aprende a través de la observación de los resultados de sus acciones, 
#sin recibir explícitamente retroalimentación sobre la calidad de sus acciones. En el contexto de grafos, el aprendizaje por refuerzo pasivo 
#puede aplicarse para aprender a navegar por un grafo de manera óptima.

import networkx as nx #Importamos las librerias necesarias.
import random

def calculate_reward(G, node): #Función para calcular el valor de recompensa de un nodo en un grafo.
    return len(G[node]) #Usamos el grado del nodo como recompensa.

def passive_reinforcement_learning(G, alpha, num_iterations): #Función para realizar un paso de aprendizaje por refuerzo pasivo.
    node_values = {node: 0 for node in G.nodes()} #Inicializamos la estimación de valor para cada nodo en el grafo.

    for _ in range(num_iterations): #Realizamos iteraciones de aprendizaje.
        current_node = random.choice(list(G.nodes())) #Seleccionamos un nodo aleatorio en el grafo.
        reward = calculate_reward(G, current_node) #Calculamos la recompensa para el nodo actual
        node_values[current_node] += alpha * (reward - node_values[current_node]) #Actualizamos la estimación de valor del nodo actual utilizando la regla de actualización de valor.
    return node_values

G = nx.Graph() #Creamos un grafo en base a la imagen "00.2_Mapa-de-Busqueda_Imagen-Referencia.png".
G.add_edges_from([('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'I'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('G', 'J'), ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'M'), ('J', 'K'), ('K', 'L'), ('L', 'N'), ('M', 'N')])

#Parámetros de aprendizaje.
alpha = 0.1  #Tasa de aprendizaje.
num_iterations = 1000  #Número de iteraciones de aprendizaje.

node_values = passive_reinforcement_learning(G, alpha, num_iterations) #Realizamos un aprendizaje por refuerzo pasivo.

print("Valores estimados para cada nodo:") #Imprimimos los valores estimados para cada nodo.
for node, value in node_values.items():
    print(f"Nodo {node}: {value}")