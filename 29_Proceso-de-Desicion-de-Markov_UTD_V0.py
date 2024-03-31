#Alejandra Rodriguez Guevara 21310127 6E1

#Un Proceso de Decisión de Markov (MDP) es un modelo matemático utilizado en el campo de la teoría de la decisión para tomar decisiones secuenciales en un entorno incierto.

#En el contexto de los grafos, los MDP se pueden representar utilizando grafos dirigidos ponderados, donde los nodos representan estados y los bordes representan transiciones 
#entre estados con probabilidades asociadas. Cada nodo puede tener una o más acciones asociadas, y las aristas salientes de un nodo representan las transiciones de estado 
#resultantes de tomar esas acciones.

#Definimos el grafo MDP
grafo_mdp = {
    'A': {
        'Ir a B': {'B': 0.5},
        'Ir a E': {'E': 0.5}
    },
    'B': {
        'Ir a A': {'A': 0.5},
        'Ir a C': {'C': 0.5}
    },
    'C': {
        'Ir a B': {'B': 0.33},
        'Ir a D': {'D': 0.33},
        'Ir a F': {'F': 0.34}
    },
    'D': {
        'Ir a C': {'C': 0.5},
        'Ir a I': {'I': 0.5}
    },
    'E': {
        'Ir a A': {'A': 0.25},
        'Ir a F': {'F': 0.25},
        'Ir a G': {'G': 0.25},
        'Ir a H': {'H': 0.25}
    },
    'F': {
        'Ir a C': {'C': 0.5},
        'Ir a E': {'E': 0.5}
    },
    'G': {
        'Ir a E': {'E': 0.5},
        'Ir a J': {'J': 0.5}
    },
    'H': {
        'Ir a E': {'E': 0.33},
        'Ir a I': {'I': 0.33},
        'Ir a J': {'J': 0.34}
    },
    'I': {
        'Ir a D': {'D': 0.33},
        'Ir a H': {'H': 0.33},
        'Ir a L': {'L': 0.34}
    },
    'J': {
        'Ir a G': {'G': 0.25},
        'Ir a H': {'H': 0.25},
        'Ir a K': {'K': 0.25},
        'Ir a M': {'M': 0.25}
    },
    'K': {
        'Ir a J': {'J': 0.5},
        'Ir a L': {'L': 0.5}
    },
    'L': {
        'Ir a I': {'I': 0.33},
        'Ir a K': {'K': 0.33},
        'Ir a N': {'N': 0.34}
    },
    'M': {
        'Ir a J': {'J': 0.5},
        'Ir a N': {'N': 0.5}
    },
    'N': {
        'Ir a L': {'L': 0.5},
        'Ir a M': {'M': 0.5}
    }
}

def iteracion_politicas(grafo): #Implementamos el algoritmo de iteración de políticas para encontrar la política óptima.
    politica = {}  #Inicializamos la política.
    for estado in grafo.keys():
        politica[estado] = list(grafo[estado].keys())[0]  #Inicializamos la política arbitrariamente.

    politica_estable = False
    while not politica_estable:
        valores_estados = evaluar_politica(grafo, politica)  #Evaluamos la política actual.
        politica, politica_estable = mejorar_politica(grafo, politica, valores_estados)  #Mejoramos la política.
    return politica

def evaluar_politica(grafo, politica, gamma=1.0, theta=1e-6): #Evaluamos la política para obtener los valores de los estados.
    valores_estados = {estado: 0 for estado in grafo.keys()}  #Inicializamos los valores de los estados.
    delta_maximo = float('inf')
    while delta_maximo > theta:
        delta_maximo = 0
        for estado in grafo.keys():
            valor_anterior = valores_estados[estado]
            accion_elegida = politica[estado]
            nuevo_valor = 0
            for nuevo_estado, probabilidad in grafo[estado][accion_elegida].items():
                nuevo_valor += probabilidad * valores_estados[nuevo_estado]
            valores_estados[estado] = nuevo_valor
            delta_maximo = max(delta_maximo, abs(valor_anterior - valores_estados[estado]))
    return valores_estados

def mejorar_politica(grafo, politica, valores_estados, gamma=1.0): #Mejoramos la política en función de los valores de los estados.
    politica_estable = True
    for estado in grafo.keys():
        accion_elegida_original = politica[estado]
        mejor_valor = float('-inf')
        mejor_accion = None
        for accion in grafo[estado].keys():
            nuevo_valor = 0
            for nuevo_estado, probabilidad in grafo[estado][accion].items():
                nuevo_valor += probabilidad * valores_estados[nuevo_estado]
            if nuevo_valor > mejor_valor:
                mejor_valor = nuevo_valor
                mejor_accion = accion
        politica[estado] = mejor_accion
        if mejor_accion != accion_elegida_original:
            politica_estable = False
    return politica, politica_estable

politica_optima = iteracion_politicas(grafo_mdp) #Obtenemos la política óptima.

print("Política óptima:") #Imprimimos la política óptima.
for estado, accion in politica_optima.items():
    print(f"{estado}: {accion}")