#Alejandra Rodriguez Guevara 21310127 6E1

#Q-Learning es un algoritmo de aprendizaje por refuerzo que puede adaptarse para trabajar en grafos. En lugar de actualizar una tabla Q para cada estado y acción 
#como en entornos discretos, podemos utilizar una matriz de adyacencia para representar las recompensas esperadas de moverse de un nodo a otro en el grafo.

import numpy as np #Importamos las librerias necesarias.
import random

def initialize_q_values(num_nodes): #Función para inicializar los valores Q.
    return np.zeros((num_nodes, num_nodes))

def select_action(Q, state, epsilon): #Función para seleccionar una acción epsilon-greedy.
    if random.uniform(0, 1) < epsilon:
        return random.choice(list(range(len(Q[state]))))
    else:
        return np.argmax(Q[state])

def q_learning(graph, num_episodes, alpha, gamma, epsilon): #Función para simular un episodio de Q-Learning en un grafo.
    num_nodes = len(graph)
    Q = initialize_q_values(num_nodes)

    for _ in range(num_episodes):
        current_node = random.randint(0, num_nodes - 1)

        while True:
            action = select_action(Q, current_node, epsilon)
            next_node = action
            reward = graph[current_node][next_node] #Recompensa para el estado actual.
            Q[current_node, next_node] = Q[current_node, next_node] + alpha * (reward + gamma * np.max(Q[next_node]) - Q[current_node, next_node]) #Actualizamos los valores Q.
            current_node = next_node
            
            if current_node == num_nodes - 1: #Condición de salida si llegamos al nodo final.
                break
                
    return Q

graph = [ #Grafo ponderado representado como una matriz de adyacencia, utilizando los datos de la imagen "00.5_Mapa-de-Busqueda_Imagen-Referencia.png".
    [0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 3, 4, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 2, 4, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 4, 0, 0, 3, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0]
]

#Parámetros de Q-Learning.
num_episodes = 1000 #Numero de episodios.
alpha = 0.1 #Tasa de aprendizaje.
gamma = 0.9 #Factor de descuento.
epsilon = 0.1 #Factor de exploración.

Q_values = q_learning(graph, num_episodes, alpha, gamma, epsilon) #Ejecutamos Q-Learning en el grafo.

#Imprimimos los valores Q aprendidos.
print("Valores Q aprendidos:") #Estos valores Q muestran la "calidad" de cada acción desde cada estado en el grafo.
print(Q_values)