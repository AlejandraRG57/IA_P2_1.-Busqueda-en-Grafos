#Alejandra Rodriguez Guevara 21310127 6E1
#Teoría de Juegos: Equilibrios y Mecanismos

#La teoría de juegos es un área de las matemáticas y la economía que estudia el comportamiento estratégico de agentes racionales en situaciones de toma de decisiones. 
#En un contexto de juegos, un equilibrio se refiere a un estado en el que ningún jugador tiene incentivos para desviarse unilateralmente de su estrategia actual. Los 
#equilibrios pueden clasificarse en varios tipos, siendo el más común el equilibrio de Nash, donde ningún jugador puede mejorar su posición cambiando su estrategia si 
#los demás jugadores mantienen las suyas.

import networkx as nx #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

def find_nash_equilibrium(G): #Definimos la función para encontrar equilibrios de Nash.
    nash_equilibria = [] #Lista para almacenar los nodos que representan equilibrios de Nash.
    
    for node in G.nodes(): #Iteramos sobre todos los nodos del grafo.
        neighbors = list(G.neighbors(node)) #Lista de vecinos del nodo actual.
        payoff = G[node][neighbors[0]]['weight'] #Pago del jugador.
        neighbors_payoff = G[neighbors[0]][node]['weight'] #Pago del vecino.

        if payoff == max(payoff, neighbors_payoff): #Comprobamos si el pago del jugador es igual al máximo entre el suyo propio y el de su vecino.
            nash_equilibria.append(node) #En caso de ser así el nodo alcanza un equilibrio de Nash.
    return nash_equilibria #Devolvemos la lista de nodos que alcanzan equilibrios de Nash.

G = nx.Graph() #Creamos un grafo vacío.
G.add_edge('A', 'B', weight=3) #Añadimos las aristas con sus respectivos pesos.
G.add_edge('A', 'E', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'F', weight=3)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'I', weight=3)
G.add_edge('E', 'F', weight=3)
G.add_edge('E', 'G', weight=4)
G.add_edge('E', 'H', weight=4)
G.add_edge('G', 'J', weight=2)
G.add_edge('H', 'I', weight=2)
G.add_edge('H', 'J', weight=4)
G.add_edge('I', 'L', weight=3)
G.add_edge('J', 'M', weight=3)
G.add_edge('J', 'K', weight=3)
G.add_edge('K', 'L', weight=4)
G.add_edge('L', 'N', weight=7)
G.add_edge('M', 'N', weight=3)

nash_equilibria = find_nash_equilibrium(G) #Encontramos los equilibrios de Nash.

if nash_equilibria: #Imprimimos los resultados.
    print("Se encontraron equilibrios de Nash en los siguientes nodos:")
    print(nash_equilibria)
else:
    print("No se encontraron equilibrios de Nash en el grafo.")

pos = nx.spring_layout(G) #Posiciones de los nodos para el trazado.
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000) #Dibujamos los nodos.
labels = nx.get_edge_attributes(G, 'weight') #Obtenemos etiquetas de peso de las aristas.
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #Dibujamos etiquetas de peso de las aristas.
plt.show() #Mostramos el gráfico.

#Este código crea un grafo ponderado que representa un juego y busca equilibrios de Nash en él. 
#Luego, imprime los nodos que alcanzan equilibrios de Nash y muestra el grafo con sus pesos de aristas en un gráfico.