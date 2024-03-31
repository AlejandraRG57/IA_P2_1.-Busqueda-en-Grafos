#Alejandra Rodriguez Guevara 21310127 6E1

#El método del Valor de la Información (VOI, por sus siglas en inglés) es una técnica utilizada en la teoría de decisiones para cuantificar el valor de adquirir 
#información adicional antes de tomar una decisión. 

#En el contexto de grafos de decisión, el VOI se utiliza para determinar si vale la pena realizar pruebas o investigaciones adicionales antes de tomar una decisión.

import networkx as nx #Importamos la librería necesaria.

grafo_decision = nx.DiGraph() #Creamos un grafo dirigido para representar el problema de decisión.

grafo_decision.add_nodes_from(['Inicio', 'Lluvia', 'No Lluvia', 'Paraguas', 'Sin Paraguas', 'Fin']) #Añadimos los nodos al grafo.

grafo_decision.add_edge('Inicio', 'Lluvia', value=-10) #Añadimos las aristas al grafo con los valores asociados.
grafo_decision.add_edge('Inicio', 'No Lluvia', value=-1)
grafo_decision.add_edge('Lluvia', 'Paraguas', value=-10)
grafo_decision.add_edge('Lluvia', 'Sin Paraguas', value=-1)
grafo_decision.add_edge('No Lluvia', 'Paraguas', value=-1)
grafo_decision.add_edge('No Lluvia', 'Sin Paraguas', value=0)
grafo_decision.add_edge('Paraguas', 'Fin', value=-10)
grafo_decision.add_edge('Sin Paraguas', 'Fin', value=0)

prob_lluvia = 0.4 #Definimos las probabilidades de los eventos inciertos.
prob_no_lluvia = 0.6

prob_lluvia_actualizada = 0.3 #Probabilidades actualizadas después de adquirir información adicional.
prob_no_lluvia_actualizada = 0.7

valor_esperado_sin_verificar = prob_lluvia * (-10) + prob_no_lluvia * (-1) #Calculamos el valor esperado de tomar una decisión sin información adicional.

costo_verificar = 5 #Costo de verificar el pronóstico.

valor_esperado_con_verificar = prob_lluvia_actualizada * (-10) + prob_no_lluvia_actualizada * 0 #Calculamos el valor esperado de tomar una decisión después de adquirir información adicional.

voi = valor_esperado_con_verificar - valor_esperado_sin_verificar - costo_verificar #Calculamos el VOI.

print("Valor esperado sin verificar el pronóstico:", valor_esperado_sin_verificar) #Mostramos los resultados.
print("Valor esperado después de verificar el pronóstico:", valor_esperado_con_verificar)
print("Valor del VOI:", voi)