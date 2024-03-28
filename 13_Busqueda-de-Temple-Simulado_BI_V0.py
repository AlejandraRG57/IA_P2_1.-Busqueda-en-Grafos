#Alejandra Rodriguez Guevara 21310127 6E1
#Es un algoritmo de optimización estocástica inspirado en el proceso de recocido en metalurgia. 

#Funciona explorando el espacio de búsqueda en busca de soluciones óptimas, 
#permitiendo movimientos que empeoren temporalmente la solución actual con cierta probabilidad, lo que ayuda a evitar quedar atrapado en óptimos locales.

import random #Importamos las librerias necesarias.
import math

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

def cost(solution): #Función de costo para evaluar una solución (ruta) en el grafo.
    total_cost = 0 #Inicializamos el costo total de la solución.
    for i in range(len(solution) - 1):
        start_node = solution[i] #Nodo de inicio de la arista.
        end_node = solution[i + 1] #Nodo final de la arista.
        total_cost += graph[start_node][end_node] #Sumamos el costo de la arista al total.
    return total_cost

def simulated_annealing(initial_solution, temperature, cooling_rate, max_iter):
    current_solution = initial_solution #Inicializamos la solución actual con la solución inicial.
    best_solution = current_solution #Inicializamos la mejor solución con la solución actual.

    for i in range(max_iter):
        temperature *= cooling_rate #Aplicamos el enfriamiento simulado reduciendo la temperatura.
        if temperature == 0: #Si la temperatura llega a cero, salimos del ciclo.
            break

        new_solution = current_solution[:]  #Copiamos la solución actual.
        swap_indices = random.sample(range(len(new_solution)), 2) #Generamos una nueva solución vecina intercambiando dos nodos aleatorios.
        new_solution[swap_indices[0]], new_solution[swap_indices[1]] = new_solution[swap_indices[1]], new_solution[swap_indices[0]]

        delta = cost(new_solution) - cost(current_solution) #Calculamos la diferencia de costo entre la nueva solución y la actual.
        
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature): #Si la nueva solución es mejor o se acepta con una probabilidad dada, actualizamos la solución actual.
            current_solution = new_solution
        
        if cost(current_solution) < cost(best_solution): #Actualizamos la mejor solución encontrada hasta el momento.
            best_solution = current_solution

    return best_solution, cost(best_solution)


initial_solution = [i for i in range(len(graph))]  #Solución inicial estando todos los nodos en orden.
temperature = 1000  #Parámetro inicial de temperatura para el Temple Simulado.
cooling_rate = 0.95 #Tasa de enfriamiento.
max_iter = 1000 #Número máximo de iteraciones.

best_solution, best_cost = simulated_annealing(initial_solution, temperature, cooling_rate, max_iter) #Ejecutamos el algoritmo.

print("Mejor solución encontrada:", best_solution) #Imprimimos los resultados de la ruta más corta posible que visita todos los nodos del grafo.
print("Costo de la mejor solución:", best_cost) #Si el costo es 0, sugiere que esta ruta es óptima en términos de costo.