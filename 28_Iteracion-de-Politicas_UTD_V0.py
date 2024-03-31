#Alejandra Rodriguez Guevara 21310127 6E1

#La iteración de políticas, también conocida como iteración de políticas de mejora, es un algoritmo utilizado en la teoría de control óptimo
#para encontrar la política óptima en un proceso de decisión.

#En un grafo, este algoritmo se utiliza para encontrar la mejor acción a tomar en cada estado para maximizar una función de valor determinada.

grafo_decision = { #Grafo de decisión.
    'Inicio': {
        'Lluvia': {'Paraguas': 0.7, 'Sin Paraguas': 0.2},
        'No Lluvia': {'Paraguas': 0.3, 'Sin Paraguas': 0.9}
    },
    'Paraguas': {
        'Continuar': {'Final': 1.0}
    },
    'Sin Paraguas': {
        'Continuar': {'Final': 1.0}
    },
    'Final': {
        'Rayo': {'Paraguas': 0.9, 'Sin Paraguas': 0.1},
        'No Rayo': {'Paraguas': 0.3, 'Sin Paraguas': 0.7} 
    }
}

politica = { #Inicializamos la política.
    'Inicio': 'Lluvia',
    'Inicio': 'No Lluvia',
    'Paraguas': 'Continuar',
    'Sin Paraguas': 'Continuar',
    'Final': 'Rayo',
    'Final': 'No Rayo'
}

def evaluar_politica(grafo, politica, valores_estados, gamma=1.0, theta=1e-6): #Función para evaluar una política y obtener los valores de los estados.
    delta_maximo = float('inf')
    while delta_maximo > theta:
        delta_maximo = 0
        for estado, acciones in grafo.items():
            valor_anterior = valores_estados[estado]
            accion_elegida = politica[estado]
            nuevo_valor = 0
            for nuevo_estado, probabilidad in acciones[accion_elegida].items():
                nuevo_valor += probabilidad * valores_estados[nuevo_estado]
            valores_estados[estado] = nuevo_valor
            delta_maximo = max(delta_maximo, abs(valor_anterior - valores_estados[estado]))
    return valores_estados

def mejorar_politica(grafo, politica, valores_estados, gamma=1.0): #Función para mejorar una política en función de los valores de los estados.
    politica_estable = True
    for estado, acciones in grafo.items():
        accion_elegida_original = politica[estado]
        mejor_valor = float('-inf')
        mejor_accion = None
        for accion, transiciones in acciones.items():
            nuevo_valor = 0
            for nuevo_estado, probabilidad in transiciones.items():
                nuevo_valor += probabilidad * valores_estados[nuevo_estado]
            if nuevo_valor > mejor_valor:
                mejor_valor = nuevo_valor
                mejor_accion = accion
        politica[estado] = mejor_accion
        if mejor_accion != accion_elegida_original:
            politica_estable = False
    return politica, politica_estable

valores_estados = {estado: 1.0 for estado in grafo_decision} #Iteramos entre evaluación y mejora de la política hasta que la política se estabilice.
politica_estable = False
while not politica_estable:
    valores_estados = evaluar_politica(grafo_decision, politica, valores_estados)
    politica, politica_estable = mejorar_politica(grafo_decision, politica, valores_estados)

print("Valores finales de los estados:") #Imprimimos los valores finales de los estados.
for estado, valor in valores_estados.items():
    print(f"{estado}: {valor:.2f}")

print("\nPolítica óptima:") #Imprimimos la política óptima.
for estado, accion in politica.items():
    print(f"{estado}: {accion}")