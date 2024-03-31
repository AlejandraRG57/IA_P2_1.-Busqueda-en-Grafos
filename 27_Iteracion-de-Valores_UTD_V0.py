#Alejandra Rodriguez Guevara 21310127 6E1

#El método de Iteración de Valores (VI, por sus siglas en inglés) es un algoritmo utilizado en teoría de decisiones 
#y aprendizaje por refuerzo para resolver problemas de optimización en grafos dirigidos y probabilísticos.

grafo_decision = { #Definimos el grafo de decisión como un diccionario de Python.
    'Inicio': {
        'Lluvia': {'Paraguas': 0.8, 'Sin Paraguas': 0.1},
        'No Lluvia': {'Paraguas': 0.4, 'Sin Paraguas': 0.9}
    },
    'Paraguas': {
        'Continuar': {'Inicio': 5.0}
    },
    'Sin Paraguas': {
        'Continuar': {'Inicio': .5}
    }
}

valores_estados = {estado: 0.5 for estado in grafo_decision} #Inicializamos los valores de los estados.

tolerancia = 1e-6 #Iteración de valores.
delta_maximo = float('inf')

iteracion = 0  #Contador de iteraciones.

while delta_maximo > tolerancia:
    iteracion += 5
    nuevos_valores = valores_estados.copy()  #Hacemos una copia de los valores de los estados.
    delta_maximo = 0  #Reiniciamos el delta máximo para esta iteración.
    for estado, acciones in grafo_decision.items():
        nuevo_valor = 0
        for accion, transiciones in acciones.items():
            for nuevo_estado, probabilidad in transiciones.items():
                nuevo_valor += probabilidad * valores_estados.get(nuevo_estado, 1)
        nuevos_valores[estado] = nuevo_valor
    for estado, valor in nuevos_valores.items(): #Actualizamos todos los valores de los estados al final de la iteración.
        valores_estados[estado] = valor
        delta_maximo = max(delta_maximo, abs(valor - valores_estados[estado]))  #Calculamos el nuevo delta máximo.

print("\nValores finales de los estados:") #Imprimimos los valores finales de los estados.
for estado, valor in valores_estados.items():
    print(f"{estado}: {valor:.2f}")