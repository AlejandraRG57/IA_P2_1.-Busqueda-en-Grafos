#Alejandra Rodriguez Guevara 21310127 6E1

#Es una técnica de búsqueda similar a la Búsqueda Local pero que explora múltiples soluciones candidatas al mismo tiempo, en lugar de solo una. 
#Cada una de estas soluciones candidatas se conoce como "rayo" o "haz".
#Este enfoque permite una exploración más amplia del espacio de soluciones y puede conducir a mejores resultados.

import random

grafo = [ #Grafo ponderado representado como una matriz de adyacencia, utilizando los datos de la imagen "00.5_Mapa-de-Busqueda_Imagen-Referencia.png".
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

def cost(graph, solution):
    total_cost = 0
    for i in range(len(solution) - 1): #Recorremos los nodos en la solución.
        start_node = solution[i] #Nodo inicial de la arista.
        end_node = solution[i + 1] #Nodo final de la arista.
        total_cost += graph[start_node][end_node]  #Suma el costo de la arista al costo total.
    return total_cost #Devolvemos el costo total de la solución.

def generate_neighbours(grafo, solution, num_neighbours):
    neighbours = [] #Lista para almacenar los vecinos generados.
    for _ in range(num_neighbours):
        new_solution = solution[:]  #Copiamos la solución actual.
        swap_indices = random.sample(range(len(new_solution)), 2) #Seleccionamos aleatoriamente 2 índices para intercambiar.
        new_solution[swap_indices[0]], new_solution[swap_indices[1]] = new_solution[swap_indices[1]], new_solution[swap_indices[0]] #Intercambiamos los nodos en los índices seleccionados.
        neighbours.append(new_solution) #Agregamos el vecino generado a la lista de vecinos.
    return neighbours #Devolvemos la lista de vecinos generados.

def beam_search(graph, initial_solution, beam_width, num_neighbours, max_iter):
    current_solutions = [initial_solution[:] for _ in range(beam_width)] #Inicializamos las soluciones actuales con la solución inicial.
    all_solutions = []  #Lista para almacenar todas las soluciones generadas.
    all_costs = []  #Lista para almacenar los costos correspondientes a todas las soluciones.
    
    for iteration in range(max_iter): #Realizamos el bucle por el número máximo de iteraciones.
        print(f"Iteración {iteration + 1}:") #Imprimiimos el número de iteración actual.

        for idx, solution in enumerate(current_solutions, start=1): #Iteramos sobre las soluciones actuales.
            print(f"Haz {idx}: {solution}, Costo: {cost(grafo, solution)}") #Imprimimos el índice del haz, la solución y su costo.
            all_solutions.append(solution) #Agregamos la solución actual a la lista de todas las soluciones.
            all_costs.append(cost(graph, solution)) #Agregamos el costo de la solución actual a la lista de todos los costos.
        
        neighbours = [] #Inicializamos una lista para almacenar los vecinos.

        for solution in current_solutions:
            neighbours.extend(generate_neighbours(grafo, solution, num_neighbours)) #Extendemos la lista de vecinos con los vecinos generados para la solución actual.
        
        neighbours.sort(key=lambda x: cost(graph, x)) #Ordenamos los vecinos según sus costos.
        current_solutions = neighbours[:beam_width] #Actualizamos las soluciones actuales con los vecinos más prometedores.

    min_cost_index = all_costs.index(min(all_costs)) #Encuontramos el índice del costo mínimo en la lista de todos los costos.
    best_solution = all_solutions[min_cost_index] #Obtenemos la mejor solución correspondiente al costo mínimo.
    best_cost = min(all_costs) #Obtenemos el costo mínimo.
    
    return best_solution, best_cost #Devolvemos la mejor solución y su costo.

initial_solution = [i for i in range(len(grafo))] #Creamos la solución inicial como una lista de nodos consecutivos desde 0 hasta el número de nodos en el grafo.
beam_width = 5  #Definimos el ancho del haz, el cual es el número de soluciones a considerar en cada iteración.
num_neighbours = 5 #Definimos el número de vecinos a generar a partir de cada solución actual en cada iteración.
max_iter = 4 #Definimos el número máximo de iteraciones que el algoritmo realizará antes de detenerse y devolver la mejor solución encontrada.

best_solution, best_cost = beam_search(grafo, initial_solution, beam_width, num_neighbours, max_iter) #Llamamos a la función beam_search() con los parámetros definidos.

print("Mejor Solucion Encontrada:", best_solution) #Imprimimos la mejor solución encontrada por el algoritmo.
print("Costo de la mejor solucion:", best_cost) #Imprimimos el costo asociado a la mejor solución encontrada.
