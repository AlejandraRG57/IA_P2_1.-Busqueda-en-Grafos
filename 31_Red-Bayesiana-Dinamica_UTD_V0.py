#Alejandra Rodriguez Guevara 21310127 6E1

#Una Red Bayesiana Dinámica en Grafos (DBN por sus siglas en inglés, Dynamic Bayesian Network) es una extensión de las Redes Bayesianas estáticas 
#que modela sistemas que cambian en el tiempo.

import numpy as np #Importamos la libreria numpy como np

class DynamicBayesianNetwork: #Definimos una nueva clase la cual representa una Red Bayesiana Dinámica.
    def __init__(self, num_nodes, num_states): #Definimos el método __init__, el cual es el constructor de la clase.
        self.num_nodes = num_nodes #Inicializamos los atributos de la clase con los valores proporcionados.
        self.num_states = num_states
        self.transition_matrix = np.random.rand(num_states, num_states, num_nodes)  #Matriz de transición.
        self.observation_matrix = np.random.rand(num_states, num_nodes)  #Matriz de observación.
        self.current_state = np.random.randint(0, num_states, num_nodes)  #Estado actual de las variables.

    def transition(self): #Definimos el método transition, el cual realiza una transición en la red.
        new_state = np.zeros_like(self.current_state) #Inicializamos la variable new_state con una matriz de ceros del mismo tamaño que self.current_state.

        for node in range(self.num_nodes): #Iteramos sobre cada nodo en la red.
            prob = self.transition_matrix[:, :, node][:, self.current_state[node]] #Seleccionamos las probabilidades de transición para el nodo actual.
            prob /= np.sum(prob) #Normalizamos las probabilidades para que sumen 1.
            new_state[node] = np.random.choice(self.num_states, p=prob) #Elegimos un nuevo estado para el nodo actual basado en las probabilidades de transición normalizadas.
        self.current_state = new_state #Actualizamos el estado actual de la red con los nuevos estados generados.

    def observe(self): #Definimos el método observe, el cual simula una observación de la red.
        observations = np.zeros(self.num_nodes) #Inicializamos la variable observations con una matriz de ceros del tamaño del número de nodos en la red.
        
        for node in range(self.num_nodes): #Iteramos sobre cada nodo en la red.
            prob = self.observation_matrix[:, node] #Seleccionamos las probabilidades de observación para el nodo actual.
            prob /= np.sum(prob) #Normalizamos las probabilidades para que sumen 1.
            observations[node] = np.random.choice(self.num_states, p=prob) #Elegimos una observación para el nodo actual basada en las probabilidades de observación normalizadas.
        return observations #Devolvemos la matriz de observaciones.


num_nodes = 7 #Definimos el número de nodos y el número de estados posibles para cada nodo.
num_states = 3

dbn = DynamicBayesianNetwork(num_nodes, num_states) #Creamos la red bayesiana dinámica.

print("Estado inicial:", dbn.current_state) #Imprimimos el estado inicial.

dbn.transition() #Realizamos una transición y observamos.
observations = dbn.observe()

print("Nuevo estado después de la transición:", dbn.current_state) #Imprimimos el nuevo estado y las observaciones.
print("Observaciones:", observations)