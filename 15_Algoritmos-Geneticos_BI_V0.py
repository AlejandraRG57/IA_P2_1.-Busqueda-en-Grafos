#Alejandra Rodriguez Guevara 21310127 6E1

#Los algoritmos genéticos son una técnica de optimización y búsqueda inspirada en el proceso de evolución natural. 
#En esencia, los algoritmos genéticos simulan la evolución de una población de soluciones potenciales a lo largo de generaciones, 
#utilizando operadores genéticos como la selección, el cruce y la mutación para producir nuevas generaciones de soluciones. 

#La idea fundamental es que las soluciones que tienen mejores características (evaluadas mediante una función de aptitud o fitness) 
#tienen más probabilidad de sobrevivir y reproducirse, transmitiendo sus características a las generaciones futuras.

import random

class Graph:
    def __init__(self, vertices):
        #Inicializamos el grafo con el número de vértices dado y creamos una matriz de adyacencia inicializada con ceros.
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        #Agregamos una arista entre los vértices u y v, marcando la conexión en la matriz de adyacencia.
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_safe(self, vertex, color, color_assignment):
        #Verificamos si es seguro asignar un color dado a un vértice, comprobando si hay conflictos de color con sus vecinos
        for i in range(self.vertices):
            if self.adj_matrix[vertex][i] == 1 and color_assignment[i] == color:
                return False
        return True

    def get_colors(self, color_assignment):
        #Calculamos el número de colores únicos utilizados en una asignación de colores dada.
        colors = set(color_assignment)
        return len(colors)

def initialize_population(pop_size, num_vertices, num_colors):
    #Inicializamos una población de asignaciones de colores aleatorias para los vértices.
    population = []
    for _ in range(pop_size):
        individual = [random.randint(1, num_colors) for _ in range(num_vertices)]
        population.append(individual)
    return population

def fitness(graph, individual):
    #Calculamos la aptitud de una asignación de colores dada para el grafo, que es el número de colores utilizados.
    return graph.get_colors(individual)

def select_parents(population):
    #Seleccionamos dos padres aleatorios de la población.
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

def crossover(parent1, parent2):
    #Realizamos el operador de cruce entre dos padres para producir dos hijos.
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, num_colors):
    #Realizamos la mutación en un individuo cambiando aleatoriamente el color de un vértice.
    mutation_point = random.randint(0, len(individual) - 1)
    individual[mutation_point] = random.randint(1, num_colors)
    return individual

def genetic_algorithm(graph, pop_size, num_generations, mutation_rate, num_colors):
    #Implementamos el algoritmo genético para encontrar la asignación de colores óptima para el grafo dado.
    population = initialize_population(pop_size, graph.vertices, num_colors)
    for gen in range(num_generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child1 = mutate(child1, num_colors)
            if random.random() < mutation_rate:
                child2 = mutate(child2, num_colors)
            new_population.extend([child1, child2])
        population = new_population
        best_individual = min(population, key=lambda x: fitness(graph, x))
        print(f"Generation {gen+1}, Best Colors: {fitness(graph, best_individual)}")
    best_individual = min(population, key=lambda x: fitness(graph, x))
    return best_individual

#Declaramos nuestras coordenadas y la cantidad de nodos de nuestro grafo en base a la imagen "00.3_Mapa-de-Busqueda_Imagen-Referencia.png".
g = Graph(14)
g.add_edge(0, 6)
g.add_edge(1, 4)
g.add_edge(0, 3)
g.add_edge(2, 0)
g.add_edge(2, 5)
g.add_edge(2, 2) 
g.add_edge(5, 6)
g.add_edge(4, 3)
g.add_edge(4, 1) 
g.add_edge(6, 5)
g.add_edge(7, 3)
g.add_edge(6, 0)
g.add_edge(8, 6)
g.add_edge(9, 4)

#Parámetros del algoritmo genético.
POP_SIZE = 50
NUM_GENERATIONS = 70
MUTATION_RATE = 0.1
NUM_COLORS = 7

#Ejecutamos el algoritmo genético y mostramos la mejor asignación de colores y el número de colores utilizados.
best_color_assignment = genetic_algorithm(g, POP_SIZE, NUM_GENERATIONS, MUTATION_RATE, NUM_COLORS)
print("Best Color Assignment:", best_color_assignment)
print("Number of Colors Used:", g.get_colors(best_color_assignment))